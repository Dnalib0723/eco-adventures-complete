from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, Date, Time, Enum
from sqlalchemy.orm import relationship
import enum

from app.db.database import Base


class CourseCategory(str, enum.Enum):
    """課程類別"""
    NATURE_EXPLORE = "自然探索"
    WORKSHOP = "體驗活動"
    LECTURE = "主題講座"
    OTHER = "其他"


class CourseStatus(str, enum.Enum):
    """課程狀態"""
    UPCOMING = "即將開始"
    ONGOING = "報名中"
    FULL = "已額滿"
    COMPLETED = "已結束"
    CANCELLED = "已取消"


class RegistrationStatus(str, enum.Enum):
    """報名狀態"""
    PENDING = "待確認"
    CONFIRMED = "已確認"
    CANCELLED = "已取消"
    WAITLIST = "候補中"


class User(Base):
    """使用者模型"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100))
    phone = Column(String(20))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 關聯
    registrations = relationship("Registration", back_populates="user")


class Instructor(Base):
    """講師模型"""
    __tablename__ = "instructors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    title = Column(String(100))
    description = Column(Text)
    image_url = Column(String(500))
    specialties = Column(Text)  # JSON 字串，儲存專長列表
    email = Column(String(255))
    phone = Column(String(20))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 關聯
    courses = relationship("Course", back_populates="instructor")


class Course(Base):
    """課程模型"""
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    category = Column(Enum(CourseCategory), default=CourseCategory.OTHER)
    status = Column(Enum(CourseStatus), default=CourseStatus.UPCOMING)
    
    # 時間與地點
    date = Column(Date, nullable=False)
    start_time = Column(Time)
    end_time = Column(Time)
    location = Column(String(200))
    
    # 名額管理
    max_spots = Column(Integer, default=30)
    current_registrations = Column(Integer, default=0)
    
    # 講師
    instructor_id = Column(Integer, ForeignKey("instructors.id"))
    
    # 圖片與附加資訊
    image_url = Column(String(500))
    requirements = Column(Text)  # 參加條件
    notes = Column(Text)  # 注意事項
    
    # 時間戳記
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 關聯
    instructor = relationship("Instructor", back_populates="courses")
    registrations = relationship("Registration", back_populates="course")


class Registration(Base):
    """報名記錄模型"""
    __tablename__ = "registrations"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # 課程與使用者
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # 允許訪客報名
    
    # 報名者資訊（訪客報名時使用）
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    
    # 報名詳情
    participants = Column(Integer, default=1)
    status = Column(Enum(RegistrationStatus), default=RegistrationStatus.PENDING)
    
    # 備註
    notes = Column(Text)
    
    # 時間戳記
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 關聯
    course = relationship("Course", back_populates="registrations")
    user = relationship("User", back_populates="registrations")


class Activity(Base):
    """過往活動模型"""
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    category = Column(String(50))
    date = Column(Date)
    location = Column(String(200))
    image_url = Column(String(500))
    participants_count = Column(Integer)
    
    # 活動詳情
    highlights = Column(Text)  # 活動亮點
    photos = Column(Text)  # JSON 字串，儲存照片 URL 列表
    
    # 時間戳記
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class FAQ(Base):
    """常見問題模型"""
    __tablename__ = "faqs"
    
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(500), nullable=False)
    answer = Column(Text, nullable=False)
    category = Column(String(50))
    order = Column(Integer, default=0)  # 顯示順序
    is_active = Column(Boolean, default=True)
    
    # 時間戳記
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
