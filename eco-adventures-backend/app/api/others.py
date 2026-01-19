from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.schemas import (
    Instructor, InstructorCreate, InstructorUpdate,
    Activity, ActivityCreate, ActivityUpdate,
    FAQ, FAQCreate, FAQUpdate,
    Message
)
from app.services.other_services import InstructorService, ActivityService, FAQService

# ============ 講師 API ============
instructor_router = APIRouter()


@instructor_router.get("/", response_model=List[Instructor])
def get_instructors(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    is_active: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    """取得講師列表"""
    instructors = InstructorService.get_multi(
        db=db, skip=skip, limit=limit, is_active=is_active
    )
    return instructors


@instructor_router.get("/{instructor_id}", response_model=Instructor)
def get_instructor(instructor_id: int, db: Session = Depends(get_db)):
    """取得單一講師"""
    instructor = InstructorService.get(db=db, instructor_id=instructor_id)
    if not instructor:
        raise HTTPException(status_code=404, detail="講師不存在")
    return instructor


@instructor_router.post("/", response_model=Instructor, status_code=201)
def create_instructor(
    instructor_in: InstructorCreate,
    db: Session = Depends(get_db)
):
    """建立新講師"""
    instructor = InstructorService.create(db=db, instructor_in=instructor_in)
    return instructor


@instructor_router.put("/{instructor_id}", response_model=Instructor)
def update_instructor(
    instructor_id: int,
    instructor_in: InstructorUpdate,
    db: Session = Depends(get_db)
):
    """更新講師資訊"""
    instructor = InstructorService.update(
        db=db, instructor_id=instructor_id, instructor_in=instructor_in
    )
    if not instructor:
        raise HTTPException(status_code=404, detail="講師不存在")
    return instructor


@instructor_router.delete("/{instructor_id}", response_model=Message)
def delete_instructor(instructor_id: int, db: Session = Depends(get_db)):
    """刪除講師"""
    success = InstructorService.delete(db=db, instructor_id=instructor_id)
    if not success:
        raise HTTPException(status_code=404, detail="講師不存在")
    return {"message": "講師已成功刪除"}


# ============ 活動 API ============
activity_router = APIRouter()


@activity_router.get("/", response_model=List[Activity])
def get_activities(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """取得活動列表"""
    activities = ActivityService.get_multi(
        db=db, skip=skip, limit=limit, category=category
    )
    return activities


@activity_router.get("/{activity_id}", response_model=Activity)
def get_activity(activity_id: int, db: Session = Depends(get_db)):
    """取得單一活動"""
    activity = ActivityService.get(db=db, activity_id=activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="活動不存在")
    return activity


@activity_router.post("/", response_model=Activity, status_code=201)
def create_activity(
    activity_in: ActivityCreate,
    db: Session = Depends(get_db)
):
    """建立新活動"""
    activity = ActivityService.create(db=db, activity_in=activity_in)
    return activity


@activity_router.put("/{activity_id}", response_model=Activity)
def update_activity(
    activity_id: int,
    activity_in: ActivityUpdate,
    db: Session = Depends(get_db)
):
    """更新活動資訊"""
    activity = ActivityService.update(
        db=db, activity_id=activity_id, activity_in=activity_in
    )
    if not activity:
        raise HTTPException(status_code=404, detail="活動不存在")
    return activity


@activity_router.delete("/{activity_id}", response_model=Message)
def delete_activity(activity_id: int, db: Session = Depends(get_db)):
    """刪除活動"""
    success = ActivityService.delete(db=db, activity_id=activity_id)
    if not success:
        raise HTTPException(status_code=404, detail="活動不存在")
    return {"message": "活動已成功刪除"}


# ============ FAQ API ============
faq_router = APIRouter()


@faq_router.get("/", response_model=List[FAQ])
def get_faqs(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    is_active: Optional[bool] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """取得 FAQ 列表"""
    faqs = FAQService.get_multi(
        db=db, skip=skip, limit=limit, is_active=is_active, category=category
    )
    return faqs


@faq_router.get("/{faq_id}", response_model=FAQ)
def get_faq(faq_id: int, db: Session = Depends(get_db)):
    """取得單一 FAQ"""
    faq = FAQService.get(db=db, faq_id=faq_id)
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ 不存在")
    return faq


@faq_router.post("/", response_model=FAQ, status_code=201)
def create_faq(faq_in: FAQCreate, db: Session = Depends(get_db)):
    """建立新 FAQ"""
    faq = FAQService.create(db=db, faq_in=faq_in)
    return faq


@faq_router.put("/{faq_id}", response_model=FAQ)
def update_faq(
    faq_id: int,
    faq_in: FAQUpdate,
    db: Session = Depends(get_db)
):
    """更新 FAQ"""
    faq = FAQService.update(db=db, faq_id=faq_id, faq_in=faq_in)
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ 不存在")
    return faq


@faq_router.delete("/{faq_id}", response_model=Message)
def delete_faq(faq_id: int, db: Session = Depends(get_db)):
    """刪除 FAQ"""
    success = FAQService.delete(db=db, faq_id=faq_id)
    if not success:
        raise HTTPException(status_code=404, detail="FAQ 不存在")
    return {"message": "FAQ 已成功刪除"}
