import api from "../services/api";
import { useEffect, useState } from "react";

export default function ManagerDashboard() {
  const [pending, setPending] = useState([]);

  useEffect(() => {
    api.get("/manager/pending").then(r => setPending(r.data));
  }, []);

  return (
    <div>
      <h2>Manager Dashboard</h2>
      <pre>{JSON.stringify(pending, null, 2)}</pre>
    </div>
  );
}
