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