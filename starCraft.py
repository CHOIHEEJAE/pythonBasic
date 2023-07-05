from random import *

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
    
    seiez_mode = False;
        
    def set_sezie_mode(self):
        if Tank.seiez_mode == False:
            print("{0} : 시즈모드 On".format(self.name))
            self.damage *= 2
            self.seiez_mode = True
        else :
            print("{0} : 시즈모드 Off".format(self.name))
            self.damage /= 2
            self.seiez_mode = False
        
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False
        
    def clocking(self):
        if self.clocked == False:
            print('{0} : 클로킹모드 On'.format(self.name))
            self.clocked = False
        else:
            print('{0} : 클로킹모드 Off'.format(self.name))
            self.clocked = True

def game_start(): 
    print('[새로운 게임을 시작합니다]')

def game_over():
    print("Player : gg")
    print("Player  님이 게임에서 퇴장하였습니다.")


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

#유닛 일괄 관리

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동

for unit in attack_units:
    unit.move("1시")

print('Tank 시즈모드 개발 완료')

#공격준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로링)
for unit in attack_units:
    if isinstance(unit, Marine) : # 해당 unit이 Marine인지 확인
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_sezie_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
        
#전군 공격개시

for unit in attack_units:
    unit.attack("1시")

#피해발생
for unit in attack_units:
    unit.damaged(randint(5,20)) # 데미지 랜덤
    
    
# 전군 사망 -> 게임종료

game_over()



# # 건물
# class BuildingUnit(Unit) :
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, speed) - 기존 상속방법
#         super().__init__(name, hp, 0) # super로 상속받은 Unit 내 init 함수를 가져옴 , 다중상속 시 처리 불가
#         self.location = location