// src/pages/Signup.jsx
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import API from "../api";

export default function Signup() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
    confirm_password: "",
  });
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
    
    if (form.password !== form.confirm_password) {
      alert("Passwords do not match");
      return;
    }

    try {
      const res = await API.post("/api/auth/signup", form);
      // Save the token returned from backend
      localStorage.setItem("token", res.data.access_token);
      
      alert("Signup successful! Welcome to the dashboard.");
      navigate("/dashboard");
    } catch (err) {
      alert(err.response?.data?.detail || "Error");
    }
  };

  return (
    <div className="auth-container">
      <div className="bg-shape shape-1"></div>
      <div className="bg-shape shape-2"></div>

      <div className="glass-panel">
        <div className="auth-header">
          <h2>Create Account</h2>
          <p>Join DealAgent today</p>
        </div>

        <form onSubmit={handleSignup} style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          <div className="input-group">
            <input
              type="text"
              className="input-field"
              placeholder="Full Name"
              required
              onChange={(e) =>
                setForm({ ...form, name: e.target.value })
              }
            />
          </div>

          <div className="input-group">
            <input
              type="email"
              className="input-field"
              placeholder="Email Address"
              required
              onChange={(e) =>
                setForm({ ...form, email: e.target.value })
              }
            />
          </div>

          <div className="input-group">
            <input
              type="password"
              className="input-field"
              placeholder="Password"
              required
              onChange={(e) =>
                setForm({ ...form, password: e.target.value })
              }
            />
          </div>

          <div className="input-group">
            <input
              type="password"
              className="input-field"
              placeholder="Confirm Password"
              required
              onChange={(e) =>
                setForm({ ...form, confirm_password: e.target.value })
              }
            />
          </div>

          <button type="submit" className="btn btn-primary">Sign Up</button>
        </form>

        <div className="auth-link">
          Already have an account? <Link to="/">Log in</Link>
        </div>
      </div>
    </div>
  );
}