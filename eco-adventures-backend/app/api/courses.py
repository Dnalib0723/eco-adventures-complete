from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.schemas import Course, CourseCreate, CourseUpdate, Message
from app.services.course_service import CourseService
from app.models.models import CourseStatus, CourseCategory

router = APIRouter()


@router.get("/", response_model=List[Course])
def get_courses(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    status: Optional[CourseStatus] = None,
    category: Optional[CourseCategory] = None,
    db: Session = Depends(get_db)
):
    """
    取得課程列表
    
    - **skip**: 略過的項目數（分頁用）
    - **limit**: 限制回傳的項目數
    - **status**: 課程狀態篩選（選填）
    - **category**: 課程類別篩選（選填）
    """
    courses = CourseService.get_multi(
        db=db,
        skip=skip,
        limit=limit,
        status=status,
        category=category
    )
    return courses


@router.get("/upcoming", response_model=List[Course])
def get_upcoming_courses(
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    """
    取得即將開始的課程
    
    - **limit**: 限制回傳的課程數量（預設 10）
    """
    courses = CourseService.get_upcoming(db=db, limit=limit)
    return courses


@router.get("/{course_id}", response_model=Course)
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    """
    取得單一課程詳細資訊
    
    - **course_id**: 課程 ID
    """
    course = CourseService.get(db=db, course_id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="課程不存在")
    return course


@router.post("/", response_model=Course, status_code=201)
def create_course(
    course_in: CourseCreate,
    db: Session = Depends(get_db)
):
    """
    建立新課程
    
    需要管理員權限（暫未實作權限驗證）
    """
    course = CourseService.create(db=db, course_in=course_in)
    return course


@router.put("/{course_id}", response_model=Course)
def update_course(
    course_id: int,
    course_in: CourseUpdate,
    db: Session = Depends(get_db)
):
    """
    更新課程資訊
    
    需要管理員權限（暫未實作權限驗證）
    """
    course = CourseService.update(db=db, course_id=course_id, course_in=course_in)
    if not course:
        raise HTTPException(status_code=404, detail="課程不存在")
    return course


@router.delete("/{course_id}", response_model=Message)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    """
    刪除課程
    
    需要管理員權限（暫未實作權限驗證）
    """
    success = CourseService.delete(db=db, course_id=course_id)
    if not success:
        raise HTTPException(status_code=404, detail="課程不存在")
    return {"message": "課程已成功刪除"}


@router.get("/stats/count")
def get_course_count(db: Session = Depends(get_db)):
    """
    取得課程總數
    """
    count = CourseService.get_count(db=db)
    return {"count": count}
