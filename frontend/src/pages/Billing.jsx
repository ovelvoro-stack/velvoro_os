import api from "../services/api";

export default function Billing() {
  async function pay() {
    await api.post("/billing/pay");
  }
  return (
    <div>
      <h2>Billing</h2>
      <button onClick={pay}>Upgrade Plan</button>
    </div>
  );
}
