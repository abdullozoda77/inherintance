class Animal:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @name.setter
    def name(self, value):
        if not value:
            print("empty")
        else:
            self.__name = value
    @age.setter
    def age (self, value):
        if 0 <= value <= 50:
            self.__age = value
        else:
            print("to mich or less")
    def make_sound(self):
        print("some genetic sound")
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print("woof, woof")
    def fetch(self):
        print(self.name , "is fetchind")

anim = input("enter animal --> ")
anim_age = int(input("enter age --> "))
an1 = Animal(anim, anim_age)
an1.make_sound()
d_name = input("enter dog name --> ")
d_age = int(input("enter age --> "))
dog = Dog(d_name, d_age)
dog.make_sound()
dog.fetch()