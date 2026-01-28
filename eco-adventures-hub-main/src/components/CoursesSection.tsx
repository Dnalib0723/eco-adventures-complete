import { useState, useEffect } from "react";
import CourseCard from "./CourseCard";
import RegistrationModal from "./RegistrationModal";
import { courseAPI } from "@/lib/api";
import { useToast } from "@/hooks/use-toast";

interface Course {
  id: number;
  image_url: string;
  title: string;
  description: string;
  date: string;
  start_time?: string;
  end_time?: string;
  location: string;
  available_spots: number;
  category: string;
  max_spots: number;
  current_registrations: number;
}

const CoursesSection = () => {
  const [courses, setCourses] = useState<Course[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedCourse, setSelectedCourse] = useState<Course | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const { toast } = useToast();

  // 載入課程資料
  useEffect(() => {
    const fetchCourses = async () => {
      try {
        setLoading(true);
        const data = await courseAPI.getUpcoming(10);
        setCourses(data);
      } catch (error) {
        console.error("載入課程失敗:", error);
        toast({
          variant: "destructive",
          title: "載入失敗",
          description: "無法載入課程資料，請稍後再試",
        });
      } finally {
        setLoading(false);
      }
    };

    fetchCourses();
  }, [toast]);

  const handleRegister = (course: Course) => {
    setSelectedCourse(course);
    setIsModalOpen(true);
  };

  // 格式化時間顯示
  const formatTime = (course: Course) => {
    if (course.start_time && course.end_time) {
      return `${course.start_time.slice(0, 5)}-${course.end_time.slice(0, 5)}`;
    }
    return "時間未定";
  };

  return (
    <section id="courses" className="section-padding">
      <div className="container-nature">
        <div className="text-center mb-12">
          <h2 className="text-2xl md:text-4xl font-bold text-foreground mb-4">
            近期課程活動
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
            每一場課程皆強調學習趣味性與實際參與感，
            讓美質環境教育成為一件輕鬆、有趣又有意義的事情。
          </p>
        </div>

        {loading ? (
          <div className="text-center py-12">
            <p className="text-muted-foreground">載入中...</p>
          </div>
        ) : courses.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-muted-foreground">目前沒有可報名的課程</p>
          </div>
        ) : (
          <>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
              {courses.map((course) => (
                <CourseCard
                  key={course.id}
                  id={course.id}
                  image={course.image_url}
                  title={course.title}
                  description={course.description}
                  date={course.date}
                  time={formatTime(course)}
                  location={course.location}
                  spots={course.available_spots}
                  category={course.category}
                  onRegister={() => handleRegister(course)}
                />
              ))}
            </div>

            <div className="text-center mt-10">
              <button className="btn-nature-outline">
                查看更多課程
              </button>
            </div>
          </>
        )}
      </div>

      <RegistrationModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        course={selectedCourse ? {
          id: selectedCourse.id,
          title: selectedCourse.title,
          date: selectedCourse.date,
          time: formatTime(selectedCourse),
          location: selectedCourse.location,
        } : null}
      />
    </section>
  );
};

export default CoursesSection;
