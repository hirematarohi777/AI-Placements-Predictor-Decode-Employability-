import { NavLink } from "react-router-dom";
import { cn } from "@/lib/utils";
import {
  LayoutDashboard,
  FileText,
  Route,
  Briefcase,
  TrendingUp,
  Users,
  BarChart3,
  FileSpreadsheet,
} from "lucide-react";
import { useAuth } from "@/contexts/AuthContext";

const Sidebar = () => {
  const { user } = useAuth();

  const studentLinks = [
    { to: "/student/dashboard", label: "Dashboard", icon: LayoutDashboard },
    { to: "/student/assessments", label: "Assessments", icon: FileText },
    { to: "/student/learning-path", label: "Learning Path", icon: Route },
    { to: "/student/career", label: "Career", icon: Briefcase },
    { to: "/student/progress", label: "Progress", icon: TrendingUp },
  ];

  const professorLinks = [
    { to: "/professor/batch", label: "Batch Overview", icon: Users },
    { to: "/professor/analytics", label: "Student Analytics", icon: BarChart3 },
    { to: "/professor/reports", label: "Reports", icon: FileSpreadsheet },
  ];

  const links = user?.role === "student" ? studentLinks : professorLinks;

  return (
    <aside className="fixed left-0 top-16 h-[calc(100vh-4rem)] w-64 border-r bg-sidebar">
      <nav className="flex flex-col gap-1 p-4">
        {links.map((link) => (
          <NavLink
            key={link.to}
            to={link.to}
            className={({ isActive }) =>
              cn(
                "flex items-center gap-3 rounded-lg px-3 py-2 text-sidebar-foreground transition-colors hover:bg-sidebar-accent",
                isActive && "bg-sidebar-accent text-sidebar-accent-foreground"
              )
            }
          >
            <link.icon className="h-5 w-5" />
            <span>{link.label}</span>
          </NavLink>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;
