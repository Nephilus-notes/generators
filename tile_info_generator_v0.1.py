import random

from dicts import weather_types, terrain_types, terrain_modifiers, weather_types, encounter_type, building_type


def generate_new_tile():
    printed_string = ""
    # Generate a new tile
    tile = {
        'terrain': terrain_types[random.randint(1, len(terrain_types))],
        'modifier': terrain_modifiers[random.randint(1, len(terrain_modifiers))],
        'weather': weather_types[random.randint(1, len(weather_types))],
        'encounter': encounter_type[random.randint(1, len(encounter_type))],
    }

    if tile['modifier'] == 'building':
        tile['building'] = building_type[random.randint(1, len(building_type))]
        printed_string = f"""the new tile is a {tile['terrain']} and ahead is a {tile['building']}. 
the weather is {tile['weather']}, 
the encounter is {tile['encounter']}.
"""
    elif tile['modifier'] == 'double':
        tile['building'] = building_type[random.randint(1, len(building_type))]
        tile['modifier'] = terrain_modifiers[random.randint(1, len(terrain_modifiers) - 1)]
        if tile['modifier'] == 'building':
            tile['building2'] = building_type[random.randint(1, len(building_type))]
            tile['building'] = building_type[random.randint(1, len(building_type))]
            printed_string = f"""the new tile is a {tile['terrain']} with a {tile['building']} and a {tile['building2']} in it. 
the weather is {tile['weather']}, 
the encounter is {tile['encounter']}."""
            
        else:
            printed_string = f"""the new tile is a {tile['terrain']} with a {tile['modifier']} in it. 
the weather is {tile['weather']}, 
the encounter is {tile['encounter']} 
and the building is a {tile['building']}. 
Double!"""
    else:
        printed_string = f"""the new tile is a {tile['terrain']} with a {tile['modifier']} in it. 
the weather is {tile['weather']}, 
the encounter is {tile['encounter']} 
and the building are no buildings in sight."""

    print(printed_string)

    return tile

generate_new_tile()


