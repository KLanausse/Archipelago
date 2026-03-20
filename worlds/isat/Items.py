from __future__ import annotations

import random
from typing import Dict, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .Types import ItemData, InStarsAndTimeItem, BaseId, ItemType

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld

# Skills 1-240
# Items  241-341
# Weapons 342-402
# Armors 403-503



starting_items: Dict[str, ItemData] = {
    # Skills
    "Knife To Meet You":            ItemData(BaseId.Skill+11,   ItemClassification.useful,      ItemType.Skill),
    "Too Cleaver by Half":          ItemData(BaseId.Skill+12,   ItemClassification.useful,      ItemType.Skill),
    "Make Up The Time":             ItemData(BaseId.Skill+14,   ItemClassification.useful,      ItemType.Skill),
    "Turn It Up":                   ItemData(BaseId.Skill+15,   ItemClassification.useful,      ItemType.Skill),
    "Memory of Self":               ItemData(BaseId.Armor+32,   ItemClassification.useful,      ItemType.Armor),
    "Siffrin's Knife":              ItemData(BaseId.Weapon+1,   ItemClassification.useful,      ItemType.Weapon),
    "Traveler's Hat":               ItemData(BaseId.Armor+1,    ItemClassification.useful,      ItemType.Armor),
    "Jolly Round Rondo":            ItemData(BaseId.Skill+32,   ItemClassification.useful,      ItemType.Skill),
    "Artsy Silent Burst":           ItemData(BaseId.Skill+33,   ItemClassification.useful,      ItemType.Skill),
    "Pretty Buffy Friend":          ItemData(BaseId.Skill+34,   ItemClassification.useful,      ItemType.Skill),
    "Super Sparkle Heal":           ItemData(BaseId.Skill+35,   ItemClassification.useful,      ItemType.Skill),
    "Memory of Mirabelle":          ItemData(BaseId.Skill+42,   ItemClassification.useful,      ItemType.Skill),
    "Shiny Rapier":                 ItemData(BaseId.Weapon+3,   ItemClassification.useful,      ItemType.Weapon),
    "Big Bow":                      ItemData(BaseId.Armor+3,    ItemClassification.useful,      ItemType.Armor),
    "SMASH!!!":                     ItemData(BaseId.Skill+22,   ItemClassification.useful,      ItemType.Skill),
    "KABOOM!!!":                    ItemData(BaseId.Skill+23,   ItemClassification.useful,      ItemType.Skill),
    "COME ON!!!":                   ItemData(BaseId.Skill+24,   ItemClassification.useful,      ItemType.Skill),
    "YOUR TURN!!!":                 ItemData(BaseId.Skill+27,   ItemClassification.useful,      ItemType.Skill),
    "Memory of Isabeau":            ItemData(BaseId.Armor+52,   ItemClassification.useful,      ItemType.Armor),
    "Crystal Knuckle":              ItemData(BaseId.Weapon+2,   ItemClassification.useful,      ItemType.Armor),
    "Rectangular Earrings":         ItemData(BaseId.Armor+2,    ItemClassification.useful,      ItemType.Armor),
    "Examine":                      ItemData(BaseId.Skill+42,   ItemClassification.useful,      ItemType.Skill),
    "Scissors III":                 ItemData(BaseId.Skill+43,   ItemClassification.useful,      ItemType.Skill),
    "Rock III":                     ItemData(BaseId.Skill+44,   ItemClassification.useful,      ItemType.Skill),
    "Paper III":                    ItemData(BaseId.Skill+45,   ItemClassification.useful,      ItemType.Skill),
    "Slow IV":                      ItemData(BaseId.Skill+47,   ItemClassification.useful,      ItemType.Skill),
    "Memory of Odile":              ItemData(BaseId.Armor+62,   ItemClassification.useful,      ItemType.Skill),
    "Dense Book":                   ItemData(BaseId.Weapon+4,   ItemClassification.useful,      ItemType.Weapon),
    "Geometric Glasses":            ItemData(BaseId.Armor+4,    ItemClassification.useful,      ItemType.Armor),
    "Thousand Blows Technique":     ItemData(BaseId.Skill+52,   ItemClassification.useful,      ItemType.Skill),
    "Aggression Boost Technique":   ItemData(BaseId.Skill+53,   ItemClassification.useful,      ItemType.Skill),
    "Fortress Building Technique":  ItemData(BaseId.Skill+54,   ItemClassification.useful,      ItemType.Skill),
    "Wolf Speed Technique":         ItemData(BaseId.Skill+55,   ItemClassification.useful,      ItemType.Skill),
    "Life Replenishing Technique":  ItemData(BaseId.Skill+56,   ItemClassification.useful,      ItemType.Skill),
    "Memory of Bonnie":             ItemData(BaseId.Armor+72,   ItemClassification.useful,      ItemType.Armor),
    "Frying Pan":                   ItemData(BaseId.Weapon+5,   ItemClassification.useful,      ItemType.Weapon),
    "Round Hat":                    ItemData(BaseId.Armor+5,    ItemClassification.useful,      ItemType.Armor),
    "Siffrin's Silver Coin":        ItemData(BaseId.Item+42,    ItemClassification.progression, ItemType.Item)
}

