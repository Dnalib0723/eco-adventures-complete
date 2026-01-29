import { Check, MapPin } from "lucide-react";
// import instructorLin from "@/assets/instructor-lin.jpg";
// import instructorChen from "@/assets/instructor-chen.jpg";

/* ========================================
   原始講師資料 - 已註解保留
   ======================================== */
// const instructors = [
//   {
//     image: instructorLin,
//     name: "林老師",
//     title: "資深生態解說員",
//     description:
//       "長期投入環境教育推廣，擅長生態解說與戶外教學，帶領過數百場自然探索活動，深受學員喜愛。",
//     specialties: ["生態解說", "戶外教學", "鳥類觀察"],
//   },
//   {
//     image: instructorChen,
//     name: "陳老師",
//     title: "永續發展講師",
//     description:
//       "專精於永續發展與環境議題，教學風格親切活潑，善於將複雜的環境概念以淺顯易懂的方式傳達給學員。",
//     specialties: ["永續發展", "環境教育", "綠色生活"],
//   },
// ];

/* ========================================
   新的地圖熱點功能資料
   ======================================== */
const mapFeatures = [
  {
    icon: Check,
    text: "地圖化呈現公廁與環境熱點",
  },
  {
    icon: Check,
    text: "公開巡檢成果",
  },
  {
    icon: Check,
    text: "彙整宣導資訊",
  },
  {
    icon: Check,
    text: "未來擴充民眾通報功能",
  },
];

const InstructorsSection = () => {
  return (
    <section id="instructors" className="section-padding bg-secondary/50">
      <div className="container-nature">
        {/* ========================================
            原始講師區塊 - 已註解保留
            ======================================== */}
        {/* <div className="text-center mb-12">
          <h2 className="text-2xl md:text-4xl font-bold text-foreground mb-4">
            專業講師團隊
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
            我們邀請具有豐富經驗的專業講師，帶領您深入認識環境與生態的美好
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
          {instructors.map((instructor) => (
            <div key={instructor.name} className="nature-card p-6 flex flex-col sm:flex-row gap-6">
              <div className="flex-shrink-0">
                <img
                  src={instructor.image}
                  alt={instructor.name}
                  className="w-24 h-24 sm:w-32 sm:h-32 rounded-2xl object-cover mx-auto sm:mx-0"
                />
              </div>
              <div className="flex-1 text-center sm:text-left">
                <h3 className="text-xl font-semibold text-foreground mb-1">
                  {instructor.name}
                </h3>
                <p className="text-primary font-medium text-sm mb-3">
                  {instructor.title}
                </p>
                <p className="text-muted-foreground text-sm mb-4">
                  {instructor.description}
                </p>
                <div className="flex flex-wrap gap-2 justify-center sm:justify-start">
                  {instructor.specialties.map((specialty) => (
                    <span
                      key={specialty}
                      className="px-3 py-1 rounded-full text-xs font-medium bg-muted text-muted-foreground"
                    >
                      {specialty}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div> */}

        {/* ========================================
            新的地圖熱點區塊
            ======================================== */}
        <div className="max-w-6xl mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-center">
            {/* 左側：文字內容 */}
            <div className="space-y-6">
              <div>
                <h2 className="text-2xl md:text-4xl font-bold text-foreground mb-4">
                  美質環境一目了然
                </h2>
                <p className="text-muted-foreground text-lg max-w-2xl">
                  整合公廁管理、環境熱點與巡檢成果，以互動地圖呈現，讓環境品質資訊透明公開
                </p>
              </div>

              {/* 功能列表 */}
              <div className="space-y-4">
                {mapFeatures.map((feature, index) => (
                  <div key={index} className="flex items-start gap-3">
                    <div className="flex-shrink-0 w-8 h-8 rounded-full bg-primary/20 flex items-center justify-center mt-1">
                      <feature.icon className="w-5 h-5 text-primary" />
                    </div>
                    <p className="text-foreground text-lg flex-1 pt-1">
                      {feature.text}
                    </p>
                  </div>
                ))}
              </div>
            </div>

            {/* 右側：地圖視覺區 */}
            <div className="relative">
              <div className="nature-card overflow-hidden">
                <div className="aspect-[4/3] bg-gradient-to-br from-primary/5 to-accent/5 flex items-center justify-center">
                  {/* 地圖插圖 */}
                  <img
                    src="/images/map-illustration.jpg"
                    alt="臺東縣公廁地圖與環境熱點"
                    className="w-full h-full object-contain"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default InstructorsSection;
