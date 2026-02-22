class Car:
    def __init__(self, brand , speed):
        self.brand = brand
        self.speed = speed
    @property
    def brand(self):
        return self.__brand
    @property
    def speed(self):
        return self.__speed
    @brand.setter
    def brand(self, value):
        if not value:
            print("Empty")
        else:
            self.__brand = value
    @speed.setter
    def speed(self ,value):
        if 0 <= value <= 300:
            self.__speed = value
        else:
            print("too much or too slow")
c1_brand = input("enter brand --> ")
while True:
    c1_speed = int(input("Enter speed --> "))
    if  0 <= c1_speed <= 300:
        break
    else:
        print("Too much or slow enter another --> ")
c1 = Car(c1_brand, c1_speed)
print(c1.brand)
print(c1.speed)
c1.speed = 350
print(c1.speed)
        