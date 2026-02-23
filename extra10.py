class Device:
    def power_on(self):
        print("device is on")
class Phone(Device):
    def call (self, number):
        print(f"calling - {number} ")
class Camera(Device):
    def take_photo(self):
        print("photo taken")
class Smartphone(Phone, Camera):
    pass
sp = Smartphone()
number = int(input())
sp.power_on()
sp.call(number)
sp.take_photo ()      