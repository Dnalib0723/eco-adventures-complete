import { MapPin, Phone, Mail, Clock } from "lucide-react";

const contactInfo = [
  {
    icon: MapPin,
    label: "地址",
    value: "新竹縣竹北市環境路 123 號",
  },
  {
    icon: Phone,
    label: "電話",
    value: "03-1234-5678",
  },
  {
    icon: Mail,
    label: "電子信箱",
    value: "ecoedu@example.com",
  },
  {
    icon: Clock,
    label: "服務時間",
    value: "週一至週五 09:00 - 17:00",
  },
];

const ContactSection = () => {
  return (
    <section id="contact" className="section-padding bg-primary text-primary-foreground">
      <div className="container-nature">
        <div className="text-center mb-12">
          <h2 className="text-2xl md:text-4xl font-bold mb-4">
            聯絡我們
          </h2>
          <p className="text-primary-foreground/80 text-lg max-w-2xl mx-auto">
            有任何問題或想法，歡迎與我們聯繫
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 max-w-5xl mx-auto">
          {contactInfo.map((item) => (
            <div
              key={item.label}
              className="bg-primary-foreground/10 backdrop-blur-sm rounded-2xl p-6 text-center"
            >
              <div className="w-12 h-12 rounded-full bg-primary-foreground/20 flex items-center justify-center mx-auto mb-4">
                <item.icon className="w-6 h-6" />
              </div>
              <p className="text-sm text-primary-foreground/70 mb-1">
                {item.label}
              </p>
              <p className="font-medium">
                {item.value}
              </p>
            </div>
          ))}
        </div>

        <div className="text-center mt-12">
          <a
            href="mailto:ecoedu@example.com"
            className="inline-flex items-center justify-center px-8 py-4 rounded-full font-medium bg-primary-foreground text-primary hover:bg-primary-foreground/90 transition-colors"
          >
            寄信給我們
          </a>
        </div>
      </div>
    </section>
  );
};

export default ContactSection;
