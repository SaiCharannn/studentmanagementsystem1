import Sidebar from "../components/SideBar";
import Navbar from "../components/NavBar";
import StudentForm from "../components/StudentForm";
import StudentTable from "../components/StudentTable";

export default function StudentsPage(){

  return(

    <div className="dashboard">

      <Sidebar />

      <div className="main">

        <Navbar />

        <StudentForm />

        <StudentTable />

      </div>

    </div>

  );
}