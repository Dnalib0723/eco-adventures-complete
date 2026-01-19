import { Calendar, Users, Camera } from "lucide-react";
import pastBirdwatching from "@/assets/past-birdwatching.jpg";
import pastCleanup from "@/assets/past-cleanup.jpg";
import pastCraft from "@/assets/past-craft.jpg";

const pastActivities = [
  {
    id: 1,
    image: pastBirdwatching,
    title: "秋季賞鳥生態之旅",
    date: "2025/11/18",
    participants: 32,
    description:
      "帶領親子走入森林，認識台灣常見鳥類與其棲息環境，學員們透過望遠鏡觀察到多種野鳥，收穫滿滿！",
    highlights: ["觀察到 12 種鳥類", "親子共學體驗", "生態解說導覽"],
  },
  {
    id: 2,
    image: pastCleanup,
    title: "海洋守護淨灘行動",
    date: "2025/10/05",
    participants: 58,
    description:
      "結合環境教育與實際行動的淨灘活動，參與者共同清理海岸線垃圾，並認識海洋生態保護的重要性。",
    highlights: ["清理垃圾超過 80 公斤", "海廢藝術創作", "減塑生活分享"],
  },
  {
    id: 3,
    image: pastCraft,
    title: "環保手作工作坊",
    date: "2025/09/21",
    participants: 25,
    description:
      "利用回收素材製作鳥屋與小盆栽，讓學員體驗手作樂趣的同時，也學習資源再利用的環保概念。",
    highlights: ["手作鳥屋帶回家", "環保素材運用", "綠色生活實踐"],
  },
];

const PastActivitiesSection = () => {
  return (
    <section id="past-activities" className="section-padding">
      <div className="container-nature">
        <div className="text-center mb-12">
          <h2 className="text-2xl md:text-4xl font-bold text-foreground mb-4">
            過去活動成果
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
            回顧我們舉辦過的精彩活動，一起感受學員們的熱情與學習成果
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
          {pastActivities.map((activity) => (
            <div key={activity.id} className="nature-card overflow-hidden group">
              {/* Image */}
              <div className="relative h-52 overflow-hidden">
                <img
                  src={activity.image}
                  alt={activity.title}
                  className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-foreground/60 to-transparent" />
                <div className="absolute bottom-4 left-4 right-4">
                  <h3 className="text-lg font-semibold text-primary-foreground mb-1">
                    {activity.title}
                  </h3>
                  <div className="flex items-center gap-4 text-primary-foreground/80 text-sm">
                    <span className="flex items-center gap-1">
                      <Calendar className="w-4 h-4" />
                      {activity.date}
                    </span>
                    <span className="flex items-center gap-1">
                      <Users className="w-4 h-4" />
                      {activity.participants} 人參與
                    </span>
                  </div>
                </div>
              </div>

              {/* Content */}
              <div className="p-5">
                <p className="text-muted-foreground text-sm mb-4 leading-relaxed">
                  {activity.description}
                </p>

                {/* Highlights */}
                <div className="flex flex-wrap gap-2">
                  {activity.highlights.map((highlight) => (
                    <span
                      key={highlight}
                      className="px-3 py-1 rounded-full text-xs font-medium bg-primary/10 text-primary"
                    >
                      {highlight}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>

        <div className="text-center mt-10">
          <button className="btn-nature-outline inline-flex items-center gap-2">
            <Camera className="w-5 h-5" />
            查看更多活動照片
          </button>
        </div>
      </div>
    </section>
  );
};

export default PastActivitiesSection;
