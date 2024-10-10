
race = {
    1: "standard",
    2: "uncommon",
    3: "uncommon_2",
    4: "uncommon_3",
    5: "rare",
    6: "rare_2",
    7: "rare_3",
}

weapons = {
    1: "sword",
    2: "axe",
    3: "mace",
    4: "spear",
    5: "bow",
    6: "crossbow",
    7: "staff",
    8: "dagger",
    9: "club",
    10: "flail",
    11: "whip",
    12: "fist",
    13: "shield",
}

weapon_materials = {
    1: "elf wood",
    2: "iron",
    3: "steel",
    4: "bronze",
    5: "dwarf metal",

}

armor_materials = {
    1: "steel",
    2: "iron",
    3: "leather",
    4: "bronze",
    5: "dwarf metal",
    6: "goblin bone",

}

## durability is affected by the material of the weapon and the skill of the craftsperson. 

## as durability degrades the weapon becomes less effective until it is repaired/upkept.

## max damage of the weapon is also affected by the material of the weapon and the skill of the craftsperson.

items = {

}

creatures = {
    1: "shadefire fox",
    2: "goldenthread owl",
    3: "vartular",
    5: "shadowpaw panther",
    6: "bloodclaw bear",
    7: "silvertip stag",
    
}


## item object example below as dictionary
item = {

    ##My thoughts:
    id: "te_001", ## true elf item 1, all ids include a racial prefix and a number
    ## name: "true elf sword",
    "type": "potion",
    "effect": "health",
    "value": 10,
    "cooldown": 1,
    "description": "A small vial of liquid that heals the imbiber for 10 health points.",
    "rarity": "common",

    ## pregenned
    "name": "minor health potion",
    "tier": 1,
    
    "duration": 1,
    
    "weight": 0.1,
    "stackable": True,
    "max_stack": 10,
    "consumable": True,
    "usable": True,
    "equipable": False,
    "sellable": True,
    "tradeable": True,
    "droppable": True,
    "harvestable": False,
    "craftable": False,
    "crafting_materials": {},
    "durability": 0,
    "max_durability": 0,
    "repairable": False,
    "max_damage": 0,
    "min_damage": 0,
    "weapon_type": "",
    "armor_type": "",
    "weapon_material": "",
    "armor_material": "",
    "weapon_skill": 0,
    "armor_skill": 0,
    "weapon_effect": "",
    "armor_effect": "",
    "weapon_effect_chance": 0,
    "armor_effect_chance": 0,
    "weapon_effect_duration": 0,
    "armor_effect_duration": 0,
    "weapon_effect_cooldown": 0,
    "armor_effect_cooldown": 0,
    "weapon_effect_value": 0,
    "armor_effect_value": 0,
    "weapon_effect_type": "",
    "armor_effect_type": "",
    "weapon_effect_description": "",
    "armor_effect_description": "",
    "weapon_effect_stackable": False,
    "armor_effect_stackable": False,
    "weapon_effect_max_stack": 0,
    "armor_effect_max_stack": 0,
    "weapon_effect_consumable": False,
    "armor_effect_consumable": False,
    "weapon_effect_usable": False,
    "armor_effect_usable": False,
    "weapon_effect_equipable": False,
    "armor_effect_equipable": False,
    "weapon_effect_sellable": False,
    "armor_effect_sellable": False,
    "weapon_effect_tradeable": False,
    "armor_effect_tradeable": False,
    "weapon_effect_droppable": False,
}
generic_items = {
## tiered potions of health and stamina. Tiered cooldown reduction potions as well (both percentage and flat reduction)
## food items from various cultures that provide health and stamina regen for a set amount of time.
1: "minor health potion",
2: "health potion",
3: "major health potion",
4: "superior health potion",
5: "minor stamina potion",
6: "stamina potion",
7: "major stamina potion",
8: "superior stamina potion",
9: "minor cooldown reduction potion",
10: "cooldown reduction potion",
11: "major cooldown reduction potion",
12: "superior cooldown reduction potion",
13: "travel bread",
14: "cultural staple",
15: "cultural delicacy",
16: "cultural feast",
17: "water",
18: "wine",
19: "cultural drink",
20: "bandage",
21: "cultural spread light", ## like torches
22: "cultural directed light", ## hooded lanterns, etc
}

uncommon_items = {

}

