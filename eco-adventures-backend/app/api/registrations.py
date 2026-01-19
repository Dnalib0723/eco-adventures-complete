from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.schemas import (
    Registration, RegistrationCreate, RegistrationUpdate,
    RegistrationWithCourse, Message
)
from app.services.registration_service import RegistrationService
from app.models.models import RegistrationStatus

router = APIRouter()


@router.get("/", response_model=List[Registration])
def get_registrations(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    course_id: Optional[int] = None,
    status: Optional[RegistrationStatus] = None,
    db: Session = Depends(get_db)
):
    """
    取得報名列表
    
    - **skip**: 略過的項目數（分頁用）
    - **limit**: 限制回傳的項目數
    - **course_id**: 課程 ID 篩選（選填）
    - **status**: 報名狀態篩選（選填）
    
    需要管理員權限（暫未實作權限驗證）
    """
    registrations = RegistrationService.get_multi(
        db=db,
        skip=skip,
        limit=limit,
        course_id=course_id,
        status=status
    )
    return registrations


@router.get("/by-email/{email}", response_model=List[RegistrationWithCourse])
def get_registrations_by_email(
    email: str,
    db: Session = Depends(get_db)
):
    """
    根據 email 查詢報名記錄
    
    - **email**: 報名時使用的電子信箱
    """
    registrations = RegistrationService.get_by_email(db=db, email=email)
    return registrations


@router.get("/{registration_id}", response_model=Registration)
def get_registration(
    registration_id: int,
    db: Session = Depends(get_db)
):
    """
    取得單一報名記錄
    
    - **registration_id**: 報名 ID
    """
    registration = RegistrationService.get(db=db, registration_id=registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="報名記錄不存在")
    return registration


@router.post("/", response_model=Registration, status_code=201)
def create_registration(
    registration_in: RegistrationCreate,
    db: Session = Depends(get_db)
):
    """
    建立新報名
    
    - 會自動檢查課程名額
    - 如果名額已滿，會加入候補名單
    - 會檢查是否重複報名
    """
    # 檢查是否重複報名
    if RegistrationService.check_duplicate(
        db=db,
        email=registration_in.email,
        course_id=registration_in.course_id
    ):
        raise HTTPException(
            status_code=400,
            detail="此信箱已經報名過這門課程"
        )
    
    registration = RegistrationService.create(db=db, registration_in=registration_in)
    if not registration:
        raise HTTPException(
            status_code=400,
            detail="報名失敗，課程可能不存在或名額不足"
        )
    
    return registration


@router.put("/{registration_id}", response_model=Registration)
def update_registration(
    registration_id: int,
    registration_in: RegistrationUpdate,
    db: Session = Depends(get_db)
):
    """
    更新報名記錄
    
    需要管理員權限（暫未實作權限驗證）
    """
    registration = RegistrationService.update(
        db=db,
        registration_id=registration_id,
        registration_in=registration_in
    )
    if not registration:
        raise HTTPException(status_code=404, detail="報名記錄不存在")
    return registration


@router.post("/{registration_id}/cancel", response_model=Registration)
def cancel_registration(
    registration_id: int,
    db: Session = Depends(get_db)
):
    """
    取消報名
    
    - 會自動釋放課程名額
    - 報名狀態會變更為「已取消」
    """
    registration = RegistrationService.cancel(db=db, registration_id=registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="報名記錄不存在")
    return registration


@router.delete("/{registration_id}", response_model=Message)
def delete_registration(
    registration_id: int,
    db: Session = Depends(get_db)
):
    """
    刪除報名記錄
    
    需要管理員權限（暫未實作權限驗證）
    """
    success = RegistrationService.delete(db=db, registration_id=registration_id)
    if not success:
        raise HTTPException(status_code=404, detail="報名記錄不存在")
    return {"message": "報名記錄已成功刪除"}


@router.get("/stats/count")
def get_registration_count(
    course_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """
    取得報名總數
    
    - **course_id**: 特定課程的報名數（選填）
    """
    count = RegistrationService.get_count(db=db, course_id=course_id)
    return {"count": count}
