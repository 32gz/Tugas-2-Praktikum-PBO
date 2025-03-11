import random

class Robot:
    def __init__(self, name, hp, attack_power, defense_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack_enemy(self, enemy):
        if random.random() < 0.8:  
            damage = max(0, self.attack_power - enemy.defense_power)
            enemy.hp -= damage
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
        else:
            print(f"{self.name} gagal menyerang {enemy.name}!")

    def is_defeated(self):
        return self.hp <= 0

    def __str__(self):
        return f"{self.name} [HP: {self.hp}, ATK: {self.attack_power}, DEF: {self.defense_power}]"

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def start(self):
        while not self.robot1.is_defeated() and not self.robot2.is_defeated():
            print(f"\nRound-{self.round} ==================================================")
            print(self.robot1)
            print(self.robot2)
            
            action1 = self.get_action(self.robot1)
            action2 = self.get_action(self.robot2)

            if action1 == "attack":
                self.robot1.attack_enemy(self.robot2)
            if action2 == "attack":
                self.robot2.attack_enemy(self.robot1)

            if self.robot1.is_defeated():
                print(f"{self.robot2.name} menang!")
                break
            if self.robot2.is_defeated():
                print(f"{self.robot1.name} menang!")
                break

            self.round += 1
    
    def get_action(self, robot):
        print(f"\n1. Attack     2. Defense     3. Giveup")
        choice = input(f"{robot.name}, pilih aksi: ")
        if choice == "1":
            return "attack"
        elif choice == "3":
            print(f"{robot.name} menyerah!")
            robot.hp = 0
            return "giveup"
        return "defense"


robot1 = Robot("Vortex", 250, 30, 5)
robot2 = Robot("Aegis", 350, 50, 3)


game = Game(robot1, robot2)
game.start()
