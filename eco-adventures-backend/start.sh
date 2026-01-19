#!/bin/bash

echo "========================================"
echo "新竹縣環境教育網 - 後端 API 啟動"
echo "========================================"
echo

# 檢查 Python 是否安裝
if ! command -v python3 &> /dev/null; then
    echo "[錯誤] 找不到 Python！"
    echo "請先安裝 Python 3.11 或更高版本"
    exit 1
fi

echo "[1/4] 檢查 Python 版本..."
python3 --version

echo
echo "[2/4] 安裝依賴套件..."
pip3 install fastapi uvicorn sqlalchemy python-dotenv pydantic pydantic-settings email-validator python-multipart

echo
echo "[3/4] 設定環境變數..."
if [ ! -f .env ]; then
    cp .env.sqlite .env
    echo "已建立 .env 檔案"
fi

echo
echo "[4/4] 初始化資料庫..."
python3 -m app.db.init_data

echo
echo "========================================"
echo "啟動中... 請稍候"
echo "========================================"
echo
echo "API 將在以下網址運行:"
echo "  - API 根路徑: http://localhost:8000"
echo "  - API 文檔: http://localhost:8000/api/v1/docs"
echo
echo "按 Ctrl+C 停止伺服器"
echo "========================================"
echo

# 啟動伺服器
python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