rare_animal_materials = {
    ## adding a larger variety of materials that can be harvested from rare animals, including hearts, eyes, claws, and other organs/tissues.
    1: "shadefire fox fur",
    2: "goldenthread owl feathers",
    3: "vartular hide",
    4: "shadowpaw panther fur",
    5: "shadowpaw panther heart",
    6: "shadowpaw panther eye",
    7: "shadowpaw panther claw",

    8: "bloodclaw bear hide",
}

regions = {
    1: {
        id: "001",
        "name": "North Wing",
        "terrain": "forest",
        "primary_race": "true elf",
        "secondary_race": "Mur'Braak",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "water",
        },
        "regional_uncommon_items": {
            1: "cultural staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "shadowpaw panther fur",
            2: "shadowpaw panther heart",
            3: "shadowpaw panther eye",
            4: "shadowpaw panther claw",
        },
    },
    2: {
        id: "002",
        "name": "South Wing",
        "terrain": "forest",
        "primary_race": "pure elf",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "wine",
        },
        "regional_uncommon_items": {
            1: "cultural staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "silvertipped stag fur",
            2: "silvertipped stag heart",
            3: "silvertipped stag eye",
            4: "silvertipped stag hoof",
            5: "silvertipped stag antler",
        },
    },
    2: {
        id: "002",
        "name": "South Wing",
        "terrain": "forest",
        "primary_race": "pure elf",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "wine",
        },
        "regional_uncommon_items": {
            1: "cultural staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "silvertipped stag fur",
            2: "silvertipped stag heart",
            3: "silvertipped stag eye",
            4: "silvertipped stag hoof",
            5: "silvertipped stag antler",
        },
    },
    3: {
        id: "003",
        "name": "Northern Split Mountains",
        "terrain": "mountain",
        "primary_race": "dwarf",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "ale",
        },
        "regional_uncommon_items": {
            1: "mushroom staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "unknown ore",
        },
    },
    4: {
        id: "004",
        "name": "Southern Split Mountains",
        "terrain": "mountain",
        "primary_race": "dwarf",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "ale",
        },
        "regional_uncommon_items": {
            1: "southern mushroom staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: " southern unknown ore",
        },
    },
    5: {
        id: "005",
        "name": "Dragon's Tail",
        "terrain": "swamp and mountain",
        "primary_race": "goblin",
        "secondary_race": "Murghaar",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "swamp water",
        },
        "regional_uncommon_items": {
            1: "swamp mushroom staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "goblin bone",
        },
    },
    6: {
        id: "006",
        "name": "Northern Body",
        "terrain": "desert",
        "primary_race": "human",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "water",
        },
        "regional_uncommon_items": {
            1: "cultural staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "human stuff",
        },
    },
    7: {
        id: "007",
        "name": "Southern Body",
        "terrain": "desert",
        "primary_race": "human",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "water",
        },
        "regional_uncommon_items": {
            1: "cultural staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "southern human stuff ore",
        },
    },
    8: {
        id: "008",
        "name": "Northern Foot Hills",
        "terrain": "hills",
        "primary_race": "ogre",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "water",
        },
        "regional_uncommon_items": {
            1: "cultural staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "ogre stuff",
        },
    },
    9: {
        id: "009",
        "name": "Southern Foot Hills",
        "terrain": "hills",
        "primary_race": "troll",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "water",
        },
        "regional_uncommon_items": {
            1: "cultural staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "troll stuff",
        },
    },
    10: {
        id: "010",
        "name": "Dragon's Head Forest",
        "terrain": "Forest",
        "primary_race": "druid",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "water",
        },
        "regional_uncommon_items": {
            1: "cultural staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "druid stuff",
        },
    },
    11: {
        id: "011",
        "name": "Southwestern Islands",
        "terrain": "Forest",
        "primary_race": "unknown",
        "secondary_race": "unknown",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "water",
        },
        "regional_uncommon_items": {
            1: "cultural staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "unknown stuff",
        },
    },
    12: {
        id: "012",
        "name": "Southeastern Islands",
        "terrain": "hills",
        "primary_race": "unknown",
        "secondary_race": "unknown",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "water",
        },
        "regional_uncommon_items": {
            1: "cultural staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "unknown stuff",
        },
    },
    13: {
        id: "013",
        "name": "Northern Islands",
        "terrain": "forest",
         "primary_race": "unknown",
        "secondary_race": "unknown",
        "regional_common_items": {
            1: "minor health potion",
            2: "minor stamina potion",
            3: "travel bread",
            4: "water",
        },
        "regional_uncommon_items": {
            1: "cultural staple",
            2: "cultural spread light",
        },
        "regional_rare_items": {
            1: "unknown stuff",
        },
    },
}