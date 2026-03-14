import api from "../api/api";

export const getStudents = () => api.get("/api/students/");

export const createStudent = (data) => api.post("/api/students/", data);

export const updateStudent = (id, data) =>
  api.put(`/api/students/${id}`, data);

export const deleteStudent = (id) =>
  api.delete(`/api/students/${id}`);

export const getPlaces = () =>
  api.get("/api/masters/places/");

export const getCourses = () =>
  api.get("/api/masters/courses/");

export const getCategories = () =>
  api.get("/api/masters/categories/");