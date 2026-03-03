from typing import TYPE_CHECKING, NamedTuple, Optional
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

dormont_table = {
    "Act 1": {
        "Reminder Note":            None,
        "Tutorial Kid Victory":     None,
        "Tutorial Kid Clean Sweep": None,
        "Sky-Loving Kid":           None,
        "Flower Growing One":       None,
        "Drawing Kid":              None,
        "Bonnie Flower":            "Flower Growing One",
        "Isabeau Flower":           "Flower Growing One",
        "Mirabelle Flower":         "Flower Growing One",
        "Odile Flower":             "Flower Growing One",
        "Welcome to the show!":     None,
    },
    "Castle-Loving One's Sidequest",
    "Stylish One's Sidequest",
    "Blind One's House",

    "Memory of Touch",
    "Memory of Fishing",
    "Memory of Defeat",
    "Memory of Memories",
    "Mirabelle's Friendquest":     ,
    "Memory of Puns":              ,
    "Isabeau's Friendquest":       ,
    "Odile's Friendquest":         ,
    "Bonnie's Friendquest":        ,
    "Opened Fanmail":              ,
    "Beautiful One's Cupboard":    ,

    "Warning! Sharp!":             ,
    "Call Loop":                   ,
    "Shopkeeper's Openphrase":     ,
    "Mystery Book":                ,

    "No thanks, stardust!":        ,
    "What was that about...?":     ,
    "Loop Flower":                 ,
    "Encore!":                     ,
    "Loop Battle":                 ,
    "Loop's Coin":                 ,
    "In this moment...":           ,
    "...You are loved.":           ,
    "Nostalgie":                   ,
    "IS THIS IT?":                 ,
    "Here's some change":          ,
}

location_region_map = {

    "Dormont - Sky-Loving Kid":                 "Dormont - Act 1",
    "Dormont - Flower Growing One":             "Dormont - Act 1",
    "Dormont - Drawing Kid":                    "Dormont - Act 1",
    "Entrance - Main Room - Circle Key":        "Entrance",
    "Dormont - Call Loop":                      "Dormont - Act 2",
    "Dormont - Castle-Loving One's Sidequest":  "Dormont - Act 2",
    "Dormont - Stylish One's Sidequest":        "Dormont - Act 2",
    "Dormont - Blind One's House":              "Dormont - Act 2",
    "Dormont - Opened Fanmail":                 "Dormont - Act 2",
    "Dormont - Shopkeeper's Openphrase":        "Dormont - Act 2",
    "Dormont - Beautiful One's Cupboard":       "Dormont - Act 2",
    "Dormont - Memory of Fishing":              "Dormont - Act 2",
    "Dormont - Memory of Defeat":               "The King - Act 2",
    "Dormont - Memory of Touch":                "Dormont - Act 3",
    "Dormont - Mirabelle's Friendquest":        "Dormont - Act 3",
    "Dormont - Isabeau's Friendquest":          "Dormont - Act 3",
    "Dormont - Odile's Friendquest":            "Dormont - Act 3",
    "Dormont - Bonnie's Friendquest":           "Dormont - Act 3",
    "Dormont - Warning! Sharp!":                "Dormont - Act 3",

    "Dormont - Memory of Memories":             "Dormont - Act 4",
    "Dormont - Memory of Puns":                 "Dormont - Act 4",
    "Dormont - Mystery Book":                   "Dormont - Act 4",

}

regions_to_locations = {

}
for location in location_region_map:
    location_table[location] = LocData(base_id+idx, location_region_map[location])
    idx += 1