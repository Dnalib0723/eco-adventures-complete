import { ShieldCheck, Droplets, Bug, CigaretteOff, TreePine } from "lucide-react";

const features = [
  {
    icon: ShieldCheck,
    title: "環境衛生推動",
    description: "推動環境衛生相關政策與措施",
  },
  {
    icon: Droplets,
    title: "公廁管理",
    description: "管理與維護公共廁所設施",
  },
  {
    icon: Bug,
    title: "登革熱防治",
    description: "防治登革熱疫情，保護民眾健康",
  },
  {
    icon: CigaretteOff,
    title: "菸蒂減量",
    description: "推動菸蒂減量，維護環境整潔",
  },
  {
    icon: TreePine,
    title: "環境維護",
    description: "維護公共環境設施與品質",
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
            「臺東縣美質環境資訊網」是一個專注於美質環境資訊與教育推廣的專業網站，
            我們致力於整合並提供即將舉辦、正在進行以及過去的美質環境教育課程與活動資訊。
          </p>
          <p className="text-muted-foreground text-lg leading-relaxed mt-4">
            透過溫暖、友善且容易使用的網站設計，
            希望讓每一位對環境、衛生與永續議題有興趣的民眾，
            都能輕鬆找到適合自己的課程，並實際參與美質環境行動。
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6">
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
