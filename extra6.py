class Classroom:
    def __init__(self ):
        self.students = []
    def add_people(self, name):
        self.students.append(name)
        print(f"{name} ilova wud")
    def remove_students(self, name):
        if name in self.students:
            self.students.remove(name)
            print(f"{name} ud karda wud")
        else:
            print(f"{name} not found")
    def show_students(self):
        if not self.students:
            print("empty")
        else:
            print("xonandagon :")
            for student in self.students:
                print(student)
c1 = Classroom()
c1.add_people("romin")
c1.add_people("ali")
c1.show_students()
c1.remove_students("ali")   
c1.show_students()     
        
        