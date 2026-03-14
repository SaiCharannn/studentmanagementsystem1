import { students } from "../data/mockData";

export default function StudentTable(){
  return(
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Course</th>
          <th>Place</th>
          <th>Category</th>
        </tr>
      </thead>

      <tbody>

        {students.map(s =>(
          <tr key={s.id}>
            <td>{s.student_id}</td>
            <td>{s.name}</td>
            <td>{s.course}</td>
            <td>{s.place}</td>
            <td>{s.category}</td>
          </tr>
        ))}

      </tbody>
    </table>
  );
}