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