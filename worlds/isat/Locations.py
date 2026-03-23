from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Any

from BaseClasses import Location

from .Types import LocData, BaseId

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld


class InStarsAndTimeLocation(Location):
    game = "In Stars and Time"

# Location IDs should match their item counterpart. If there is none associated, use BaseId.Misc
level_table: Dict[str, LocData] = {  # Levels
    "Siffrin - Buy One Get One Three":  LocData(BaseId.Skill+20,    "Act 1"),
    "Siffrin - Done Heal":              LocData(BaseId.Skill+16,    "Act 1"),
    "Siffrin - In A While, Rockodile":  LocData(BaseId.Skill+17,    "Act 1"),
    "Siffrin - Regener-ade":            LocData(BaseId.Skill+155,   "Act 1"),
    "Siffrin - Rose Printed Glasses":   LocData(BaseId.Skill+18,    "Act 1"),
    "Siffrin - Tear You Apart":         LocData(BaseId.Skill+157,   "Act 1"),
    "Siffrin - Rock Bottom":            LocData(BaseId.Skill+156,   "Act 1"),
    "Mirabelle - Lovely Moving Cure":   LocData(BaseId.Skill+36,    "Act 1"),
    "Mirabelle - Shining Life":         LocData(BaseId.Skill+37,    "Act 1"),
    "Mirabelle - Mega Sparkle Heal":    LocData(BaseId.Skill+39,    "Act 1"),
    "Isabeau - SO WEAK!!!":             LocData(BaseId.Skill+25,    "Act 1"),
    "Isabeau - BREAK, BREAK!!!":        LocData(BaseId.Skill+26,    "Act 1"),
    "Isabeau - NOT OVER YET!!!":        LocData(BaseId.Skill+28,    "Act 1"),
    "Odile - Paper α V":                LocData(BaseId.Skill+46,    "Act 1"),
    "Odile - Craft Buff":               LocData(BaseId.Skill+48,    "Act 1"),
    "Odile - Craft Break":              LocData(BaseId.Skill+49,    "Act 1"),
}

dormont_table: Dict[str, LocData] = {
    "Dormont - Castle-Loving One's Sidequest":  LocData(BaseId.Weapon+27),
    "Dormont - Stylish One's Sidequest":        LocData(BaseId.Item+55),
    "Dormont - Sky-Loving Kid":                 LocData(BaseId.Item+47),
    "Dormont - Flower Growing One":             LocData(BaseId.Item+43),
    "Dormont - Drawing Kid":                    LocData(BaseId.Item+54),
    "Dormont - Storage House":                  LocData(BaseId.Item+69,     "Act 2", "has", "Change Openphrase"),
    "Dormont - Reminder Note":                  LocData(BaseId.Item+46),
    "Dormont - Memory of Touch":                LocData(BaseId.Armor+37,    "Act 3"),
    "Dormont - Memory of Fishing":              LocData(BaseId.Armor+38),
    "Dormont - Memory of Defeat":               LocData(BaseId.Armor+83),
    "Dormont - Memory of Memories":             LocData(BaseId.Armor+87),
    "Dormont - Mirabelle's Friendquest":        LocData(BaseId.Armor+50,    "Act 3"),

    "Dormont - Memory of Puns":                 LocData(BaseId.Armor+55),
    "Dormont - Isabeau's Friendquest":          LocData(BaseId.Armor+60,    "Act 3"),

    "Dormont - Odile's Friendquest":            LocData(BaseId.Armor+70,    "Act 3"),

    "Dormont - Bonnie's Friendquest":           LocData(BaseId.Armor+80,    "Act 3"),

    "Dormont - Opened Fanmail":                 LocData(BaseId.Armor+16),
    "Dormont - Beautiful One's Cupboard":       LocData(BaseId.Weapon+32),
    "Dormont - Tutorial Kid Victory":           LocData(BaseId.Misc+1),
    "Dormont - Tutorial Kid Clean Sweep":       LocData(BaseId.Misc+2),
    "Dormont - Warning! Sharp!":                LocData(BaseId.Item+12),
    "Dormont - Call Loop":                      LocData(BaseId.Skill+160),
    "Dormont - Shopkeeper's Openphrase":        LocData(BaseId.Misc+3),
    "Dormont - Mystery Book":                   LocData(BaseId.Misc+4),
    "Dormont - Bonnie Flower":                  LocData(BaseId.Misc+5,     "Act 2", "has", "Bright Flower"),
    "Dormont - Isabeau Flower":                 LocData(BaseId.Misc+6,     "Act 2", "has", "Bright Flower"),
    "Dormont - Mirabelle Flower":               LocData(BaseId.Misc+7,     "Act 2", "has", "Bright Flower"),
    "Dormont - Odile Flower":                   LocData(BaseId.Misc+8,     "Act 2", "has", "Bright Flower"),
    "Dormont - No thanks, stardust!":           LocData(BaseId.Misc+9,     "Act 2",    "has_any",
                                                ["Bright Flower", "Four-Pointed Leaf", "Loving Fanmail"]),
    "Dormont - What was that about...?":        LocData(BaseId.Misc+10),
    "Dormont - Loop Flower":                    LocData(BaseId.Misc+11,     "Act 2", "has", "Bright Flower"),
    "Dormont - Welcome to the show!":           LocData(BaseId.Misc+12),
    "Dormont - Encore!":                        LocData(BaseId.Armor+82),
    "Dormont - Loop Battle":                    LocData(BaseId.Misc+13,     "Act 6"),
    "Dormont - Loop's Coin":                    LocData(BaseId.Item+62,     "Act 6"),
    "Dormont - In this moment...":              LocData(BaseId.Armor+86,    "Act 3"),
    "Dormont - ...You are loved.":              LocData(BaseId.Misc+14,     "Act 3"),
    "Dormont - Nostalgie":                      LocData(BaseId.Skill+13),
    "Dormont - IS THIS IT?":                    LocData(BaseId.Misc+15),
    "Dormont - Here's some change":             LocData(BaseId.Misc+16),

}

