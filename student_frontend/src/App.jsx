import { useState } from "react";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";
import StudentsPage from "./pages/StudentsPage";


function App(){

  const [page, setPage] = useState("login");

  if(page === "login"){
    return <LoginPage setPage={setPage} />;
  }

  if(page === "signup"){
    return <SignupPage setPage={setPage} />;
  }

  if(page === "students"){
    return <StudentsPage />;
  }

}

export default App;