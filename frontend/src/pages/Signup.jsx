// src/pages/Signup.jsx
import { useState } from "react";
import API from "../api";

export default function Signup() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
    confirm_password: "",
  });

  const handleSignup = async (e) => {
    e.preventDefault();
    
    if (form.password !== form.confirm_password) {
      alert("Passwords do not match");
      return;
    }

    try {
      await API.post("/api/auth/signup", form);
      alert("Signup successful");
    } catch (err) {
      alert(err.response?.data?.detail || "Error");
    }
  };

  return (
    <form onSubmit={handleSignup}>
      <h2>Signup</h2>

      <input
        type="text"
        placeholder="Name"
        required
        onChange={(e) =>
          setForm({ ...form, name: e.target.value })
        }
      />

      <input
        type="email"
        placeholder="Email"
        required
        onChange={(e) =>
          setForm({ ...form, email: e.target.value })
        }
      />

      <input
        type="password"
        placeholder="Password"
        required
        onChange={(e) =>
          setForm({ ...form, password: e.target.value })
        }
      />

      <input
        type="password"
        placeholder="Confirm Password"
        required
        onChange={(e) =>
          setForm({ ...form, confirm_password: e.target.value })
        }
      />

      <button type="submit">Signup</button>
    </form>
  );
}