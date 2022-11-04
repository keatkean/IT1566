import Hero
import dragon_knight
import Omniknight
import Crystal_Maiden

import Hero as h
import dragon_knight as dk
import Omniknight as omni
import Crystal_Maiden as cm

from Hero import *
from dragon_knight import *
from Omniknight import *
from Crystal_Maiden import *

# Create a Hero Instance called hero1
# hero1 = Hero("Hero1", "Melee", "Physical", 100, 100, "Ultimate", 1000, 1000)
hero1 = Hero.Hero("Hero1", "Melee", "Physical", 100, 100, "Ultimate", 1000, 1000)
# hero1 = h.Hero("Hero1", "Melee", "Physical", 100, 100, "Ultimate", 1000, 1000)

# Increase number of Hero by 1
Hero.Hero.number_of_Hero += 1

# Print class attribute number_of_Hero
print("Number of Hero: ", Hero.Hero.number_of_Hero)

# Call print_hero_info method
hero1.print_hero_info()

# Create a Dragon Knight Instance called dragon_knight1
dragon_knight1 = dragon_knight.DragonKnight("Dragon Knight", "Melee", "Physical", 100, 100, "Dragon Formed", 1000, 1000)
# dragon_knight1 = DragonKnight("Dragon Knight", "Melee", "Physical", 100, 100, "Dragon Formed", 1000, 1000)
# dragon_knight1 = dk.DragonKnight("Dragon Knight", "Melee", "Physical", 100, 100, "Dragon Formed", 1000, 1000)

# Increase number of Hero by 1
Hero.Hero.number_of_Hero += 1

# Call Dragon_form method
dragon_knight1.dragon_form()

# Call Dragon_blood method
dragon_knight1.dragon_blood()

# Print class attribute number_of_Hero
print("Number of Hero: ", Hero.Hero.number_of_Hero)

# Call print_hero_info method
dragon_knight1.print_hero_info()

# Create an Omniknight Instance called omniknight1
omniknight1 = Omniknight("Omniknight", "Melee", "Physical", 100, 100, "Guardian Angel")
# omniknight1 = omni.Omniknight("Omniknight", "Melee", "Physical", 100, 100, "Guardian Angel")
# omniknight1 = Omniknight.Omniknight("Omniknight", "Melee", "Physical", 100, 100, "Guardian Angel")

# Increase number of Hero by 1
Hero.Hero.number_of_Hero += 1

# Call Guardian Angel method
omniknight1.guardian_angel()

# Call heal method
omniknight1.heal()

# Print class attribute number_of_Hero
print("Number of Hero: ", Hero.Hero.number_of_Hero)

# Call __str__ method
print(omniknight1)

# Create a CrystalMaidsen Instance called crystal_maiden1
crystal_maiden1 = CrystalMaiden("Crystal Maiden", "Ranged", "Magical", 100, 100, "Freezing Field", 40, 200)

# Increase number of Hero by 1
Hero.Hero.number_of_Hero += 1

# Call activate_freezing_field method
crystal_maiden1.activate_freezing_field()

# Print class attribute number_of_Hero
print("Number of Hero: ", Hero.Hero.number_of_Hero)

# Call __str__ method
print(crystal_maiden1)

