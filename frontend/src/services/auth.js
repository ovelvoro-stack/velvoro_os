export function saveSession(data) {
  localStorage.setItem("velvoro_session", JSON.stringify(data));
}

export function getUser() {
  const s = localStorage.getItem("velvoro_session");
  return s ? JSON.parse(s) : null;
}

export function logout() {
  localStorage.removeItem("velvoro_session");
  window.location.href = "/login";
}
