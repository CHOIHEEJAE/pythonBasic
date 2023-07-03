# 일반유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, location):
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))

        # self.damage = damage
        # print("{0} 유닛이 생성되었습니다.".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 공격유닛
class AttackUnit (Unit) : # Unit class 상속
    def __init__(self, name, hp, damage):
        # self.name = name
        # self.hp = hp
        Unit.__init__(self, name, hp) # 상속받은 class 사용
        self.damage = damage
        
    def attack(self, location) : 
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 의 데미지를 입었습니다.".format(self.name, self.damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능 class
class Flyable :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed
        
    def fly(self, name, location) :
        print('{0} : {1} 방향으로 날아갑니다. [속도 : {2}]'.format(name, location, self.flying_speed))
        
# 공중 공격 유닛 (공격유닛 + 날 수 있는 기능) - 다중상속
class FlyableAttackUnit (AttackUnit, Flyable) :
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

