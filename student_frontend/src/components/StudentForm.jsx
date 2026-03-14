import { places, courses, categories } from "../data/mockData";

export default function StudentForm(){

  return(

    <div className="form">

      <h3>Add Student</h3>

      <input placeholder="Student ID" />
      <input placeholder="Name" />
      <input placeholder="Father Name" />
      <input type="date"/>

      <select>
        <option>Select Place</option>
        {places.map(p=>(
          <option key={p.id}>{p.name}</option>
        ))}
      </select>

      <select>
        <option>Select Course</option>
        {courses.map(c=>(
          <option key={c.id}>{c.name}</option>
        ))}
      </select>

      <select>
        <option>Select Category</option>
        {categories.map(c=>(
          <option key={c.id}>{c.name}</option>
        ))}
      </select>

      <button>Add Student</button>

    </div>

  )

}