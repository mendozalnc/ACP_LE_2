class Student:

    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        
        self.id_name = (student_id, student_name)
        self.email = email
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else set()
    
    def __str__(self):
        return (f"Student ID: {self.id_name}\n"
                f"Email: {self.email}\n"
                f"Grades: {self.grades}\n"
                f"Courses: {self.courses}\n")
