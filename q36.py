class Enemy:
    def attack(self):
        pass

class Zombie(Enemy):
    def attack(self):
        print("Zombie attack")

class Alien(Enemy):
    def attack(self):
        print("Alien attack")

for e in [Zombie(), Alien()]:
    e.attack()
