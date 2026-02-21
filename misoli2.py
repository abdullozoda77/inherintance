class Person:
    def __init__(self,name):
        self.name = name
    def info(self):
        print(f"Name --> {self.name}")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
        
    def info(self):
        super().info()
        print(f"Name --> {self.grade}")

student_name = input("Enter name -->")
student_grade = int(input("Enter grade --> "))
student1 = Student(student_name, student_grade)

student1.info()

        