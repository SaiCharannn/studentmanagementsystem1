import { useState } from "react";

export default function SignupPage({ setPage }) {

  const [user, setUser] = useState({
    name:"",
    email:"",
    password:""
  });

  const handleChange = (e)=>{
    setUser({
      ...user,
      [e.target.name]:e.target.value
    });
  };

  const handleSignup = (e)=>{
    e.preventDefault();

    if(user.name && user.email && user.password){
      alert("Signup successful (dummy)");
      setPage("login");
    }
  };

  return (

    <div className="login">

      <h2>Sign Up</h2>

      <form onSubmit={handleSignup}>

        <input
          name="name"
          placeholder="Full Name"
          onChange={handleChange}
        />

        <input
          name="email"
          placeholder="Email"
          onChange={handleChange}
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleChange}
        />

        <button>Create Account</button>

      </form>

      <p>
        Already have an account?{" "}
        <span onClick={()=>setPage("login")} className="link">
          Login
        </span>
      </p>

    </div>
  );
}