import { Bell } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";

const NotificationBell = () => {
  const notifications = [
    { id: 1, text: "New assessment available", time: "2 mins ago" },
    { id: 2, text: "Skill progress updated", time: "1 hour ago" },
    { id: 3, text: "Career insight ready", time: "3 hours ago" },
  ];

  return (
    <Popover>
      <PopoverTrigger asChild>
        <Button variant="ghost" size="icon" className="relative">
          <Bell className="h-5 w-5" />
          {notifications.length > 0 && (
            <span className="absolute -top-1 -right-1 h-4 w-4 rounded-full bg-destructive text-[10px] text-destructive-foreground flex items-center justify-center">
              {notifications.length}
            </span>
          )}
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-80">
        <div className="space-y-2">
          <h4 className="font-semibold text-sm">Notifications</h4>
          {notifications.map((notification) => (
            <div
              key={notification.id}
              className="p-2 rounded-md hover:bg-muted cursor-pointer transition-colors"
            >
              <p className="text-sm">{notification.text}</p>
              <p className="text-xs text-muted-foreground">{notification.time}</p>
            </div>
          ))}
        </div>
      </PopoverContent>
    </Popover>
  );
};

export default NotificationBell;
