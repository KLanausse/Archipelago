import logging
from typing import Dict

from BaseClasses import Item, ItemClassification

from .Types import ItemData, InStarsAndTimeItem, BaseId, ItemType

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

filler_items: Dict[str, ItemData] = {
    "Sour Tonic":           ItemData(BaseId.Item+2,     ItemClassification.filler, ItemType.Item, 5),
    "Super Sour Tonic":     ItemData(BaseId.Item+3,     ItemClassification.filler, ItemType.Item, 5),
    "Crafted Water":        ItemData(BaseId.Item+4,     ItemClassification.filler, ItemType.Item, 5),
    "Pepper Juice":         ItemData(BaseId.Item+5,     ItemClassification.filler, ItemType.Item, 5),
    "Ginger Juice":         ItemData(BaseId.Item+6,     ItemClassification.filler, ItemType.Item, 5),
    "Thyme Juice":          ItemData(BaseId.Item+7,     ItemClassification.filler, ItemType.Item, 5),

    "Sweet Tonic":          ItemData(BaseId.Item+9,     ItemClassification.filler, ItemType.Item, 5),
    "Super Sweet Tonic":    ItemData(BaseId.Item+10,    ItemClassification.filler, ItemType.Item, 5),
    "Salty Broth":          ItemData(BaseId.Item+11,    ItemClassification.filler, ItemType.Item, 5),

}

# This name could be confusing. TODO: Rename
all_items = {
    **starting_items
}

# Create Item Table
item_table = {name: data.id for name, data in all_items.items()}