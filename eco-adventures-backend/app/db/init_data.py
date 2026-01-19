"""
初始化資料庫資料
執行方式: python -m app.db.init_data
"""

from datetime import date, time
from sqlalchemy.orm import Session

from app.db.database import SessionLocal, engine, Base
from app.models.models import Course, Instructor, Activity, FAQ, CourseCategory, CourseStatus
import json

# 建立資料庫表格
Base.metadata.create_all(bind=engine)


def init_instructors(db: Session):
    """初始化講師資料"""
    instructors = [
        {
            "name": "林老師",
            "title": "資深生態解說員",
            "description": "長期投入環境教育推廣，擅長生態解說與戶外教學，帶領過數百場自然探索活動，深受學員喜愛。",
            "image_url": "/images/instructors/instructor-lin.jpg",
            "specialties": json.dumps(["生態解說", "戶外教學", "鳥類觀察"], ensure_ascii=False),
            "email": "lin@eco-adventures.com",
            "phone": "0912-345-678"
        },
        {
            "name": "陳老師",
            "title": "永續發展講師",
            "description": "專精於永續發展與環境議題,教學風格親切活潑，善於將複雜的環境概念以淺顯易懂的方式傳達給學員。",
            "image_url": "/images/instructors/instructor-chen.jpg",
            "specialties": json.dumps(["永續發展", "環境教育", "綠色生活"], ensure_ascii=False),
            "email": "chen@eco-adventures.com",
            "phone": "0923-456-789"
        }
    ]
    
    for instructor_data in instructors:
        instructor = Instructor(**instructor_data)
        db.add(instructor)
    
    db.commit()
    print("✓ 講師資料初始化完成")


def init_courses(db: Session):
    """初始化課程資料"""
    courses = [
        {
            "title": "春日森林探索營",
            "description": "帶領親子走入自然森林，認識台灣原生植物與昆蟲生態，體驗大自然的奧妙。",
            "category": CourseCategory.NATURE_EXPLORE,
            "status": CourseStatus.ONGOING,
            "date": date(2026, 2, 15),
            "start_time": time(9, 0),
            "end_time": time(16, 0),
            "location": "新竹縣自然公園",
            "max_spots": 15,
            "current_registrations": 0,
            "instructor_id": 1,
            "image_url": "/images/courses/activity-explore.jpg",
            "requirements": "適合親子參加，建議穿著運動服裝與防滑鞋",
            "notes": "請自備水壺、防曬用品與防蚊液"
        },
        {
            "title": "生態種植體驗工作坊",
            "description": "透過實際操作學習有機種植技術，認識永續農業的重要性，並帶回自己種植的小盆栽。",
            "category": CourseCategory.WORKSHOP,
            "status": CourseStatus.ONGOING,
            "date": date(2026, 2, 22),
            "start_time": time(13, 30),
            "end_time": time(17, 0),
            "location": "環境教育中心",
            "max_spots": 20,
            "current_registrations": 0,
            "instructor_id": 2,
            "image_url": "/images/courses/activity-workshop.jpg",
            "requirements": "無特殊限制，歡迎對園藝有興趣的民眾參加",
            "notes": "現場提供所有工具與材料"
        },
        {
            "title": "永續生活實踐講座",
            "description": "邀請專家分享如何在日常生活中實踐永續理念，從減塑、節能到環保消費一次學會。",
            "category": CourseCategory.LECTURE,
            "status": CourseStatus.UPCOMING,
            "date": date(2026, 3, 1),
            "start_time": time(14, 0),
            "end_time": time(16, 30),
            "location": "縣立圖書館",
            "max_spots": 50,
            "current_registrations": 0,
            "instructor_id": 2,
            "image_url": "/images/courses/activity-lecture.jpg",
            "requirements": "開放所有民眾參加",
            "notes": "現場提供講義與筆記本"
        }
    ]
    
    for course_data in courses:
        course = Course(**course_data)
        db.add(course)
    
    db.commit()
    print("✓ 課程資料初始化完成")


