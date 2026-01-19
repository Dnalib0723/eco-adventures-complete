# 新竹縣環境教育網 - 後端 API

FastAPI 後端服務，提供環境教育平台的資料管理與 API 接口。

## 🚀 快速開始

### 方式一：使用 Docker（推薦）

1. **確保已安裝 Docker 和 Docker Compose**

2. **複製環境變數檔案**
```bash
cp .env.example .env
```

3. **啟動服務**
```bash
docker-compose up -d
```

4. **初始化資料庫資料**
```bash
docker-compose exec api python -m app.db.init_data
```

5. **訪問 API 文件**
- Swagger UI: http://localhost:8000/api/v1/docs
- ReDoc: http://localhost:8000/api/v1/redoc

### 方式二：本地開發

#### 前置需求
- Python 3.11+
- PostgreSQL 15+

#### 安裝步驟

1. **建立虛擬環境**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. **安裝依賴**
```bash
pip install -r requirements.txt
```

3. **設定環境變數**
```bash
cp .env.example .env
# 編輯 .env 檔案，修改資料庫連線資訊
```

4. **建立資料庫**
```bash
# 登入 PostgreSQL
psql -U postgres

# 建立資料庫與使用者
CREATE DATABASE eco_adventures_db;
CREATE USER eco_user WITH PASSWORD 'eco_password';
GRANT ALL PRIVILEGES ON DATABASE eco_adventures_db TO eco_user;
\q
```

5. **初始化資料庫資料**
```bash
python -m app.db.init_data
```

6. **啟動開發伺服器**
```bash
uvicorn app.main:app --reload
```

7. **訪問 API**
- API 根路徑: http://localhost:8000
- Swagger UI: http://localhost:8000/api/v1/docs
- ReDoc: http://localhost:8000/api/v1/redoc

## 📁 專案結構

```
eco-adventures-backend/
├── app/
│   ├── api/                    # API endpoints
│   │   ├── courses.py         # 課程 API
│   │   ├── registrations.py   # 報名 API
│   │   └── others.py          # 其他 API（講師、活動、FAQ）
│   ├── core/                   # 核心配置
│   │   └── config.py          # 應用程式設定
│   ├── db/                     # 資料庫相關
│   │   ├── database.py        # 資料庫連接
│   │   └── init_data.py       # 初始化資料
│   ├── models/                 # 資料模型
│   │   └── models.py          # SQLAlchemy models
│   ├── schemas/                # Pydantic schemas
│   │   └── schemas.py         # API 請求/回應 schemas
│   ├── services/               # 業務邏輯層
│   │   ├── course_service.py
│   │   ├── registration_service.py
│   │   └── other_services.py
│   └── main.py                 # FastAPI 應用程式入口
├── .env.example                # 環境變數範例
├── docker-compose.yml          # Docker Compose 配置
├── Dockerfile                  # Docker 映像檔配置
└── requirements.txt            # Python 依賴

## 🔧 API 端點

### 課程 (Courses)
- `GET /api/v1/courses` - 取得課程列表
- `GET /api/v1/courses/upcoming` - 取得即將開始的課程
- `GET /api/v1/courses/{id}` - 取得單一課程
- `POST /api/v1/courses` - 建立課程（管理員）
- `PUT /api/v1/courses/{id}` - 更新課程（管理員）
- `DELETE /api/v1/courses/{id}` - 刪除課程（管理員）

### 報名 (Registrations)
- `GET /api/v1/registrations` - 取得報名列表（管理員）
- `GET /api/v1/registrations/{id}` - 取得單一報名記錄
- `GET /api/v1/registrations/by-email/{email}` - 查詢報名記錄
- `POST /api/v1/registrations` - 建立報名
- `POST /api/v1/registrations/{id}/cancel` - 取消報名
- `DELETE /api/v1/registrations/{id}` - 刪除報名（管理員）

### 講師 (Instructors)
- `GET /api/v1/instructors` - 取得講師列表
- `GET /api/v1/instructors/{id}` - 取得單一講師
- `POST /api/v1/instructors` - 建立講師（管理員）
- `PUT /api/v1/instructors/{id}` - 更新講師（管理員）
- `DELETE /api/v1/instructors/{id}` - 刪除講師（管理員）

### 活動 (Activities)
- `GET /api/v1/activities` - 取得活動列表
- `GET /api/v1/activities/{id}` - 取得單一活動
- `POST /api/v1/activities` - 建立活動（管理員）
- `PUT /api/v1/activities/{id}` - 更新活動（管理員）
- `DELETE /api/v1/activities/{id}` - 刪除活動（管理員）

### FAQ
- `GET /api/v1/faqs` - 取得 FAQ 列表
- `GET /api/v1/faqs/{id}` - 取得單一 FAQ
- `POST /api/v1/faqs` - 建立 FAQ（管理員）
- `PUT /api/v1/faqs/{id}` - 更新 FAQ（管理員）
- `DELETE /api/v1/faqs/{id}` - 刪除 FAQ（管理員）

## 🗄️ 資料庫設計

### 主要資料表

1. **courses** - 課程
   - 課程資訊、時間、地點
   - 名額管理
   - 講師關聯

2. **registrations** - 報名記錄
   - 報名者資訊
   - 報名狀態管理
   - 課程關聯

3. **instructors** - 講師
   - 講師資料
   - 專長資訊

4. **activities** - 活動
   - 過往活動記錄
   - 活動照片

5. **faqs** - 常見問題
   - 問答內容
   - 分類與排序

6. **users** - 使用者（預留）
   - 會員系統
   - 權限管理

## 🔒 環境變數說明

```env
# 資料庫配置
DATABASE_URL=postgresql://user:password@host:port/database

# API 配置
API_V1_STR=/api/v1
PROJECT_NAME=新竹縣環境教育網 API
DEBUG=True
SECRET_KEY=your-secret-key

# CORS 設定
BACKEND_CORS_ORIGINS=["http://localhost:5173", "http://localhost:3000"]

# Email 配置（選用）
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-password
```

## 📝 開發指南

### 新增 API Endpoint

1. 在 `app/api/` 建立或修改路由檔案
2. 在 `app/services/` 新增業務邏輯
3. 在 `app/main.py` 註冊路由

### 新增資料模型

1. 在 `app/models/models.py` 新增 SQLAlchemy 模型
2. 在 `app/schemas/schemas.py` 新增 Pydantic schema
3. 在 `app/services/` 新增對應的 CRUD 服務

### 資料庫遷移

使用 Alembic 進行資料庫遷移：

```bash
# 建立遷移檔案
alembic revision --autogenerate -m "描述"

# 執行遷移
alembic upgrade head

# 回退遷移
alembic downgrade -1
```

## 🧪 測試

```bash
# 執行測試
pytest

# 執行測試並顯示覆蓋率
pytest --cov=app
```

## 🚢 部署

### Docker 部署

```bash
# 建置映像
docker build -t eco-adventures-api .

# 執行容器
docker run -p 8000:8000 --env-file .env eco-adventures-api
```

### 傳統部署

```bash
# 安裝 gunicorn
pip install gunicorn

# 啟動生產伺服器
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

## 📚 技術棧

- **FastAPI** - 現代化 Python Web 框架
- **SQLAlchemy** - ORM 資料庫工具
- **PostgreSQL** - 關聯式資料庫
- **Pydantic** - 資料驗證
- **Uvicorn** - ASGI 伺服器
- **Docker** - 容器化部署

## 🤝 貢獻

歡迎提交 Pull Request 或開 Issue！

## 📄 授權

MIT License
```

