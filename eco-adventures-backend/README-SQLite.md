# 🚀 SQLite 版本 - 快速啟動（不需要 Docker）

這是簡化版本，使用 SQLite 資料庫，不需要 Docker 或 PostgreSQL！

## ✅ 前置需求

只需要 **Python 3.11+**！

檢查方式：
```bash
python --version
# 或
python3 --version
```

如果沒有 Python，請從 https://www.python.org/downloads/ 下載安裝。

---

## 🎯 最快啟動方式

### Windows 用戶

1. **雙擊執行 `start.bat`**
2. 就這樣！系統會自動完成所有設定

### macOS/Linux 用戶

```bash
chmod +x start.sh
./start.sh
```

---

## 📖 手動啟動（如果腳本失敗）

### 步驟 1：安裝依賴

```bash
pip install fastapi uvicorn sqlalchemy python-dotenv pydantic pydantic-settings email-validator python-multipart
```

### 步驟 2：設定環境變數

```bash
# Windows
copy .env.sqlite .env

# macOS/Linux
cp .env.sqlite .env
```

### 步驟 3：初始化資料庫

```bash
python -m app.db.init_data
```

### 步驟 4：啟動伺服器

```bash
python -m uvicorn app.main:app --reload
```

---

## ✅ 驗證

開啟瀏覽器訪問：

- **API 文檔**：http://localhost:8000/api/v1/docs
- **健康檢查**：http://localhost:8000/health

應該看到 `{"status": "healthy"}`

---

## 🗄️ 資料庫檔案

SQLite 會在專案目錄建立 `eco_adventures.db` 檔案，所有資料都儲存在這裡。

**優點**：
- ✅ 簡單易用
- ✅ 不需要額外服務
- ✅ 單一檔案，方便備份

**注意**：
- ⚠️ 不適合高流量生產環境（但開發和小型專案完全足夠）
- ⚠️ 不支援多個同時寫入的連線

---

## 🔄 切換回 PostgreSQL

如果之後想切換回 PostgreSQL：

1. 安裝 PostgreSQL
2. 修改 `.env` 中的 `DATABASE_URL`：
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/database
   ```
3. 安裝額外的依賴：
   ```bash
   pip install psycopg2-binary
   ```
4. 重新執行初始化：
   ```bash
   python -m app.db.init_data
   ```

---

## 🐛 常見問題

### 問題 1：找不到 Python

**解決**：安裝 Python 3.11+ from https://www.python.org/downloads/

安裝時記得勾選「Add Python to PATH」！

### 問題 2：pip 指令失敗

**解決**：
```bash
# 使用 python -m pip
python -m pip install fastapi uvicorn sqlalchemy python-dotenv pydantic pydantic-settings email-validator python-multipart
```

### 問題 3：埠號被佔用

**解決**：修改啟動指令的埠號
```bash
python -m uvicorn app.main:app --reload --port 8001
```

然後前端的 `.env` 也要改成 `VITE_API_URL=http://localhost:8001`

---

## 📊 效能比較

| 功能 | SQLite | PostgreSQL |
|------|--------|------------|
| 開發使用 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 設定複雜度 | ⭐ | ⭐⭐⭐⭐ |
| 生產環境 | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| 備份還原 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

**結論**：SQLite 非常適合開發和測試！

---

祝開發順利！🌱✨