def init_activities(db: Session):
    """初始化活動資料"""
    activities = [
        {
            "title": "淨灘護海洋",
            "description": "與社區夥伴一起清理海灘垃圾，保護海洋生態",
            "category": "環保行動",
            "date": date(2025, 12, 10),
            "location": "新竹海灘",
            "image_url": "/images/activities/past-cleanup.jpg",
            "participants_count": 45,
            "highlights": "清理垃圾約 150 公斤，並進行海洋廢棄物分類教學",
            "photos": json.dumps([
                "/images/activities/past-cleanup.jpg"
            ], ensure_ascii=False)
        },
        {
            "title": "賞鳥趣",
            "description": "專業講師帶領認識新竹地區常見鳥類",
            "category": "自然探索",
            "date": date(2025, 11, 25),
            "location": "新竹濕地公園",
            "image_url": "/images/activities/past-birdwatching.jpg",
            "participants_count": 28,
            "highlights": "觀察到 15 種鳥類，包括稀有的黑面琵鷺",
            "photos": json.dumps([
                "/images/activities/past-birdwatching.jpg"
            ], ensure_ascii=False)
        },
        {
            "title": "環保手作日",
            "description": "利用回收材料製作實用生活小物",
            "category": "體驗活動",
            "date": date(2025, 11, 15),
            "location": "環境教育中心",
            "image_url": "/images/activities/past-craft.jpg",
            "participants_count": 32,
            "highlights": "學員創作出多件精美的環保作品",
            "photos": json.dumps([
                "/images/activities/past-craft.jpg"
            ], ensure_ascii=False)
        }
    ]
    
    for activity_data in activities:
        activity = Activity(**activity_data)
        db.add(activity)
    
    db.commit()
    print("✓ 活動資料初始化完成")


def init_faqs(db: Session):
    """初始化 FAQ 資料"""
    faqs = [
        {
            "question": "如何報名課程？",
            "answer": "您可以在課程頁面點擊「立即報名」按鈕，填寫相關資料後送出即可。報名成功後會收到確認信。",
            "category": "報名相關",
            "order": 1
        },
        {
            "question": "可以取消報名嗎？",
            "answer": "可以的！請至少在課程開始前 3 天透過 email 或電話聯絡我們取消報名。",
            "category": "報名相關",
            "order": 2
        },
        {
            "question": "課程需要準備什麼？",
            "answer": "每門課程的準備事項不同，請參考課程頁面的「注意事項」欄位。一般建議攜帶水壺、防曬用品與舒適的服裝。",
            "category": "課程相關",
            "order": 3
        },
        {
            "question": "課程適合什麼年齡參加？",
            "answer": "我們有針對不同年齡設計的課程。親子課程適合 5 歲以上兒童，一般課程建議 12 歲以上。詳細資訊請參考各課程說明。",
            "category": "課程相關",
            "order": 4
        },
        {
            "question": "如何成為志工？",
            "answer": "我們歡迎熱心的志工加入！請來信至 volunteer@eco-adventures.com 或致電 03-1234-5678 詢問志工招募資訊。",
            "category": "其他",
            "order": 5
        }
    ]
    
    for faq_data in faqs:
        faq = FAQ(**faq_data)
        db.add(faq)
    
    db.commit()
    print("✓ FAQ 資料初始化完成")


def main():
    """主函數"""
    print("開始初始化資料庫資料...")
    
    db = SessionLocal()
    try:
        # 檢查是否已有資料
        if db.query(Instructor).count() > 0:
            print("⚠ 資料庫已有資料，跳過初始化")
            return
        
        init_instructors(db)
        init_courses(db)
        init_activities(db)
        init_faqs(db)
        
        print("\n✓✓✓ 所有資料初始化完成！✓✓✓")
        print("\n您可以使用以下指令啟動 API 伺服器：")
        print("  uvicorn app.main:app --reload")
        
    except Exception as e:
        print(f"✗ 初始化失敗: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()