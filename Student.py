class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name)
        self.email = email
        self.grades = grades if grades else {}
        self.courses = courses if courses else set()

    def __str__(self):
        return (
            f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, Email: {self.email}\n"
            f"Courses Enrolled: {', '.join(self.courses) if self.courses else 'None'}\n"
            f"Grades: {self.grades if self.grades else 'No grades recorded'}"
        )


class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id:
                return "Student with this ID already exists."
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student)
        return "Student added successfully."

    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id:
                if email:
                    student.email = email
                if grades:
                    student.grades.update(grades)
                if courses:
                    student.courses.update(courses)
                return "Student updated successfully."
        return "Student not found."

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.id_name[0] == student_id:
                del self.students[i]
                return "Student deleted successfully."
        return "Student not found."

    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.id_name[0] == student_id:
                student.courses.add(course)
                return f"Enrolled in course: {course}"
        return "Student not found."

    def search_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return str(student)
        return "Student not found."


if __name__ == "__main__":
    records = StudentRecords()
    print(records.add_student(1, "Alice", "alice@example.com"))
    print(records.add_student(2, "Bob", "bob@example.com", grades={"Math": 90}, courses={"Math", "English"}))
    print(records.add_student(1, "Alice", "alice@example.com"))
    print(records.update_student(2, email="bob.new@example.com", grades={"Science": 85}, courses={"Science"}))
    print(records.enroll_course(1, "History"))
    print("\nSearching for student with ID 1:")
    print(records.search_student(1))
    print("\nSearching for student with ID 2:")
    print(records.search_student(2))
    print("\n" + records.delete_student(2))
    print("\nSearching for student with ID 2 after deletion:")
    print(records.search_student(2))
