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