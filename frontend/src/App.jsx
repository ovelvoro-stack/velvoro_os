import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import EmployeeDashboard from "./pages/EmployeeDashboard";
import ManagerDashboard from "./pages/ManagerDashboard";
import AdminDashboard from "./pages/AdminDashboard";
import Billing from "./pages/Billing";
import ProtectedRoute from "./routes/ProtectedRoute";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />

        <Route element={<ProtectedRoute role="employee" />}>
          <Route path="/employee" element={<EmployeeDashboard />} />
        </Route>

        <Route element={<ProtectedRoute role="manager" />}>
          <Route path="/manager" element={<ManagerDashboard />} />
        </Route>

        <Route element={<ProtectedRoute role="admin" />}>
          <Route path="/admin" element={<AdminDashboard />} />
          <Route path="/billing" element={<Billing />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
