import { useState } from "react";
import api from "../services/api";
import { saveSession } from "../services/auth";

export default function Login() {
  const [company, setCompany] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  async function submit() {
    const res = await api.post("/auth/login", {
      company_name: company,
      username,
      password
    });
    saveSession(res.data);
    window.location.href = `/${res.data.role}`;
  }

  return (
    <div>
      <h2>Velvoro Daily OS</h2>
      <input placeholder="Company" onChange={e => setCompany(e.target.value)} />
      <input placeholder="Username" onChange={e => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
      <button onClick={submit}>Login</button>
    </div>
  );
}
