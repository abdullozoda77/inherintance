class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("animal sounds")
class Dog(Animal):
    def speak(self):
        return "woof"
class Cat(Animal):
    def speak(self):
        return "hav"
    
d1 = input("enter dog name --> ")
c1 = input("enter cat name --> ")
d = Dog(d1)
c = Cat(c1)
print(d.speak())
print(c.speak())
        