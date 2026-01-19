from datetime import datetime, date, time
from typing import Optional, List
from pydantic import BaseModel, EmailStr, validator
from app.models.models import CourseCategory, CourseStatus, RegistrationStatus


# ============ Course Schemas ============

class CourseBase(BaseModel):
    """課程基礎 Schema"""
    title: str
    description: Optional[str] = None
    category: CourseCategory = CourseCategory.OTHER
    date: date
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    location: Optional[str] = None
    max_spots: int = 30
    instructor_id: Optional[int] = None
    image_url: Optional[str] = None
    requirements: Optional[str] = None
    notes: Optional[str] = None


class CourseCreate(CourseBase):
    """建立課程 Schema"""
    pass


class CourseUpdate(BaseModel):
    """更新課程 Schema"""
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[CourseCategory] = None
    status: Optional[CourseStatus] = None
    date: Optional[date] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    location: Optional[str] = None
    max_spots: Optional[int] = None
    instructor_id: Optional[int] = None
    image_url: Optional[str] = None
    requirements: Optional[str] = None
    notes: Optional[str] = None


class CourseInDB(CourseBase):
    """資料庫中的課程 Schema"""
    id: int
    status: CourseStatus
    current_registrations: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class Course(CourseInDB):
    """課程回應 Schema（包含講師資訊）"""
    instructor: Optional['InstructorSimple'] = None
    available_spots: int = 0
    
    @validator('available_spots', always=True)
    def calculate_available_spots(cls, v, values):
        return values.get('max_spots', 0) - values.get('current_registrations', 0)


# ============ Instructor Schemas ============

class InstructorBase(BaseModel):
    """講師基礎 Schema"""
    name: str
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    specialties: Optional[List[str]] = []
    email: Optional[EmailStr] = None
    phone: Optional[str] = None


class InstructorCreate(InstructorBase):
    """建立講師 Schema"""
    pass


class InstructorUpdate(BaseModel):
    """更新講師 Schema"""
    name: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    specialties: Optional[List[str]] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None


class InstructorSimple(BaseModel):
    """簡化的講師 Schema（用於課程中顯示）"""
    id: int
    name: str
    title: Optional[str] = None
    image_url: Optional[str] = None
    
    class Config:
        from_attributes = True


class Instructor(InstructorBase):
    """講師回應 Schema"""
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


# ============ Registration Schemas ============

class RegistrationBase(BaseModel):
    """報名基礎 Schema"""
    name: str
    email: EmailStr
    phone: str
    participants: int = 1
    notes: Optional[str] = None
    
    @validator('participants')
    def validate_participants(cls, v):
        if v < 1 or v > 5:
            raise ValueError('報名人數必須在 1-5 人之間')
        return v


class RegistrationCreate(RegistrationBase):
    """建立報名 Schema"""
    course_id: int


class RegistrationUpdate(BaseModel):
    """更新報名 Schema"""
    status: Optional[RegistrationStatus] = None
    notes: Optional[str] = None


class Registration(RegistrationBase):
    """報名回應 Schema"""
    id: int
    course_id: int
    status: RegistrationStatus
    created_at: datetime
    
    class Config:
        from_attributes = True


class RegistrationWithCourse(Registration):
    """包含課程資訊的報名 Schema"""
    course: CourseInDB


# ============ Activity Schemas ============

class ActivityBase(BaseModel):
    """活動基礎 Schema"""
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    date: Optional[date] = None
    location: Optional[str] = None
    image_url: Optional[str] = None
    participants_count: Optional[int] = None
    highlights: Optional[str] = None
    photos: Optional[List[str]] = []


class ActivityCreate(ActivityBase):
    """建立活動 Schema"""
    pass


class ActivityUpdate(BaseModel):
    """更新活動 Schema"""
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    date: Optional[date] = None
    location: Optional[str] = None
    image_url: Optional[str] = None
    participants_count: Optional[int] = None
    highlights: Optional[str] = None
    photos: Optional[List[str]] = None


class Activity(ActivityBase):
    """活動回應 Schema"""
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


# ============ FAQ Schemas ============

class FAQBase(BaseModel):
    """FAQ 基礎 Schema"""
    question: str
    answer: str
    category: Optional[str] = None
    order: int = 0


class FAQCreate(FAQBase):
    """建立 FAQ Schema"""
    pass


class FAQUpdate(BaseModel):
    """更新 FAQ Schema"""
    question: Optional[str] = None
    answer: Optional[str] = None
    category: Optional[str] = None
    order: Optional[int] = None
    is_active: Optional[bool] = None


class FAQ(FAQBase):
    """FAQ 回應 Schema"""
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


# ============ User Schemas ============

class UserBase(BaseModel):
    """使用者基礎 Schema"""
    email: EmailStr
    full_name: Optional[str] = None
    phone: Optional[str] = None


class UserCreate(UserBase):
    """建立使用者 Schema"""
    password: str


class UserUpdate(BaseModel):
    """更新使用者 Schema"""
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None


class User(UserBase):
    """使用者回應 Schema"""
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


# ============ 通用回應 Schemas ============

class Message(BaseModel):
    """通用訊息 Schema"""
    message: str


class PaginatedResponse(BaseModel):
    """分頁回應 Schema"""
    items: List
    total: int
    page: int
    page_size: int
    total_pages: int


# 更新 forward references
Course.model_rebuild()
