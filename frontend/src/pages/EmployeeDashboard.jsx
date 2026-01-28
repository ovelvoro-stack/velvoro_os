import api from "../services/api";
import { useEffect, useState } from "react";

export default function EmployeeDashboard() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    api.get("/daily-summary").then(r => setTasks(r.data));
  }, []);

  return (
    <div>
      <h2>Employee Dashboard</h2>
      <pre>{JSON.stringify(tasks, null, 2)}</pre>
    </div>
  );
}
