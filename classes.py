# classes are used to group similar functions and variables together

x= 3.2
class Enemy:
    life = 3

    def __init__(self, mp):
        self.mana = mp

    def get_mana(self):
        print(self.mana)

    def attack(self):
        if self.mana >= 2:
            print("-ve hp")
            self.life -= 1
            self.mana -= 2
        else:
            print("No mana, just like a CM!")

    def check_life(self):
        if self.life <= 0:
            print("Killed just like a CM")
        else:
            print(str(self.life) + ": current hp")


enemy1 = Enemy(5)
enemy2 = Enemy(6)

enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.check_life()
enemy2.check_life()
enemy2.attack()
enemy2.attack()
enemy2.attack()
enemy2.check_life()

