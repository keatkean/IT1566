import Hero as h
from Hero import *
import Hero


# class DragonKnight(h.Hero):
# class DragonKnight(Hero):
class DragonKnight(Hero.Hero):  # Inheritance 'Is-A' relationship e.g. DragonKnight is a Hero

    # Constructor/Initializer
    def __init__(self, name, attack_type, damage_type, attack, defense, ultimate_skill, health, mana):
        # Call the parent class constructor
        super().__init__(name, attack_type, damage_type, attack, defense, ultimate_skill, health, mana)
        # Hero.Hero.__init__(self, name, attack_type, damage_type, attack, defense, ultimate_skill, health, mana)

        # Initialize the Dragon Knight's attributes
        self.__dragon_form = False

    # Getters/Accessor Methods
    def get_dragon_form(self):
        return self.__dragon_form

    # Setters/Mutator Methods
    def set_dragon_form(self, dragon_form):
        if isinstance(dragon_form, bool):
            self.__dragon_form = dragon_form
        else:
            print("Invalid dragon form!\n")

    # Other Methods
    def dragon_blood(self):
        if self.get_dragon_form():
            self.set_health(self.get_health() + 100)
            self.set_mana(self.get_mana() + 100)
            print("Dragon Blood Activated!\n")
        else:
            print("Dragon Blood cannot be activated while not in dragon form!\n")

    def dragon_kick(self):
        if self.get_dragon_form():
            print("Dragon Kick Activated!\n")
        else:
            print("Dragon Kick cannot be activated while not in dragon form!\n")

    def dragon_tail(self):
        if self.get_dragon_form():
            print("Dragon Tail Activated!\n")
        else:
            print("Dragon Tail cannot be activated while not in dragon form!\n")

    def dragon_form(self):
        if self.get_dragon_form():
            self.set_dragon_form(False)
            print("Dragon Form Deactivated!\n")
        else:
            self.set_dragon_form(True)
            print("Dragon Form Activated!\n")

    def ultimate(self):
        if self.get_dragon_form():
            print("Ultimate Activated!\n")
        else:
            print("Ultimate cannot be activated while not in dragon form!\n")

    # Polymorphism - Method Overriding.
    # Override the parent class method print_hero_info()
    def print_hero_info(self):
        print("Name: " + self.get_name())
        print("Attack Type: " + self.get_attack_type())
        print("Damage Type: " + self.get_damage_type())
        print("Attack: " + str(self.get_attack()))
        print("Defense: " + str(self.get_defense()))
        print("Health: " + str(self.get_health()))
        print("Mana: " + str(self.get_mana()))
        print("Ultimate Skill: " + self.get_ultimate_skill())
        print("Dragon Form: " + str(self.get_dragon_form()) + "\n")
