import Hero
import dragon_knight
import Omniknight

import Hero as h
import dragon_knight as dk
import Omniknight as omni

from Hero import *
from dragon_knight import *
from Omniknight import *

# Create a Hero Instance called hero1
hero1 = Hero("Hero1", "Melee", "Physical", 100, 100, "Ultimate", 1000, 1000)
# hero1 = Hero.Hero("Hero1", "Melee", "Physical", 100, 100, "Ultimate", 1000, 1000)
# hero1 = h.Hero("Hero1", "Melee", "Physical", 100, 100, "Ultimate", 1000, 1000)

# Increase number of Hero by 1
Hero.number_of_Hero += 1

# Print class attribute number_of_Hero
print("Number of Hero: ", Hero.number_of_Hero)

# Call print_hero_info method
hero1.print_hero_info()

# Create a Dragon Knight Instance called dragon_knight1
dragon_knight1 = dragon_knight.DragonKnight("Dragon Knight", "Melee", "Physical", 100, 100, "Dragon Formed", 1000, 1000)
# dragon_knight1 = DragonKnight("Dragon Knight", "Melee", "Physical", 100, 100, "Dragon Formed", 1000, 1000)
# dragon_knight1 = dk.DragonKnight("Dragon Knight", "Melee", "Physical", 100, 100, "Dragon Formed", 1000, 1000)

# Increase number of Hero by 1
Hero.number_of_Hero += 1

# Call Dragon_form method
dragon_knight1.dragon_form()

# Call Dragon_blood method
dragon_knight1.dragon_blood()

# Print class attribute number_of_Hero
print("Number of Hero: ", Hero.number_of_Hero)

# Call print_hero_info method
dragon_knight1.print_hero_info()

# Create an Omniknight Instance called omniknight1
omniknight1 = Omniknight("Omniknight", "Melee", "Physical", 100, 100, "Guardian Angel")
# omniknight1 = omni.Omniknight("Omniknight", "Melee", "Physical", 100, 100, "Guardian Angel")
# omniknight1 = Omniknight.Omniknight("Omniknight", "Melee", "Physical", 100, 100, "Guardian Angel")

# Increase number of Hero by 1
Hero.number_of_Hero += 1

# Call Guardian Angel method
omniknight1.guardian_angel()

# Call heal method
omniknight1.heal()

# Call __str__ method
print(omniknight1)
