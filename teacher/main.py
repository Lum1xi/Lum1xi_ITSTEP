class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience
        self.students = []

    def add_student(self, student_name):
        self.students.append(student_name)

    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)

    def show_students(self):
        print(f"Студенти {self.name}: {', '.join(self.students) if self.students else 'Немає студентів'}")

    def info(self):
        return f"{self.name} - викладач {self.subject}, {self.experience} років стажу."

teacher = Teacher("Іван Петрович", "Математика", 15)
teacher.add_student("Олександр")
teacher.add_student("Марія")
teacher.show_students()
print(teacher.info())
