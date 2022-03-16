
class ForceType:
    health = 17000
    attack = 900
    defence = 1100

class MagicType:
    health = 13000
    attack = 1300
    defence = 800

class SpiritType:
    health = 13000
    attack = 700
    defence = 1400

class ForceHero(ForceType):

    def __init__(self, equipment, money):

        self.health += equipment.equipment_health
        self.attack += equipment.equipment_attack
        self.defence += equipment.equipment_defence
        self.damage = int(self.health / 17)
        self.money = money

    def update_damage(self):
        self.damage = int(self.health / 17)

    def buy_equipment(self, equipment):
        if self.money >= equipment.equipment_cost:
            self.money -= equipment.equipment_cost
            self.health += equipment.equipment_health
            self.attack += equipment.equipment_attack
            self.defence += equipment. equipment_defence
            self.update_damage()
        else:
            print("Not enough money")

    def get_damage(self, damage):
        self.health -= (damage * 1.3 - self.defence * 0.3)

    def print_stats(self):
        print("health = ", self.health, " \t attack = ", self.attack,
              " \t defence = ", self.defence, " \t damage = ",
              self.damage, " \t current_money = ", self.money)


class MagicHero(MagicType):

    def __init__(self, equipment, money):

        self.health += equipment.equipment_health
        self.attack += equipment.equipment_attack
        self.defence += equipment.equipment_defence
        self.damage = int(self.attack)
        self.money = money

    def update_damage(self):
        self.damage = int(self.attack)

    def buy_equipment(self, equipment):
        if self.money >= equipment.equipment_cost:
            self.money -= equipment.equipment_cost
            self.health += equipment.equipment_health
            self.attack += equipment.equipment_attack
            self.defence += equipment.equipment_defence
            self.update_damage()
        else:
            print("Not enough money")

    def get_damage(self, damage):
        self.health -= (damage * 1.3 - self.defence * 0.3)

    def print_stats(self):
        print("health = ", self.health, " \t attack = ", self.attack,
              " \t defence = ", self.defence, " \t damage = ",
              self.damage, " \t current_money = ", self.money)
class SpiritHero(SpiritType):

    def __init__(self, equipment, money):

        self.health += equipment.equipment_health
        self.attack += equipment.equipment_attack
        self.defence += equipment.equipment_defence
        self.damage = int(self.defence)
        self.money = money

    def update_damage(self):
        self.damage = int(self.defence)

    def buy_equipment(self, equipment):
        if self.money >= equipment.equipment_cost:
            self.money -= equipment.equipment_cost
            self.health += equipment.equipment_health
            self.attack += equipment.equipment_attack
            self.defence += equipment.equipment_defence
            self.update_damage()
        else:
            print("Not enough money")

    def get_damage(self, damage):
        self.health -= (damage * 1.3 - self.defence * 0.3)

    def print_stats(self):
        print("health = ", self.health, " \t attack = ", self.attack,
              " \t defence = ", self.defence, " \t damage = ",
              self.damage, " \t current_money = ", self.money)


class Equipment:
    def __init__(self, health, attack, defence, cost):
        self.equipment_health = health
        self.equipment_attack = attack
        self.equipment_defence = defence
        self.equipment_cost = cost

class Ring(Equipment):
    def use_extra_health(self, hero):
        hero.health = int(hero.health * 1.2)
        hero.update_damage()

class Necklace(Equipment):
    def use_extra_defence(self, hero):
        hero.defence = int(hero.defence * 1.6)
        hero.update_damage()

class Banner(Equipment):
    def use_extra_attack(self, hero):
        hero.attack = int(hero.attack * 2.2)
        hero.update_damage()


# изначально все герои раздетые, поэтому сделаем экипировку с 0 параметрами
poor = Equipment(0, 0, 0, 0)
weapon_one = Equipment(1861, 228, 166, 800)
weapon_two = Equipment(2332, 197, 201, 950)
helmet_one = Equipment(2880, 140, 214, 600)
shield_two = Equipment(1940, 166, 322, 760)
ring_one = Ring(1500, 140, 115, 1100)
banner_two = Banner(1760, 124, 193, 1020)

# создадим 2 раздетых героев c 2 косарями в кармане и выведем их статы в консоль
Mountain_King = ForceHero(poor, 2000)
print("Статы голого горного короля: ")
Mountain_King.print_stats()
Ninja = MagicHero(poor, 2000)
print("Статы голого ниндзи: ")
Ninja.print_stats()

#закупимся чутка и выведем статы
Mountain_King.buy_equipment(weapon_one)
print("статы горного после покупки weapon_one: ")
Mountain_King.print_stats()
# и еще закупимся
Mountain_King.buy_equipment(ring_one)
print("статы горного после покупки ring_one: ")
Mountain_King.print_stats()
#ударим голым ниндзей по одетому горному королю и выведем статы
Mountain_King.get_damage(Ninja.damage)
print("статы горного короля после удара ниндзи: ")
Mountain_King.print_stats()
print("статы горного короля после использования абилки кольца: ")
ring_one.use_extra_health(Mountain_King)
Mountain_King.print_stats()
