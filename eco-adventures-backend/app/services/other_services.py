from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import desc
import json

from app.models.models import Instructor, Activity, FAQ
from app.schemas.schemas import (
    InstructorCreate, InstructorUpdate,
    ActivityCreate, ActivityUpdate,
    FAQCreate, FAQUpdate
)


class InstructorService:
    """講師服務類別"""
    
    @staticmethod
    def get(db: Session, instructor_id: int) -> Optional[Instructor]:
        """取得單一講師"""
        return db.query(Instructor).filter(Instructor.id == instructor_id).first()
    
    @staticmethod
    def get_multi(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        is_active: Optional[bool] = None
    ) -> List[Instructor]:
        """取得講師列表"""
        query = db.query(Instructor)
        
        if is_active is not None:
            query = query.filter(Instructor.is_active == is_active)
        
        return query.offset(skip).limit(limit).all()
    
    @staticmethod
    def create(db: Session, instructor_in: InstructorCreate) -> Instructor:
        """建立講師"""
        instructor_data = instructor_in.model_dump()
        # 將專長列表轉換為 JSON 字串
        if 'specialties' in instructor_data:
            instructor_data['specialties'] = json.dumps(
                instructor_data['specialties'], ensure_ascii=False
            )
        
        instructor = Instructor(**instructor_data)
        db.add(instructor)
        db.commit()
        db.refresh(instructor)
        return instructor
    
    @staticmethod
    def update(
        db: Session,
        instructor_id: int,
        instructor_in: InstructorUpdate
    ) -> Optional[Instructor]:
        """更新講師"""
        instructor = db.query(Instructor).filter(Instructor.id == instructor_id).first()
        if not instructor:
            return None
        
        update_data = instructor_in.model_dump(exclude_unset=True)
        # 將專長列表轉換為 JSON 字串
        if 'specialties' in update_data:
            update_data['specialties'] = json.dumps(
                update_data['specialties'], ensure_ascii=False
            )
        
        for field, value in update_data.items():
            setattr(instructor, field, value)
        
        db.commit()
        db.refresh(instructor)
        return instructor
    
    @staticmethod
    def delete(db: Session, instructor_id: int) -> bool:
        """刪除講師"""
        instructor = db.query(Instructor).filter(Instructor.id == instructor_id).first()
        if not instructor:
            return False
        
        db.delete(instructor)
        db.commit()
        return True


class ActivityService:
    """活動服務類別"""
    
    @staticmethod
    def get(db: Session, activity_id: int) -> Optional[Activity]:
        """取得單一活動"""
        return db.query(Activity).filter(Activity.id == activity_id).first()
    
    @staticmethod
    def get_multi(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        category: Optional[str] = None
    ) -> List[Activity]:
        """取得活動列表"""
        query = db.query(Activity)
        
        if category:
            query = query.filter(Activity.category == category)
        
        return query.order_by(desc(Activity.date)).offset(skip).limit(limit).all()
    
    @staticmethod
    def create(db: Session, activity_in: ActivityCreate) -> Activity:
        """建立活動"""
        activity_data = activity_in.model_dump()
        # 將照片列表轉換為 JSON 字串
        if 'photos' in activity_data:
            activity_data['photos'] = json.dumps(
                activity_data['photos'], ensure_ascii=False
            )
        
        activity = Activity(**activity_data)
        db.add(activity)
        db.commit()
        db.refresh(activity)
        return activity
    
    @staticmethod
    def update(
        db: Session,
        activity_id: int,
        activity_in: ActivityUpdate
    ) -> Optional[Activity]:
        """更新活動"""
        activity = db.query(Activity).filter(Activity.id == activity_id).first()
        if not activity:
            return None
        
        update_data = activity_in.model_dump(exclude_unset=True)
        # 將照片列表轉換為 JSON 字串
        if 'photos' in update_data:
            update_data['photos'] = json.dumps(
                update_data['photos'], ensure_ascii=False
            )
        
        for field, value in update_data.items():
            setattr(activity, field, value)
        
        db.commit()
        db.refresh(activity)
        return activity
    
    @staticmethod
    def delete(db: Session, activity_id: int) -> bool:
        """刪除活動"""
        activity = db.query(Activity).filter(Activity.id == activity_id).first()
        if not activity:
            return False
        
        db.delete(activity)
        db.commit()
        return True


class FAQService:
    """FAQ 服務類別"""
    
    @staticmethod
    def get(db: Session, faq_id: int) -> Optional[FAQ]:
        """取得單一 FAQ"""
        return db.query(FAQ).filter(FAQ.id == faq_id).first()
    
    @staticmethod
    def get_multi(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        is_active: Optional[bool] = None,
        category: Optional[str] = None
    ) -> List[FAQ]:
        """取得 FAQ 列表"""
        query = db.query(FAQ)
        
        if is_active is not None:
            query = query.filter(FAQ.is_active == is_active)
        if category:
            query = query.filter(FAQ.category == category)
        
        return query.order_by(FAQ.order, FAQ.created_at).offset(skip).limit(limit).all()
    
    @staticmethod
    def create(db: Session, faq_in: FAQCreate) -> FAQ:
        """建立 FAQ"""
        faq = FAQ(**faq_in.model_dump())
        db.add(faq)
        db.commit()
        db.refresh(faq)
        return faq
    
    @staticmethod
    def update(db: Session, faq_id: int, faq_in: FAQUpdate) -> Optional[FAQ]:
        """更新 FAQ"""
        faq = db.query(FAQ).filter(FAQ.id == faq_id).first()
        if not faq:
            return None
        
        update_data = faq_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(faq, field, value)
        
        db.commit()
        db.refresh(faq)
        return faq
    
    @staticmethod
    def delete(db: Session, faq_id: int) -> bool:
        """刪除 FAQ"""
        faq = db.query(FAQ).filter(FAQ.id == faq_id).first()
        if not faq:
            return False
        
        db.delete(faq)
        db.commit()
        return True
