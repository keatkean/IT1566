import Hero as h
from Hero import *
import Hero


class CrystalMaiden(h.Hero):  # Inheritance 'Is-A' relationship e.g. CrystalMaiden is a Hero
    # class CrystalMaiden(Hero.Hero):
    # class CrystalMaiden(Hero):

    def __init__(self, name, attack_type, damage_type, attack, defense, ultimate_skill, health, mana):
        super().__init__(name, attack_type, damage_type, attack, defense, ultimate_skill, health, mana)
        # Hero.Hero.__init__(self, name, attack_type, damage_type, attack, defense, ultimate_skill, health, mana)
        self.__freezing_field = False

    def get_freezing_field(self):
        return self.__freezing_field

    def set_freezing_field(self, freezing_field):
        if isinstance(freezing_field, bool):
            self.__freezing_field = freezing_field
        else:
            print("Invalid Freezing Field!\n")

    def activate_freezing_field(self):
        if self.get_freezing_field():
            self.set_freezing_field(False)
            print("Freezing Field Deactivated!\n")
        else:
            self.set_freezing_field(True)
            print("Freezing Field Activated!\n")

    # Polymorphism - Method Overriding.
    # Override the parent class method __str__
    def __str__(self):
        return super().__str__() + "Freezing Field: " + str(self.get_freezing_field()) + "\n"
