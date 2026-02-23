class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def work(self):
        print("employee is working")
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def work(self):
        print("is working")
class Develper(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def work(self):
        print("is working")
m1_name = input('enter man name --> ')
m1_salary = int(input("enter man salary --> "))
d1_name = input('enter dev name --> ')
d1_salary = int(input("enter dev salary --> "))
m = Manager(m1_name, m1_salary)
d = Develper(d1_name, d1_salary)
m.work()
d.work()


        