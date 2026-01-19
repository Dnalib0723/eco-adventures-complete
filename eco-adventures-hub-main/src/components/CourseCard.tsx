import { Calendar, MapPin, Users, Clock } from "lucide-react";

interface CourseCardProps {
  image: string;
  title: string;
  description: string;
  date: string;
  time: string;
  location: string;
  spots: number;
  category: string;
  onRegister: () => void;
}

const CourseCard = ({
  image,
  title,
  description,
  date,
  time,
  location,
  spots,
  category,
  onRegister,
}: CourseCardProps) => {
  return (
    <div className="nature-card overflow-hidden group">
      {/* Image */}
      <div className="relative h-48 overflow-hidden">
        <img
          src={image}
          alt={title}
          className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
        />
        <div className="absolute top-4 left-4">
          <span className="px-3 py-1 rounded-full text-sm font-medium bg-primary text-primary-foreground">
            {category}
          </span>
        </div>
      </div>

      {/* Content */}
      <div className="p-6">
        <h3 className="text-xl font-semibold text-foreground mb-2 group-hover:text-primary transition-colors">
          {title}
        </h3>
        <p className="text-muted-foreground text-sm mb-4 line-clamp-2">
          {description}
        </p>

        {/* Info Grid */}
        <div className="grid grid-cols-2 gap-3 mb-4 text-sm">
          <div className="flex items-center gap-2 text-muted-foreground">
            <Calendar className="w-4 h-4 text-primary" />
            <span>{date}</span>
          </div>
          <div className="flex items-center gap-2 text-muted-foreground">
            <Clock className="w-4 h-4 text-primary" />
            <span>{time}</span>
          </div>
          <div className="flex items-center gap-2 text-muted-foreground">
            <MapPin className="w-4 h-4 text-primary" />
            <span>{location}</span>
          </div>
          <div className="flex items-center gap-2 text-muted-foreground">
            <Users className="w-4 h-4 text-primary" />
            <span>剩餘 {spots} 名</span>
          </div>
        </div>

        <button onClick={onRegister} className="btn-nature w-full">
          立即報名
        </button>
      </div>
    </div>
  );
};

export default CourseCard;
