import { useState } from "react";
import { X, Check, Loader2 } from "lucide-react";
import { registrationAPI } from "@/lib/api";
import { useToast } from "@/hooks/use-toast";

interface Course {
  id: number;
  title: string;
  date: string;
  time: string;
  location: string;
}

interface RegistrationModalProps {
  isOpen: boolean;
  onClose: () => void;
  course: Course | null;
}

const RegistrationModal = ({ isOpen, onClose, course }: RegistrationModalProps) => {
  const [formData, setFormData] = useState({
    name: "",
    phone: "",
    email: "",
    participants: "1",
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);
  const { toast } = useToast();

  if (!isOpen || !course) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);

    try {
      // 呼叫 API 建立報名
      await registrationAPI.create({
        course_id: course.id,
        name: formData.name,
        email: formData.email,
        phone: formData.phone,
        participants: parseInt(formData.participants),
      });

      setIsSuccess(true);
      
      // 顯示成功訊息
      toast({
        title: "報名成功！",
        description: "我們會盡快寄送確認信到您的信箱",
      });

      // 重置表單並關閉
      setTimeout(() => {
        setIsSuccess(false);
        setFormData({ name: "", phone: "", email: "", participants: "1" });
        onClose();
      }, 2000);
    } catch (error: any) {
      toast({
        variant: "destructive",
        title: "報名失敗",
        description: error.message || "請稍後再試",
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-foreground/50 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Modal */}
      <div className="relative bg-card rounded-2xl shadow-card w-full max-w-md p-6 animate-scale-in">
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-2 text-muted-foreground hover:text-foreground transition-colors"
          aria-label="關閉"
        >
          <X className="w-5 h-5" />
        </button>

        {isSuccess ? (
          <div className="text-center py-8">
            <div className="w-16 h-16 rounded-full bg-primary/20 flex items-center justify-center mx-auto mb-4">
              <Check className="w-8 h-8 text-primary" />
            </div>
            <h3 className="text-xl font-semibold text-foreground mb-2">
              報名成功！
            </h3>
            <p className="text-muted-foreground">
              我們會盡快寄送確認信到您的信箱
            </p>
          </div>
        ) : (
          <>
            <h3 className="text-xl font-semibold text-foreground mb-2">
              課程報名
            </h3>
            <p className="text-muted-foreground text-sm mb-6">
              {course.title} - {course.date}
            </p>

            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label htmlFor="name" className="block text-sm font-medium text-foreground mb-1">
                  姓名 *
                </label>
                <input
                  type="text"
                  id="name"
                  name="name"
                  required
                  value={formData.name}
                  onChange={handleChange}
                  className="w-full px-4 py-3 rounded-lg border border-input bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-primary/50 transition-shadow"
                  placeholder="請輸入您的姓名"
                />
              </div>

              <div>
                <label htmlFor="phone" className="block text-sm font-medium text-foreground mb-1">
                  聯絡電話 *
                </label>
                <input
                  type="tel"
                  id="phone"
                  name="phone"
                  required
                  value={formData.phone}
                  onChange={handleChange}
                  className="w-full px-4 py-3 rounded-lg border border-input bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-primary/50 transition-shadow"
                  placeholder="09XX-XXX-XXX"
                />
              </div>

              <div>
                <label htmlFor="email" className="block text-sm font-medium text-foreground mb-1">
                  電子信箱 *
                </label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  required
                  value={formData.email}
                  onChange={handleChange}
                  className="w-full px-4 py-3 rounded-lg border border-input bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-primary/50 transition-shadow"
                  placeholder="example@email.com"
                />
              </div>

              <div>
                <label htmlFor="participants" className="block text-sm font-medium text-foreground mb-1">
                  報名人數
                </label>
                <select
                  id="participants"
                  name="participants"
                  value={formData.participants}
                  onChange={handleChange}
                  className="w-full px-4 py-3 rounded-lg border border-input bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-primary/50 transition-shadow"
                >
                  {[1, 2, 3, 4, 5].map((num) => (
                    <option key={num} value={num}>
                      {num} 人
                    </option>
                  ))}
                </select>
              </div>

              <button
                type="submit"
                disabled={isSubmitting}
                className="btn-nature w-full mt-6 disabled:opacity-70 disabled:cursor-not-allowed"
              >
                {isSubmitting ? (
                  <>
                    <Loader2 className="w-5 h-5 animate-spin mr-2" />
                    送出中...
                  </>
                ) : (
                  "確認報名"
                )}
              </button>
            </form>
          </>
        )}
      </div>
    </div>
  );
};

export default RegistrationModal;
