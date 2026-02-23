class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.__salary = salary
    def salary(self):
        return self.__salary
    def isalary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("too less") 
e_name = input("enter name --> ") 
e_salary = int(input("enter salaty --> "))
e = Employee(e_name, e_salary) 
print(f"{e.name} salary is {e.salary()}")
new_salary = int(input("enter new"))
e.isalary(new_salary)
print(f"{e.name} new salary is {e.salary()}")
