import { Navigate, Outlet } from "react-router-dom";
import { getUser } from "../services/auth";

export default function ProtectedRoute({ role }) {
  const user = getUser();
  if (!user) return <Navigate to="/login" />;
  if (role && user.role !== role) return <Navigate to="/login" />;
  return <Outlet />;
}
