class Character:
    def attack(self):
        pass


class Warrior(Character):
    def attack(self):
        print("Sword attack")


class Archer(Character):
    def attack(self):
        print("Arrow attack")


chars = [Warrior(), Archer()]

for c in chars:
    c.attack()
