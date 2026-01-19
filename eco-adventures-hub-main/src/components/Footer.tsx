import { Leaf, Heart } from "lucide-react";

const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-secondary py-8 border-t border-border">
      <div className="container-nature px-4">
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          {/* Logo */}
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center">
              <Leaf className="w-4 h-4 text-primary-foreground" />
            </div>
            <span className="font-semibold text-foreground">
              新竹縣環境教育網
            </span>
          </div>

          {/* Copyright */}
          <p className="text-muted-foreground text-sm flex items-center gap-1">
            © {currentYear} 新竹縣環境教育網 - 用
            <Heart className="w-4 h-4 text-destructive inline" />
            守護地球
          </p>

          {/* Links */}
          <div className="flex items-center gap-6 text-sm">
            <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
              隱私政策
            </a>
            <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
              使用條款
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
