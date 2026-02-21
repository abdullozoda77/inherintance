class Character:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
    def attack(self):
        print("Basic attack")
class Warrior (Character):
    def __init__(self, name, health=100):
        super().__init__(name, health)
    def attack(self):
        print("Sword attack")
class Mage (Character):
    def __init__(self, name, health=100):
        super().__init__(name, health)
    def attack(self):
        print("Magic attack")
warrior1 = Warrior(input("Enter war1 name --> "))
mage1 = Mage(input("Enter mage1 name --> "))
warrior1.attack()
mage1.attack()
        