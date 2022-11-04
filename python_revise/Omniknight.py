import Hero as h
import Hero
from Hero import *


# class Omniknight(h.Hero):
# class Omniknight(Hero.Hero):
class Omniknight(Hero):  # Inheritance 'Is-A' relationship e.g. Omniknight is a Hero

    def __init__(self, name, attack_type, damage_type, attack, defense, ultimate_skill):
        super().__init__(name, attack_type, damage_type, attack, defense, ultimate_skill)
        # Hero.Hero.__init__(self, name, attack_type, damage_type, attack, defense, ultimate_skill)
        self.__guardian_angel = False

    def get_guardian_angel(self):
        return self.__guardian_angel

    def set_guardian_angel(self, guardian_angel):
        if isinstance(guardian_angel, bool):
            self.__guardian_angel = guardian_angel
        else:
            print("Invalid guardian angel!\n")

    def guardian_angel(self):
        if self.get_guardian_angel():
            self.set_guardian_angel(False)
            print("Guardian Angel Deactivated!\n")
        else:
            self.set_guardian_angel(True)
            print("Guardian Angel Activated!\n")

    def ultimate(self):
        if self.get_guardian_angel():
            print("Guardian Angel Activated!\n")
        else:
            print("Guardian Angel cannot be activated while not in guardian angel form!\n")

    def heal(self):
        if self.get_guardian_angel():
            print("Heal Activated!\n")
            super().heal()
            # Hero.heal(self)
        else:
            print("Heal cannot be activated while not in guardian angel form!\n")

    def repel(self):
        if self.get_guardian_angel():
            print("Repel Activated!\n")
        else:
            print("Repel cannot be activated while not in guardian angel form!\n")

    def purify(self):
        if self.get_guardian_angel():
            print("Purify Activated!\n")
        else:
            print("Purify cannot be activated while not in guardian angel form!\n")

    # Polymorphism - Method Overriding.
    # Override the parent class method __str__
    def __str__(self):
        return super().__str__() + "Guardian Angel: {}\n".format(self.get_guardian_angel())
        # return Hero.__str__(self) + "\nGuardian Angel: {}".format(self.get_guardian_angel())
