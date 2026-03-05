from typing import TYPE_CHECKING, NamedTuple, Optional, List

from jinja2.nodes import Dict

from BaseClasses import ItemClassification, Location

from .Types import LocData
from ..jakanddaxter import level_table

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld

base_id = 1677310

class InStarsAndTimeLocation(Location):
    game = "In Stars and Time"

level_table = { # Levels
    "Siffrin - Buy One Get One Three",
    "Siffrin - Done Heal",
    "Siffrin - In A While, Rockodile",
    "Siffrin - Regener-ade",
    "Siffrin - Rose Printed Glasses",
    "Siffrin - Tear You Apart",
    "Siffrin - Rock Bottom",
    "Mirabelle - Lovely Moving Cure",
    "Mirabelle - Shining Life",
    "Mirabelle - Mega Sparkle Heal",
    "Isabeau - SO WEAK!!!",
    "Isabeau - BREAK, BREAK!!!",
    "Isabeau - NOT OVER YET!!!",
    "Odile - Paper α V",
    "Odile - Craft Buff",
    "Odile - Craft Break",
}

dormont_table: Dict[str, Dict[str, str]] = {
    "Act 1": {
        "Reminder Note":            None,
        "Tutorial Kid Victory":     None,
        "Tutorial Kid Clean Sweep": None,
        "Sky-Loving Kid":           None,
        "Flower Growing One":       None,
        "Drawing Kid":              None,
        "Bonnie Flower":            "Bright Flower",
        "Isabeau Flower":           "Bright Flower",
        "Mirabelle Flower":         "Bright Flower",
        "Odile Flower":             "Bright Flower",
        "Welcome to the show!":     None,
    },

    "Act 2": {
        "Call Loop":                        None, # Progression: Floor 1
        "Warning! Sharp!":                  None, # Progression: Floor 1

        "Loop Flower":                      "Bright Flower",
        # Redo this. Likely w/ a string array
        "No thanks, stardust!":             "Any Souvenir", # Progression: Floor 1

        "Memory of Fishing":                None,
        "Shopkeeper's Openphrase":          None, # Progression: Shopkeeper
        "Beautiful One's Cupboard":         None,
        "Castle-Loving One's Sidequest":    None, # Progression: First Issue
        "Stylish One's Sidequest":          None, # Progression: Stylish One
        "Blind One's House":                "Change Openphrase", # Progression: Openphrase
        "Opened Fanmail":                   "Loving Fanmail",
    },

    "Act 3": {
        "Memory of Defeat":         None, # Progression: King

        "Bonnie's Friendquest":     None, # Progression: Victory
        "Encore!":                  None, # Progression: Victory
        "Memory of Touch":          None, # Progression: Confession


        "Mirabelle's Friendquest":  None, # Progression: Mirabelle
        "Odile's Friendquest":      None, # Progression: Odile
        "Isabeau's Friendquest":    None, # Progression: Loved

        "In this moment...":        None, # Progression: Loved
        "...You are loved.":        None, # Progression: Loved

        "Memory of Puns":           None, # Progression: Betrayed
        "Memory of Memories":       None, # Progression: Betrayed
        "Mystery Book":             None, # Progression: Betrayed
    },

    "Act 4": {
        "What was that about...?":  None, # Progression: Incident
        "Nostalgie":                None,
        "IS THIS IT?":              None,
        "Here's some change":       None,
    },

    "Act 5": {
    },

    "Act 6": {
        "Loop's Coin": None, # Progression: Two Hats
        "Loop Battle": "Loop's Silver Coin", # Progression: Floor 1
    }

}

entrance_table: Dict[str, Dict[str, str]] = {
    "Main Room - Circle Key"
}

location_table = {}
# Create Location Table
#idx = 0
#for location in location_region_map:
#    location_table[location] = LocData(base_id+idx, location_region_map[location])
#    idx += 1