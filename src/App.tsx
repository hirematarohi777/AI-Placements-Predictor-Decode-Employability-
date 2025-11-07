import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import Login from "./pages/Auth/Login";
import Register from "./pages/Auth/Register";
import StudentLayout from "./layouts/StudentLayout";
import ProfessorLayout from "./layouts/ProfessorLayout";
import NotFound from "./pages/NotFound";

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <TooltipProvider>
      <Toaster />
      <Sonner />
      <BrowserRouter>
        <AuthProvider>
          <Routes>
            <Route path="/" element={<Navigate to="/login" replace />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/student/*" element={<StudentLayout />} />
            <Route path="/professor/*" element={<ProfessorLayout />} />
            <Route path="/dashboard" element={<Navigate to="/student/dashboard" replace />} />
            <Route path="/assessments" element={<Navigate to="/student/assessments" replace />} />
            <Route path="/quiz" element={<Navigate to="/student/quiz" replace />} />
            <Route path="/learning-path" element={<Navigate to="/student/learning-path" replace />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </TooltipProvider>
  </QueryClientProvider>
);

export default App;
