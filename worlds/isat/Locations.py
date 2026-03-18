from __future__ import annotations
from typing import TYPE_CHECKING, NamedTuple, Optional, List, Dict

from BaseClasses import ItemClassification, Location

from .Types import LocData, BaseId
from .Items import ITEM_TABLE

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld


class InStarsAndTimeLocation(Location):
    game = "In Stars and Time"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: location_name_to_id[location_name] for location_name in location_names}

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
    "Reminder Note":            LocData(BaseId.Item+46, "Act 1"),
    "Tutorial Kid Victory":     LocData(BaseId.Misc+1,  "Act 1"),
    "Tutorial Kid Clean Sweep": LocData(BaseId.Misc+2,  "Act 1"),
    "Sky-Loving Kid":           None,
    "Flower Growing One":       None,
    "Drawing Kid":              None,
    "Bonnie Flower":            "Bright Flower",
    "Isabeau Flower":           "Bright Flower",
    "Mirabelle Flower":         "Bright Flower",
    "Odile Flower":             "Bright Flower",
    "Welcome to the show!":     None,

    "Act 2": {
        "Call Loop": None,  # Progression: Floor 1
        "Warning! Sharp!": None,  # Progression: Floor 1

        "Loop Flower": "Bright Flower",
        # Redo this. Likely w/ a string array
        "No thanks, stardust!": "Any Souvenir",  # Progression: Floor 1

        "Memory of Fishing": None,
        "Shopkeeper's Openphrase": None,  # Progression: Shopkeeper
        "Beautiful One's Cupboard": None,
        "Castle-Loving One's Sidequest": None,  # Progression: First Issue
        "Stylish One's Sidequest": None,  # Progression: Stylish One
        "Blind One's House": "Change Openphrase",  # Progression: Openphrase
        "Opened Fanmail": "Loving Fanmail",
    },

    "Act 3": {
        "Memory of Defeat": None,  # Progression: King

        "Bonnie's Friendquest": None,  # Progression: Victory
        "Encore!": None,  # Progression: Victory
        "Memory of Touch": None,  # Progression: Confession

        "Mirabelle's Friendquest": None,  # Progression: Mirabelle
        "Odile's Friendquest": None,  # Progression: Odile
        "Isabeau's Friendquest": None,  # Progression: Loved

        "In this moment...": None,  # Progression: Loved
        "...You are loved.": None,  # Progression: Loved

        "Memory of Puns": None,  # Progression: Betrayed
        "Memory of Memories": None,  # Progression: Betrayed
        "Mystery Book": None,  # Progression: Betrayed
    },

    "Act 4": {
        "What was that about...?": None,  # Progression: Incident
        "Nostalgie": None,
        "IS THIS IT?": None,
        "Here's some change": None,
    },

    "Act 5": {
    },

    "Act 6": {
        "Loop's Coin": None,  # Progression: Two Hats
        "Loop Battle": "Loop's Silver Coin",  # Progression: Floor 1
    }

}

entrance_table: Dict[str, Dict[str, str]] = {
    "Main Room - Circle Key"
}

all_locations = {
    "Level": level_table,
    "Dormont": dormont_table
}

def create_all_locations(world: InStarsAndTimeWorld):
    dormont = world.get_region("Dormont")
    dormont_locations = get_location_names_with_ids(["Dormont - Reminder Note", "Dormont - Tutorial Kid Victory"])
    dormont.add_locations(dormont_locations, InStarsAndTimeLocation)
    print(f"create_all_locations stub...")

# Create Location Table
location_count = 0
location_table = {}
location_name_to_id = {}
for location_set in all_locations:
    for act in all_locations[location_set]:
        for location in all_locations[location_set][act]:
            location_table[f"{location_set} - {location}"] = (BaseId.Base + location_count,
                                                                     f"{act} - {location_set}",
                                                                     all_locations[location_set][act][location]),
            location_name_to_id[f"{location_set} - {location}"] = BaseId.Base + location_count
            # print(f"\"{location_set} - {location}\": LocData({base_id+location_count}, \"{act} - {location_set}\", {all_locations[location_set][act][location]})")
            location_count += 1
