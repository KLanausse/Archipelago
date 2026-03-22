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
    "Dormont - Reminder Note":            LocData(BaseId.Item+46, "Act 1"),
    "Dormont - Tutorial Kid Victory":     LocData(BaseId.Misc+1,  "Act 1"),
    "Dormont - Tutorial Kid Clean Sweep": LocData(BaseId.Misc+2,  "Act 1"),
    "Dormont - Sky-Loving Kid":           LocData(BaseId.Item+47, "Act 1"),
    "Dormont - Flower Growing One":       LocData(BaseId.Item+43, "Act 1"),
    "Dormont - Drawing Kid":              LocData(BaseId.Item+54, "Act 1"),
    "Dormont - Bonnie Flower":            LocData(BaseId.Misc+3,  "Act 1",  "has", "Bright Flower"),
    "Dormont - Isabeau Flower":           LocData(BaseId.Misc+4,  "Act 1",  "has", "Bright Flower"),
    "Dormont - Mirabelle Flower":         LocData(BaseId.Misc+5,  "Act 1",  "has", "Bright Flower"),
    "Dormont - Odile Flower":             LocData(BaseId.Misc+6,  "Act 1",  "has", "Bright Flower"),
    "Dormont - Welcome to the show!":     LocData(BaseId.Misc+7,  "Act 1"),

    # Act 2 | Progression: Floor 1 (Circle Key)
    "Dormont - Loop Flower":            LocData(BaseId.Misc+8,      "Act 2",    "has", "Bright Flower"),
    "Dormont - Call Loop":              LocData(BaseId.Skill+160,   "Act 2"),
    "Dormont - Warning! Sharp!":        LocData(BaseId.Misc+9,      "Act 2"),
    "Dormont - No thanks, stardust!":   LocData(BaseId.Misc+10,     "Act 2",    "has_any",
                                                ["Bright Flower", "Four-Pointed Leaf", "Loving Fanmail"]),
    "Dormont - Memory of Fishing":      LocData(BaseId.Armor+38,   "Act 2"),
    # "Shopkeeper's Openphrase": None,  # Progression: Shopkeeper
    # "Beautiful One's Cupboard": None,
    # "Castle-Loving One's Sidequest": None,  # Progression: First Issue
    # "Stylish One's Sidequest": None,  # Progression: Stylish One
    # "Blind One's House": "Change Openphrase",  # Progression: Openphrase
    # "Opened Fanmail": "Loving Fanmail",

    # Act 3 | Progression: King (Lovely Moving Shield or Holy Care Shield)
    # "Memory of Defeat": None,  #
    # "Bonnie's Friendquest": None,  # Progression: Victory
    # "Encore!": None,  # Progression: Victory
    # "Memory of Touch": None,  # Progression: Confession
    # "Mirabelle's Friendquest": None,  # Progression: Mirabelle
    # "Odile's Friendquest": None,  # Progression: Odile
    # "Isabeau's Friendquest": None,  # Progression: Loved
    # "In this moment...": None,  # Progression: Loved
    # "...You are loved.": None,  # Progression: Loved


    # Act 4 | Progression: Betrayed
    # "Memory of Puns": None,
    # "Memory of Memories": None,  # Progression: Betrayed
    # "Mystery Book": None,  # Progression: Betrayed
    # "What was that about...?": None,  # Progression: Incident
    # "Nostalgie": None,
    # "IS THIS IT?": None,
    # "Here's some change": None,

    # Act 5

    # Act 6
    # "Loop's Coin": None,  # Progression: Two Hats
    # "Loop Battle": "Loop's Silver Coin",  # Progression: Floor 1

}

entrance_table: Dict[str, LocData] = {
    "Entrance - Main Room - Circle Key":    LocData(BaseId.Item+22, "Act 1"),
    "Entrance - Storage Room - Vial 1":     LocData(BaseId.Misc+11,  "Act 1"),
    "Entrance - Storage Room - Vial 2":     LocData(BaseId.Misc+12,  "Act 1"),
    "Entrance - Storage Room - Vial 3":     LocData(BaseId.Misc+13, "Act 1"),
    "Entrance - Storage Room - Vial 4":     LocData(BaseId.Misc+14, "Act 1"),
    "Entrance - Jackpot!":                  LocData(BaseId.Misc+15, "Act 1"),
}

floor_1_table: Dict[str, Dict[str, LocData]] = {
    "Main Room": {

    },
}


all_locations: Dict[str, LocData] = {
    **level_table,
    **dormont_table,
    **entrance_table,
    **floor_1_table["Main Room"],
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

    print(f"In Stars And Time: create_all_locations stub...")

def create_events(world: InStarsAndTimeWorld) -> None:
    pass