import { useState } from "react";
import { ChevronDown } from "lucide-react";

const faqs = [
  {
    question: "如何報名參加課程？",
    answer:
      "您可以直接在本網站點選想參加的課程，填寫報名表單即可完成報名。報名成功後，我們會寄送確認信至您的電子信箱。",
  },
  {
    question: "報名後可以取消嗎？",
    answer:
      "如需取消報名，請於活動前 3 天透過電話或 Email 與我們聯繫。若因天候因素取消活動，我們會另行通知並安排改期或全額退費。",
  },
  {
    question: "參加課程需要收費嗎？",
    answer:
      "本網站提供的環境教育課程多為免費或收取材料費，詳細費用資訊請參考各課程頁面說明。",
  },
  {
    question: "活動適合什麼年齡參加？",
    answer:
      "我們的課程適合各年齡層參與，部分親子課程建議 6 歲以上小朋友參加。每堂課程頁面會詳細說明適合對象，請依課程說明報名。",
  },
  {
    question: "下雨天活動會照常舉行嗎？",
    answer:
      "若遇輕微陣雨，戶外活動會照常舉行，請自備雨具。若遇颱風或大雨等惡劣天候，我們會提前通知並協調改期。",
  },
];

const FAQSection = () => {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  return (
    <section id="faq" className="section-padding">
      <div className="container-nature">
        <div className="text-center mb-12">
          <h2 className="text-2xl md:text-4xl font-bold text-foreground mb-4">
            常見問題
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
            在報名前，您可能想知道的事情都在這裡
          </p>
        </div>

        <div className="max-w-3xl mx-auto space-y-3">
          {faqs.map((faq, index) => (
            <div
              key={index}
              className="nature-card overflow-hidden"
            >
              <button
                onClick={() => setOpenIndex(openIndex === index ? null : index)}
                className="w-full flex items-center justify-between p-5 text-left"
              >
                <span className="font-medium text-foreground pr-4">
                  {faq.question}
                </span>
                <ChevronDown
                  className={`w-5 h-5 text-primary flex-shrink-0 transition-transform duration-300 ${
                    openIndex === index ? "rotate-180" : ""
                  }`}
                />
              </button>
              <div
                className={`overflow-hidden transition-all duration-300 ${
                  openIndex === index ? "max-h-48" : "max-h-0"
                }`}
              >
                <p className="px-5 pb-5 text-muted-foreground leading-relaxed">
                  {faq.answer}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FAQSection;
