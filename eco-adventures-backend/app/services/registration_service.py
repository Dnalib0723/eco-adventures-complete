from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models.models import Registration, RegistrationStatus, CourseStatus
from app.schemas.schemas import RegistrationCreate, RegistrationUpdate
from app.services.course_service import CourseService


class RegistrationService:
    """報名服務類別"""
    
    @staticmethod
    def get(db: Session, registration_id: int) -> Optional[Registration]:
        """取得單一報名記錄"""
        return db.query(Registration).filter(Registration.id == registration_id).first()
    
    @staticmethod
    def get_multi(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        course_id: Optional[int] = None,
        user_id: Optional[int] = None,
        status: Optional[RegistrationStatus] = None
    ) -> List[Registration]:
        """取得報名列表"""
        query = db.query(Registration)
        
        if course_id:
            query = query.filter(Registration.course_id == course_id)
        if user_id:
            query = query.filter(Registration.user_id == user_id)
        if status:
            query = query.filter(Registration.status == status)
        
        return query.order_by(desc(Registration.created_at)).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_email(db: Session, email: str) -> List[Registration]:
        """根據 email 取得報名記錄"""
        return db.query(Registration).filter(Registration.email == email).all()
    
    @staticmethod
    def create(db: Session, registration_in: RegistrationCreate) -> Optional[Registration]:
        """建立報名記錄"""
        # 檢查課程是否存在
        course = CourseService.get(db, registration_in.course_id)
        if not course:
            return None
        
        # 檢查課程狀態
        if course.status == CourseStatus.FULL:
            # 如果課程已額滿，加入候補
            registration_in_dict = registration_in.model_dump()
            registration = Registration(**registration_in_dict)
            registration.status = RegistrationStatus.WAITLIST
            db.add(registration)
            db.commit()
            db.refresh(registration)
            return registration
        
        # 檢查名額
        available_spots = course.max_spots - course.current_registrations
        if available_spots < registration_in.participants:
            return None  # 名額不足
        
        # 建立報名記錄
        registration_in_dict = registration_in.model_dump()
        registration = Registration(**registration_in_dict)
        registration.status = RegistrationStatus.CONFIRMED
        
        db.add(registration)
        db.commit()
        
        # 更新課程報名人數（根據參加人數增加）
        for _ in range(registration_in.participants):
            CourseService.increment_registration(db, registration_in.course_id)
        
        db.refresh(registration)
        return registration
    
    @staticmethod
    def update(
        db: Session,
        registration_id: int,
        registration_in: RegistrationUpdate
    ) -> Optional[Registration]:
        """更新報名記錄"""
        registration = db.query(Registration).filter(
            Registration.id == registration_id
        ).first()
        
        if not registration:
            return None
        
        update_data = registration_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(registration, field, value)
        
        db.commit()
        db.refresh(registration)
        return registration
    
    @staticmethod
    def cancel(db: Session, registration_id: int) -> Optional[Registration]:
        """取消報名"""
        registration = db.query(Registration).filter(
            Registration.id == registration_id
        ).first()
        
        if not registration:
            return None
        
        # 如果是已確認的報名，需要釋放名額
        if registration.status == RegistrationStatus.CONFIRMED:
            for _ in range(registration.participants):
                CourseService.decrement_registration(db, registration.course_id)
        
        registration.status = RegistrationStatus.CANCELLED
        db.commit()
        db.refresh(registration)
        
        return registration
    
    @staticmethod
    def delete(db: Session, registration_id: int) -> bool:
        """刪除報名記錄"""
        registration = db.query(Registration).filter(
            Registration.id == registration_id
        ).first()
        
        if not registration:
            return False
        
        # 如果是已確認的報名，需要釋放名額
        if registration.status == RegistrationStatus.CONFIRMED:
            for _ in range(registration.participants):
                CourseService.decrement_registration(db, registration.course_id)
        
        db.delete(registration)
        db.commit()
        return True
    
    @staticmethod
    def get_count(db: Session, course_id: Optional[int] = None) -> int:
        """取得報名總數"""
        query = db.query(Registration)
        if course_id:
            query = query.filter(Registration.course_id == course_id)
        return query.count()
    
    @staticmethod
    def check_duplicate(db: Session, email: str, course_id: int) -> bool:
        """檢查是否重複報名"""
        existing = db.query(Registration).filter(
            Registration.email == email,
            Registration.course_id == course_id,
            Registration.status != RegistrationStatus.CANCELLED
        ).first()
        return existing is not None
