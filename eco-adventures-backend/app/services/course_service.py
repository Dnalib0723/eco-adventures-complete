from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.models.models import Course, CourseStatus
from app.schemas.schemas import CourseCreate, CourseUpdate


class CourseService:
    """課程服務類別"""
    
    @staticmethod
    def get(db: Session, course_id: int) -> Optional[Course]:
        """取得單一課程"""
        return db.query(Course).filter(Course.id == course_id).first()
    
    @staticmethod
    def get_multi(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        status: Optional[CourseStatus] = None,
        category: Optional[str] = None
    ) -> List[Course]:
        """取得課程列表"""
        query = db.query(Course)
        
        if status:
            query = query.filter(Course.status == status)
        if category:
            query = query.filter(Course.category == category)
        
        return query.order_by(desc(Course.date)).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_upcoming(db: Session, limit: int = 10) -> List[Course]:
        """取得即將開始的課程"""
        return db.query(Course).filter(
            Course.status.in_([CourseStatus.UPCOMING, CourseStatus.ONGOING])
        ).order_by(Course.date).limit(limit).all()
    
    @staticmethod
    def create(db: Session, course_in: CourseCreate) -> Course:
        """建立課程"""
        course = Course(**course_in.model_dump())
        db.add(course)
        db.commit()
        db.refresh(course)
        return course
    
    @staticmethod
    def update(db: Session, course_id: int, course_in: CourseUpdate) -> Optional[Course]:
        """更新課程"""
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            return None
        
        update_data = course_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(course, field, value)
        
        db.commit()
        db.refresh(course)
        return course
    
    @staticmethod
    def delete(db: Session, course_id: int) -> bool:
        """刪除課程"""
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            return False
        
        db.delete(course)
        db.commit()
        return True
    
    @staticmethod
    def increment_registration(db: Session, course_id: int) -> Optional[Course]:
        """增加報名人數"""
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            return None
        
        course.current_registrations += 1
        
        # 檢查是否額滿
        if course.current_registrations >= course.max_spots:
            course.status = CourseStatus.FULL
        
        db.commit()
        db.refresh(course)
        return course
    
    @staticmethod
    def decrement_registration(db: Session, course_id: int) -> Optional[Course]:
        """減少報名人數"""
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            return None
        
        if course.current_registrations > 0:
            course.current_registrations -= 1
            
            # 如果原本額滿，現在有名額了
            if course.status == CourseStatus.FULL:
                course.status = CourseStatus.ONGOING
        
        db.commit()
        db.refresh(course)
        return course
    
    @staticmethod
    def get_count(db: Session) -> int:
        """取得課程總數"""
        return db.query(Course).count()
