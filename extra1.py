class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def name(self):
        return  self.__name
    @property
    def age(self):
        return self.__age
    @name.setter
    def name(self, value):
        if not value:
            print("Empty")
        else:
            self.__name = value
    @age.setter
    def age (self, value):
        if 0 <= value <= 120:
             self.__age = value
        else:
            print("Too much or to less")

s1_name = input("Enter name --> ")
while True:
    s1_age = int(input("Enter age --> "))
    if 0 <= s1_age <= 120:
        break
    print("Too much or too less. Дубора ворид кунед.") 
s1 = Student(s1_name, s1_age)
print(s1.name)
print(s1.age)
