import { Leaf, Heart, Users, Sparkles } from "lucide-react";

const features = [
  {
    icon: Leaf,
    title: "美質生活",
    description: "帶領民眾走入自然，認識生態與環境資源",
  },
  {
    icon: Heart,
    title: "環境守護",
    description: "透過互動與實作，加深環境保護觀念",
  },
  {
    icon: Users,
    title: "專業師資",
    description: "邀請專業講師分享環境知識與實務經驗",
  },
  {
    icon: Sparkles,
    title: "寓教於樂",
    description: "讓環境教育成為一件輕鬆、有趣又有意義的事",
  },
];

const AboutSection = () => {
  return (
    <section id="about" className="section-padding bg-secondary/50">
      <div className="container-nature">
        <div className="max-w-3xl mx-auto text-center mb-12 md:mb-16">
          <h2 className="text-2xl md:text-4xl font-bold text-foreground mb-6">
            關於我們
          </h2>
          <p className="text-muted-foreground text-lg leading-relaxed">
            「臺東縣美質環境資訊網」是一個專注於環境資訊與教育推廣的專業網站，
            我們致力於整合並提供即將舉辦、正在進行以及過去的環境教育課程與活動資訊。
          </p>
          <p className="text-muted-foreground text-lg leading-relaxed mt-4">
            透過溫暖、友善且容易使用的網站設計，
            希望讓每一位對環境、生態與永續議題有興趣的民眾，
            都能輕鬆找到適合自己的課程，並實際參與環境行動。
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((feature, index) => (
            <div
              key={feature.title}
              className="nature-card p-6 text-center group"
              style={{ animationDelay: `${index * 100}ms` }}
            >
              <div className="w-16 h-16 rounded-2xl bg-primary/10 flex items-center justify-center mx-auto mb-4 group-hover:bg-primary/20 transition-colors">
                <feature.icon className="w-8 h-8 text-primary" />
              </div>
              <h3 className="text-lg font-semibold text-foreground mb-2">
                {feature.title}
              </h3>
              <p className="text-muted-foreground text-sm">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default AboutSection;
