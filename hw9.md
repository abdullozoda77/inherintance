class Transport:
    def __init__(self, speed, brand):
        self.brand = brand
        self.speed = speed
    def move(self):
        print("Transport is moving")
class Car(Transport):
    def move(self):
        print("Car is driving")
class Plane(Transport):
    def move(self):
        print("Plane is driving")

car_brand = input("Car brand: ")
car_speed = int(input("Car speed: "))
plane_brand = input("Plane brand: ")
plane_speed = int(input("Plane speed: "))
car1 = Car(car_speed, car_brand)
plane1 = Plane(plane_speed, plane_brand)
car1.move()
plane1.move()

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

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def work(self):
        print("Employee works")
class Developer(Employee):
    def work(self):
        print("Writes code")
class Manager(Employee):
        def work(self):
             print("Manages team")
dev1_name = input("Enter dev1 name --> ")
dev1_salary = int(input("Enter dev1 salary -->"))
manager1_name = input("Enter manager1 name --> ")
manager1_salary = int(input("Enter manager1 salary --> "))
dev1 = Developer(dev1_name, dev1_salary)
manager1 = Manager(manager1_name, manager1_salary)
dev1.work()
manager1.work()

class Character:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
    def attack(self):
        print("Basic attack")
class Warrior (Character):
    def __init__(self, name, health=100):
        super().__init__(name, health)
    def attack(self):
        print("Sword attack")
class Mage (Character):
    def __init__(self, name, health=100):
        super().__init__(name, health)
    def attack(self):
        print("Magic attack")
warrior1 = Warrior(input("Enter war1 name --> "))
mage1 = Mage(input("Enter mage1 name --> "))
warrior1.attack()
mage1.attack()
        
class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Sound of animal")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
          super().sound()    
          print("Bark")
dog1_name = input("Enter dogs name --> ")
dog1 = Dog(dog1_name)
dog1.sound()    