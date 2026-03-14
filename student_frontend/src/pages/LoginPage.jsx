import { useState } from "react";
import API from "../api/api";
import SignupPage from "./SignupPage";
export default function LoginPage({ setPage }) {

  const [form,setForm] = useState({
    email: "",
    password: ""
  }) ;
  const handleChange = (e) =>{

    setForm({
      ...form,
      [e.target.name] : e.target.value
    });

  };

  const handleLogin = async (e) => {
    e.preventDefault();

    try{
      const res = await API.post("/auth/login",form);
      alert(res.data.message);
      setPage("students");

    } catch{
      alert("Invalid credentials");
    }
  };

  return (

    <div className="login">

      <h2>Login</h2>

      <form onSubmit={handleLogin}>

        <input
          placeholder="Username"
          onChange={handleChange}
        />

        <input
          type="password"
          placeholder="Password"
          onChange={handleChange}
        />

        <button type="submit">Login</button>

      </form>

      <p>
        Don't have an account?{" "}
        <span onClick={SignupPage } className="link">
          Sign Up
        </span>
      </p>

    </div>
  );
}