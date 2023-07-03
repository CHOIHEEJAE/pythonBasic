# 일반유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{0} 유닛이 생성되었습니다.'.format(name))
        
    def move(self, location):
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed)) 

        # self.damage = damage
        # print("{0} 유닛이 생성되었습니다.".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격유닛
class AttackUnit (Unit) : # Unit class 상속
    def __init__(self, name, hp, speed, damage):
        # self.name = name
        # self.hp = hp
        Unit.__init__(self, name, hp, speed) # 상속받은 class 사용
        self.damage = damage
        
    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name, location, self.damage))

# 마린
class Marine (AttackUnit) :
    def __init__(self):
        AttackUnit.__init__(self, "마린", 50, 1, 5)

    # 특수기능 (스팀팩)
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print('{0} 스팀팩을 사용합니다.'.format(self.name))
        else :
            print("{0} 체력이 부족하여 스팀팩을 사용할 수 없습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        

# 날 수 있는 기능 class
class Flyable :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed
        
    def fly(self, name, location) :
        print('{0} : {1} 방향으로 날아갑니다. [속도 : {2}]'.format(name, location, self.flying_speed))
        
# 공중 공격 유닛 (공격유닛 + 날 수 있는 기능) - 다중상속
class FlyableAttackUnit (AttackUnit, Flyable) :
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
        
    def move(self, location) :
        self.fly(self.name, location)

# # 건물
# class BuildingUnit(Unit) :
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, speed) - 기존 상속방법
#         super().__init__(name, hp, 0) # super로 상속받은 Unit 내 init 함수를 가져옴 , 다중상속 시 처리 불가
#         self.location = location