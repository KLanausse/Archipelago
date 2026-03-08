from typing import TYPE_CHECKING, NamedTuple, Optional, List, Dict

from BaseClasses import ItemClassification, Location

from .Types import LocData, BaseId
from .Items import item_table

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld


class InStarsAndTimeLocation(Location):
    game = "In Stars and Time"


level_table = {  # Levels
    "Act 1": {
        "Siffrin - Buy One Get One Three": None,
        "Siffrin - Done Heal": None,
        "Siffrin - In A While, Rockodile": None,
        "Siffrin - Regener-ade": None,
        "Siffrin - Rose Printed Glasses": None,
        "Siffrin - Tear You Apart": None,
        "Siffrin - Rock Bottom": None,
        "Mirabelle - Lovely Moving Cure": None,
        "Mirabelle - Shining Life": None,
        "Mirabelle - Mega Sparkle Heal": None,
        "Isabeau - SO WEAK!!!": None,
        "Isabeau - BREAK, BREAK!!!": None,
        "Isabeau - NOT OVER YET!!!": None,
        "Odile - Paper α V": None,
        "Odile - Craft Buff": None,
        "Odile - Craft Break": None,
    }
}

dormont_table: Dict[str, Dict[str, str]] = {
    "Act 1": {
        "Reminder Note": None,
        "Tutorial Kid Victory": None,
        "Tutorial Kid Clean Sweep": None,
        "Sky-Loving Kid": None,
        "Flower Growing One": None,
        "Drawing Kid": None,
        "Bonnie Flower": "Bright Flower",
        "Isabeau Flower": "Bright Flower",
        "Mirabelle Flower": "Bright Flower",
        "Odile Flower": "Bright Flower",
        "Welcome to the show!": None,
    },

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

def create_all_locations(arg):
    print(f"create_all_locations stub... Passed arg: {arg}")

# Create Location Table
location_count = 0
location_table = {}
for location_set in all_locations:
    for act in all_locations[location_set]:
        for location in all_locations[location_set][act]:
            location_table[f"{location_set} - {location}"] = (BaseId.Base + location_count,
                                                                     f"{act} - {location_set}",
                                                                     all_locations[location_set][act][location])
            # print(f"\"{location_set} - {location}\": LocData({base_id+location_count}, \"{act} - {location_set}\", {all_locations[location_set][act][location]})")
            location_count += 1