level_items: Dict[str, ItemData] = {
    "Siffrin - Buy One Get One Three":  ItemData(BaseId.Skill+20,   ItemClassification.useful,  ItemType.Skill),
    "Siffrin - Done Heal":              ItemData(BaseId.Skill+16,   ItemClassification.useful,  ItemType.Skill),
    "Siffrin - In A While, Rockodile":  ItemData(BaseId.Skill+17,   ItemClassification.useful,  ItemType.Skill),
    "Siffrin - Regener-ade":            ItemData(BaseId.Skill+155,  ItemClassification.useful,  ItemType.Skill),
    "Siffrin - Rose Printed Glasses":   ItemData(BaseId.Skill+18,   ItemClassification.useful,  ItemType.Skill),
    "Siffrin - Tear You Apart":         ItemData(BaseId.Skill+157,  ItemClassification.useful,  ItemType.Skill),
    "Siffrin - Rock Bottom":            ItemData(BaseId.Skill+156,  ItemClassification.useful,  ItemType.Skill),
    "Mirabelle - Lovely Moving Cure":   ItemData(BaseId.Skill+36,   ItemClassification.useful,  ItemType.Skill),
    "Mirabelle - Shining Life":         ItemData(BaseId.Skill+37,   ItemClassification.useful,  ItemType.Skill),
    "Mirabelle - Mega Sparkle Heal":    ItemData(BaseId.Skill+39,   ItemClassification.useful,  ItemType.Skill),
    "Isabeau - SO WEAK!!!":             ItemData(BaseId.Skill+25,   ItemClassification.useful,  ItemType.Skill),
    "Isabeau - BREAK, BREAK!!!":        ItemData(BaseId.Skill+26,   ItemClassification.useful,  ItemType.Skill),
    "Isabeau - NOT OVER YET!!!":        ItemData(BaseId.Skill+28,   ItemClassification.useful,  ItemType.Skill),
    "Odile - Paper α V":                ItemData(BaseId.Skill+46,   ItemClassification.useful,  ItemType.Skill),
    "Odile - Craft Buff":               ItemData(BaseId.Skill+48,   ItemClassification.useful,  ItemType.Skill),
    "Odile - Craft Break":              ItemData(BaseId.Skill+49,   ItemClassification.useful,  ItemType.Skill),
}

dormont_items: Dict[str, ItemData] = {
    "Bright Flower":        ItemData(BaseId.Item+43, ItemClassification.filler, ItemType.Item),
    "Reminder Note":        ItemData(BaseId.Item+46, ItemClassification.filler, ItemType.Item),
    "Four-Pointed Leaf":    ItemData(BaseId.Item+47, ItemClassification.filler, ItemType.Item),
}

entrance_items: Dict[str, ItemData] = {
    "Circle Key": ItemData(BaseId.Item+22,  ItemClassification.progression, ItemType.Item)
}

floor_1_items: Dict[str, ItemData] = {
    "Teardrop Star Crest (Teardrop)":  ItemData(BaseId.Item+32, ItemClassification.progression, ItemType.Item),
    "Egg Key":              ItemData(BaseId.Item+23, ItemClassification.progression, ItemType.Item),
    "Opaque Glasses":       ItemData(BaseId.Item+20, ItemClassification.useful, ItemType.Item),
}

filler_items: Dict[str, ItemData] = {
    "Sour Tonic":           ItemData(BaseId.Item+2,     ItemClassification.filler, ItemType.Item),
    "Super Sour Tonic":     ItemData(BaseId.Item+3,     ItemClassification.filler, ItemType.Item),
    "Crafted Water":        ItemData(BaseId.Item+4,     ItemClassification.filler, ItemType.Item),
    "Pepper Juice":         ItemData(BaseId.Item+5,     ItemClassification.filler, ItemType.Item),
    "Ginger Juice":         ItemData(BaseId.Item+6,     ItemClassification.filler, ItemType.Item),
    "Thyme Juice":          ItemData(BaseId.Item+7,     ItemClassification.filler, ItemType.Item),

    "Sweet Tonic":          ItemData(BaseId.Item+9,     ItemClassification.filler, ItemType.Item),
    "Super Sweet Tonic":    ItemData(BaseId.Item+10,    ItemClassification.filler, ItemType.Item),
    "Salty Broth":          ItemData(BaseId.Item+11,    ItemClassification.filler, ItemType.Item),

}

# This name could be confusing. TODO: Rename
ALL_ITEMS = {
    **starting_items,
    **level_items,
    **entrance_items,
    **floor_1_items,
    **filler_items
}
SHUFFLED_ITEMS = {
    **level_items,
    **entrance_items,
    **floor_1_items,
    **filler_items
}

# Create Item Table
ITEM_TABLE = {name: data.id for name, data in ALL_ITEMS.items()}

def get_random_filler_item_name(world: InStarsAndTimeWorld):
    return random.choice([name for name in filler_items]) # Temp

def create_item_with_correct_classification(world: InStarsAndTimeWorld, name: str) -> InStarsAndTimeItem:
    return InStarsAndTimeItem(name, ALL_ITEMS[name].classification, ALL_ITEMS[name].id, world.player)

def create_all_items(world: InStarsAndTimeWorld) -> None:
    itempool: list[Item] = [world.create_item(name) for name, data in SHUFFLED_ITEMS.items()]

    # Based off of APQuest Code
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

    # Starting Items
    for name in starting_items:
        world.push_precollected(world.create_item(name))