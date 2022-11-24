# 생성자 : 인스턴스를 만들 때 호출되는 메서드

class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed

    def decrease_health(self,num):
        self.health -=num

    def get_health(self):
        return self.health

# 고블린 인스턴스 생성
goblin = Monster(800,120,300)
goblin.decrease_health(100)
print(goblin.health)

# 늑대 인스턴스 생성
wolf = Monster(400,80,200)
wolf.decrease_health(40)
print(wolf.health)