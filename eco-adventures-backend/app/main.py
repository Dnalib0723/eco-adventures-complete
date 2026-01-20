from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.database import engine, Base
from app.api import courses, registrations, others

# 建立資料庫表格
Base.metadata.create_all(bind=engine)

# 建立 FastAPI 應用程式
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
)

# 設定 CORS - 允許所有 localhost 端口
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000", 
        "http://localhost:8080",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8080",
        "https://eehcepb.com", 
        "https://www.eehcepb.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 註冊路由
app.include_router(
    courses.router,
    prefix=f"{settings.API_V1_STR}/courses",
    tags=["courses"]
)
app.include_router(
    registrations.router,
    prefix=f"{settings.API_V1_STR}/registrations",
    tags=["registrations"]
)
app.include_router(
    others.instructor_router,
    prefix=f"{settings.API_V1_STR}/instructors",
    tags=["instructors"]
)
app.include_router(
    others.activity_router,
    prefix=f"{settings.API_V1_STR}/activities",
    tags=["activities"]
)
app.include_router(
    others.faq_router,
    prefix=f"{settings.API_V1_STR}/faqs",
    tags=["faqs"]
)


@app.get("/")
def root():
    """API 根路徑"""
    return {
        "message": "歡迎使用新竹縣環境教育網 API",
        "version": "1.0.0",
        "docs": f"{settings.API_V1_STR}/docs"
    }


@app.get("/health")
def health_check():
    """健康檢查端點"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )