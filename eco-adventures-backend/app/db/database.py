from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from app.core.config import settings

# 建立資料庫引擎
# 支援 SQLite 和 PostgreSQL
DATABASE_URL = getattr(settings, 'DATABASE_URL', 'sqlite:///./eco_adventures.db')

# SQLite 特殊配置
if DATABASE_URL.startswith('sqlite'):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},  # SQLite 需要
        echo=settings.DEBUG
    )
else:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        echo=settings.DEBUG
    )

# 建立 Session 工廠
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 宣告式基底類別
Base = declarative_base()


# 依賴注入：取得資料庫 session
def get_db():
    """
    FastAPI 依賴注入函數
    用於在 API endpoint 中取得資料庫 session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
