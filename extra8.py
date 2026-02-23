class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    def move(self):
        print("vehicle is moving")
class Car(Vehicle):
    def move(self):
        print(f'car is moving {self.speed} km ')
class Bike(Vehicle):
    def move(self):
        print(f'Bike is moving {self.speed} km ')
c_speed = int(input("enter car speed --> "))
b_speed = int(input("enter bike speed --> "))
c = Car(c_speed)
b = Bike(b_speed)
c.move()
b.move()
        