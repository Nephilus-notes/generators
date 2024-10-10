from classes import *

def initialize():
    items = [
        Item("0001_pe", "Minor Health Potion", "Pure Elf", "A common potion for healing", 1, "healing", 7, 0.1), 
        Item("0002_pe", "Health Potion", "Pure Elf", "An uncommon potion for healing", 2, "healing", 7, 0.1), 
        Item("0003_pe", "Major Health Potion", "Pure Elf", "A rare potion for healing", 3, "healing", 7, 0.1), 
        Item("0004_pe", "Superior Health Potion", "Pure Elf", "A legendary potion for healing", 4, "healing", 7, 0.1), 
        Item("0005_pe", "Minor Stamina Potion", "Pure Elf", "A common potion for stamina", 1, "stamina", 7, 0.1), 
        Item("0006_pe", "Stamina Potion", "Pure Elf", "An uncommon potion for stamina", 2, "stamina", 7, 0.1), 
        Item("0007_pe", "Major Stamina Potion", "Pure Elf", "A rare potion for stamina", 3, "stamina", 7, 0.1), 
        Item("0008_pe", "Superior Stamina Potion", "Pure Elf", "A legendary potion for stamina", 4, "stamina", 7, 0.1), 
        Item("0009_pe", "Minor Cooldown Reduction Potion", "Pure Elf", "A common potion for Cooldown Reduction", 1, "cdr", 7, 0.1), 
        Item("0010_pe", "Cooldown Reduction Potion", "Pure Elf", "An uncommon potion for Cooldown Reduction", 2, "cdr", 7, 0.1), 
        Item("0011_pe", "Major Cooldown Reduction Potion", "Pure Elf", "A rare potion for Cooldown Reduction", 3, "cdr", 7, 0.1), 
        Item("0012_pe", "Superior Cooldown Reduction Potion", "Pure Elf", "A legendary potion for Cooldown Reduction", 4, "cdr", 7, 0.1), 
        Item("0013_dw", "Ap'Liq", "Dwarf", "An apple cider shot that heals health while getting the imbiber drunk, reducing focus, cooldown reduction rates, and stamina recharge.", 1, "healing", 7, 0.1), 
        Item("0014_dw", "Gra'Liq", "Dwarf", "A shot of a light grain based alcohol. It provides some healing and can get the imbiber drunk.", 2, "healing", 7, 0.1), 
        Item("0015_dw", "Pot'Liq", "Dwarf", "A shot of a potato liquor.  Dwarven magic infused into it means that it heals a good amount of health but repeated shots have been known to incapacitate the hardiest of warriors.", 3, "healing", 7, 0.1), 
        Item("0016_dw", "Shrum'Liq", "Dwarf", "A powerful mushroom liquor that restores a large amount of health but gets the imbiber very, very drunk.", 4, "healing", 7, 0.1), 
        Item("0017_dw", "He'Te", "Dwarf", "A drink of various refreshing herbs that perks the user up.", 1, "stamina", 7, 0.1), 
        Item("0018_dw", "Mint'Te", "Dwarf", "A drink made from steeped leaves that gives the drinker a boost of energy that occasionally ends in a crash.", 2, "stamina", 7, 0.1), 
        Item("0019_dw", "Gre'Te", "Dwarf", "A shot of a formerly warm beverage made from steeped leaves.  It wakes up the drinker, but can cause an energy crash", 3, "stamina", 7, 0.1), 
        Item("0020_dw", "Bla'Te", "Dwarf", "A shot of a formerly warm beverage made from steeped leaves.  It wakes up the drinker, but can cause an energy crash", 4, "stamina", 7, 0.1), 
        Item("0021_dw", "De'co", "Dwarf", "decaf.", 1, "cdr", 7, 0.1), 
        Item("0022_dw", "Fu'ro'co", "Dwarf", "A shot of a drink made from roasted beans that gives a solid boost of energy but is followed by a crash.", 2, "cdr", 7, 0.1), 
        Item("0023_dw", "Esp'co", "Dwarf", "espresso.", 3, "cdr", 7, 0.1), 
        Item("0024_dw", "Du'so'esp'co", "Dwarf", "a double shot of espresso blended by dwarves.", 4, "cdr", 7, 0.1), 
    ]
    return items



items = initialize()
# print("Items: ", items)
# Shop("The Drunken Dwarf", 1, items, "Dwarf")
Shop("Purity", 5, items, "Pure Elf")