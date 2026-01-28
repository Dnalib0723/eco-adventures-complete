import heroImage from "@/assets/hero-nature.jpg";
import { ChevronDown } from "lucide-react";

const HeroSection = () => {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Background Image */}
      <div className="absolute inset-0">
        <img
          src={heroImage}
          alt="可愛的森林動物們歡迎您來到環境教育世界"
          className="w-full h-full object-cover"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-background/30 via-transparent to-background" />
      </div>

      {/* Content */}
      <div className="relative z-10 container-nature px-4 text-center pt-20">
        <div className="max-w-3xl mx-auto bg-background/80 backdrop-blur-sm rounded-3xl p-8 md:p-12 shadow-card">
          <h1 className="text-3xl md:text-5xl lg:text-6xl font-bold text-foreground mb-6 animate-fade-in leading-tight">
            歡迎來到
            <span className="block text-primary mt-2">臺東縣美質環境資訊網</span>
          </h1>
          
          <p className="text-lg md:text-xl text-muted-foreground mb-8 animate-fade-in opacity-0 [animation-delay:200ms] leading-relaxed">
            一個陪你美質生活、認識環境、
            <br className="hidden sm:block" />
            一起學習永續生活的環境教育平台
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center animate-fade-in opacity-0 [animation-delay:400ms]">
            <a href="#courses" className="btn-nature text-lg px-8 py-4">
              探索課程
            </a>
            <a href="#about" className="btn-nature-outline text-lg px-8 py-4">
              了解更多
            </a>
          </div>
        </div>
      </div>

      {/* Scroll Indicator */}
      <a
        href="#about"
        className="absolute bottom-8 left-1/2 -translate-x-1/2 text-primary animate-bounce-gentle"
        aria-label="向下滾動"
      >
        <ChevronDown className="w-8 h-8" />
      </a>
    </section>
  );
};

export default HeroSection;
