// src/pages/Signup.jsx
import { useState } from "react";
import axios from "axios";

export default function Signup() {
  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  const handleSignup = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://127.0.0.1:8000/api/auth/signup", form);
      alert("Signup successful");
    } catch (err) {
      alert(err.response?.data?.detail || "Error");
    }
  };

  return (
    <form onSubmit={handleSignup}>
      <h2>Signup</h2>

      <input
        type="email"
        placeholder="Email"
        onChange={(e) =>
          setForm({ ...form, email: e.target.value })
        }
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) =>
          setForm({ ...form, password: e.target.value })
        }
      />

      <button type="submit">Signup</button>
    </form>
  );
}