entrance_table: Dict[str, LocData] = {
    "Entrance - Main Room - Circle Key":    LocData(BaseId.Item+22, "Act 1"),
    "Entrance - Storage Room - Vial 1":     LocData(BaseId.Misc+18,  "Act 1"),
    "Entrance - Storage Room - Vial 2":     LocData(BaseId.Misc+19,  "Act 1"),
    "Entrance - Storage Room - Vial 3":     LocData(BaseId.Misc+20, "Act 1"),
    "Entrance - Storage Room - Vial 4":     LocData(BaseId.Misc+21, "Act 1"),
    "Entrance - Jackpot!":                  LocData(BaseId.Misc+22, "Act 1"),
}

floor_1_table: Dict[str, Dict[str, LocData]] = {
    "Main Room": {

    },
}

floor_2_table: Dict[str, Dict[str, LocData]] = {
    "Main Room": {

    },
}

floor_3_table: Dict[str, Dict[str, LocData]] = {
    "Main Room": {

    },
}

the_end_table: Dict[str, Dict[str, LocData]] = {

}


all_locations: Dict[str, LocData] = {
    **level_table,
    **dormont_table,
    **entrance_table,
    **floor_1_table["Main Room"],
    **floor_2_table["Main Room"],
    **floor_3_table["Main Room"],
    **the_end_table,
}

# Create location table
LOCATION_TABLE = {location_name: all_locations[location_name].id for location_name in all_locations}

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: all_locations[location_name].id for location_name in location_names}

def create_location(world: InStarsAndTimeWorld, region_name: str, location_table) -> None:
    region = world.get_region(region_name)
    locations = get_location_names_with_ids([location_name for location_name in location_table])
    region.add_locations(locations, InStarsAndTimeLocation)

def create_all_locations(world: InStarsAndTimeWorld) -> None:
    create_location(world, "Level", level_table)
    create_location(world, "Dormont", dormont_table)
    create_location(world, "Entrance", entrance_table)

    for sub_region in floor_1_table:
        create_location(world, f"Floor 1 - {sub_region}", floor_1_table[sub_region])

    for sub_region in floor_2_table:
        create_location(world, f"Floor 2 - {sub_region}", floor_1_table[sub_region])

    for sub_region in floor_3_table:
        create_location(world, f"Floor 3 - {sub_region}", floor_1_table[sub_region])

    create_location(world, "The End", the_end_table)

def create_events(world: InStarsAndTimeWorld) -> None:
    pass