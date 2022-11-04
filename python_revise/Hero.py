class Hero:
    # Class Attributes
    attack_type = ['Melee', 'Ranged']
    damage_type = ['Physical', 'Magical', 'Pure']
    number_of_Hero = 0

    # Initializer
    def __init__(self, name, attack_type, damage_type, attack, defense, ultimate_skill, health=50, mana=50):
        # Encapsulation
        # - hides internal representation of an object from the outside
        # - allows the access of private attribute of an object to be controlled via methods

        self.__name = name  # self.__name is a private instance attribute

        # check if attack_type is valid
        # To reference a class attribute from code inside the class, you qualify it
        # with self.__class__ (or the class name)
        if attack_type in Hero.attack_type:  # Hero.attack_type is a class attribute.
            self.__attack_type = attack_type  # self.__attack_type is a private instance attribute
        else:
            print("Invalid attack type!")
            self.__attack_type = 'Unknown'

        # check if damage_type is valid
        # To reference a class attribute from code inside the class, you qualify it
        # with self.__class__ (or the class name)
        if damage_type in self.__class__.damage_type:  # self.__class__.damage_type is a class attribute
            self.__damage_type = damage_type  # self.damage_type is a private instance attribute
        else:
            print("Invalid damage type!")
            self.__damage_type = 'Unknown'

        # check if attack is valid and is between 0 and 100
        if 0 <= attack <= 100:
            self.__attack = attack  # self.__attack is a private instance attribute
        else:
            print("Invalid attack!")
            self.__attack = 0

        # check if defense is valid and is between 0 and 100
        if 0 <= defense <= 100:
            self.__defense = defense  # self.__defense is a private instance attribute
        else:
            print("Invalid defense!")
            self.__defense = 0

        self.__health = health  # self.__health is an instance attribute
        self.__mana = mana  # self.__mana is a private instance attribute

        # check if ultimate_skill is valid string
        if isinstance(ultimate_skill, str):
            self.__ultimate_skill = ultimate_skill  # self.__ultimate_skill is a private instance attribute
        else:
            print("Invalid ultimate skill!")
            self.__ultimate_skill = 'Unknown'

    # Getters/Accessor Methods
    def get_name(self):
        return self.__name

    def get_attack_type(self):
        return self.__attack_type

    def get_attack(self):
        return self.__attack

    def get_damage_type(self):
        return self.__damage_type

    def get_defense(self):
        return self.__defense

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def get_ultimate_skill(self):
        return self.__ultimate_skill

    # Setters/Mutator Methods
    def set_name(self, name):
        self.__name = name

    def set_attack_type(self, attack_type):
        self.__attack_type = attack_type

    def set_attack(self, attack):
        self.__attack = attack

    def set_damage_type(self, damage_type):
        self.__damage_type = damage_type

    def set_defense(self, defense):
        self.__defense = defense

    def set_health(self, health):
        self.__health = health

    def set_mana(self, mana):
        self.__mana = mana

    def set_ultimate_skill(self, ultimate_skill):
        self.__ultimate_skill = ultimate_skill

    # Methods
    def attack(self):
        print("Attacking with " + self.__attack_type + " attack!\n")

    def defend(self):
        print("Defending!\n")

    def heal(self):
        print("Healing!\n")

    def cast_ultimate_skill(self):
        print("Casting " + self.__ultimate_skill + "!\n")

    def Description(self):
        print("This is a hero\n")

    def __str__(self):
        return "Name: " + self.__name + "\nAttack Type: " + self.__attack_type + "\nDamage Type: " + self.__damage_type + "\nAttack: " + str(
            self.__attack) + "\nDefense: " + str(self.__defense) + "\nHealth: " + str(self.__health) + "\nMana: " + str(
            self.__mana) + "\nUltimate Skill: " + self.__ultimate_skill + "\n"

    # Abstraction
    # - hides unnecessary details from users
    # - allows implementation of more complex logic without having the need to understand the hidden details
    def print_hero_info(self):
        print(self.__str__())
