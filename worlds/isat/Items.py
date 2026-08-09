from __future__ import annotations

import random
from typing import TYPE_CHECKING, Dict

from BaseClasses import Item, ItemClassification

from .Types import BaseId, InStarsAndTimeItem, ItemData, ItemType

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld

# Skills 1-240
# Items  241-341
# Weapons 342-402
# Armors 403-503


starting_items: Dict[str, ItemData] = {
    # Skills
    "Knife To Meet You": ItemData(BaseId.Skill + 11, ItemClassification.useful, ItemType.Skill),
    "Too Cleaver by Half": ItemData(BaseId.Skill + 12, ItemClassification.useful, ItemType.Skill),
    "Make Up The Time": ItemData(BaseId.Skill + 14, ItemClassification.useful, ItemType.Skill),
    "Turn It Up": ItemData(BaseId.Skill + 15, ItemClassification.useful, ItemType.Skill),
    "Memory of Self": ItemData(BaseId.Armor + 32, ItemClassification.useful, ItemType.Armor),
    "Siffrin's Knife": ItemData(BaseId.Weapon + 1, ItemClassification.useful, ItemType.Weapon),
    "Traveler's Hat": ItemData(BaseId.Armor + 1, ItemClassification.useful, ItemType.Armor),
    "Jolly Round Rondo": ItemData(BaseId.Skill + 32, ItemClassification.useful, ItemType.Skill),
    "Artsy Silent Burst": ItemData(BaseId.Skill + 33, ItemClassification.useful, ItemType.Skill),
    "Pretty Buffy Friend": ItemData(BaseId.Skill + 34, ItemClassification.useful, ItemType.Skill),
    "Super Sparkle Heal": ItemData(BaseId.Skill + 35, ItemClassification.useful, ItemType.Skill),
    "Memory of Mirabelle": ItemData(BaseId.Armor + 42, ItemClassification.useful, ItemType.Skill),
    "Shiny Rapier": ItemData(BaseId.Weapon + 3, ItemClassification.useful, ItemType.Weapon),
    "Big Bow": ItemData(BaseId.Armor + 3, ItemClassification.useful, ItemType.Armor),
    "SMASH!!!": ItemData(BaseId.Skill + 22, ItemClassification.useful, ItemType.Skill),
    "KABOOM!!!": ItemData(BaseId.Skill + 23, ItemClassification.useful, ItemType.Skill),
    "COME ON!!!": ItemData(BaseId.Skill + 24, ItemClassification.useful, ItemType.Skill),
    "YOUR TURN!!!": ItemData(BaseId.Skill + 27, ItemClassification.useful, ItemType.Skill),
    "Memory of Isabeau": ItemData(BaseId.Armor + 52, ItemClassification.useful, ItemType.Armor),
    "Crystal Knuckle": ItemData(BaseId.Weapon + 2, ItemClassification.useful, ItemType.Armor),
    "Rectangular Earrings": ItemData(BaseId.Armor + 2, ItemClassification.useful, ItemType.Armor),
    "Examine": ItemData(BaseId.Skill + 42, ItemClassification.useful, ItemType.Skill),
    "Scissors III": ItemData(BaseId.Skill + 43, ItemClassification.useful, ItemType.Skill),
    "Rock III": ItemData(BaseId.Skill + 44, ItemClassification.useful, ItemType.Skill),
    "Paper III": ItemData(BaseId.Skill + 45, ItemClassification.useful, ItemType.Skill),
    "Slow IV": ItemData(BaseId.Skill + 47, ItemClassification.useful, ItemType.Skill),
    "Memory of Odile": ItemData(BaseId.Armor + 62, ItemClassification.useful, ItemType.Skill),
    "Dense Book": ItemData(BaseId.Weapon + 4, ItemClassification.useful, ItemType.Weapon),
    "Geometric Glasses": ItemData(BaseId.Armor + 4, ItemClassification.useful, ItemType.Armor),
    "Thousand Blows Technique": ItemData(BaseId.Skill + 52, ItemClassification.useful, ItemType.Skill),
    "Aggression Boost Technique": ItemData(BaseId.Skill + 53, ItemClassification.useful, ItemType.Skill),
    "Fortress Building Technique": ItemData(BaseId.Skill + 54, ItemClassification.useful, ItemType.Skill),
    "Wolf Speed Technique": ItemData(BaseId.Skill + 55, ItemClassification.useful, ItemType.Skill),
    "Life Replenishing Technique": ItemData(BaseId.Skill + 56, ItemClassification.useful, ItemType.Skill),
    "Memory of Bonnie": ItemData(BaseId.Armor + 72, ItemClassification.useful, ItemType.Armor),
    "Frying Pan": ItemData(BaseId.Weapon + 5, ItemClassification.useful, ItemType.Weapon),
    "Round Hat": ItemData(BaseId.Armor + 5, ItemClassification.useful, ItemType.Armor),
    "Siffrin's Silver Coin": ItemData(BaseId.Item + 42, ItemClassification.progression, ItemType.Item),
}

level_items: Dict[str, ItemData] = {
    "Siffrin - Buy One Get One Three": ItemData(BaseId.Skill + 20, ItemClassification.useful, ItemType.Skill),
    "Siffrin - Done Heal": ItemData(BaseId.Skill + 16, ItemClassification.useful, ItemType.Skill),
    "Siffrin - In A While, Rockodile": ItemData(BaseId.Skill + 17, ItemClassification.useful, ItemType.Skill),
    "Siffrin - Regener-ade": ItemData(BaseId.Skill + 155, ItemClassification.useful, ItemType.Skill),
    "Siffrin - Rose Printed Glasses": ItemData(BaseId.Skill + 18, ItemClassification.useful, ItemType.Skill),
    "Siffrin - Tear You Apart": ItemData(BaseId.Skill + 157, ItemClassification.useful, ItemType.Skill),
    "Siffrin - Rock Bottom": ItemData(BaseId.Skill + 156, ItemClassification.useful, ItemType.Skill),
    "Mirabelle - Lovely Moving Cure": ItemData(BaseId.Skill + 36, ItemClassification.useful, ItemType.Skill),
    "Mirabelle - Shining Life": ItemData(BaseId.Skill + 37, ItemClassification.useful, ItemType.Skill),
    "Mirabelle - Mega Sparkle Heal": ItemData(BaseId.Skill + 39, ItemClassification.useful, ItemType.Skill),
    "Isabeau - SO WEAK!!!": ItemData(BaseId.Skill + 25, ItemClassification.useful, ItemType.Skill),
    "Isabeau - BREAK, BREAK!!!": ItemData(BaseId.Skill + 26, ItemClassification.useful, ItemType.Skill),
    "Isabeau - NOT OVER YET!!!": ItemData(BaseId.Skill + 28, ItemClassification.useful, ItemType.Skill),
    "Odile - Paper α V": ItemData(BaseId.Skill + 46, ItemClassification.useful, ItemType.Skill),
    "Odile - Craft Buff": ItemData(BaseId.Skill + 48, ItemClassification.useful, ItemType.Skill),
    "Odile - Craft Break": ItemData(BaseId.Skill + 49, ItemClassification.useful, ItemType.Skill),
}

dormont_items: Dict[str, ItemData] = {
    "First Issue": ItemData(BaseId.Weapon + 27, ItemClassification.useful, ItemType.Weapon),
    "Loving Fanmail": ItemData(BaseId.Item + 55, ItemClassification.progression, ItemType.Item),
    "Four-Pointed Leaf": ItemData(BaseId.Item + 47, ItemClassification.filler, ItemType.Item),
    "Bright Flower": ItemData(BaseId.Item + 43, ItemClassification.progression, ItemType.Item),
    "Bright Friendship Doodle": ItemData(BaseId.Item + 54, ItemClassification.filler, ItemType.Item),
    "Long Thingy-Thing": ItemData(BaseId.Item + 69, ItemClassification.progression, ItemType.Item),
    "Reminder Note": ItemData(BaseId.Item + 46, ItemClassification.filler, ItemType.Item),
    "Memory of Touch": ItemData(BaseId.Armor + 37, ItemClassification.filler, ItemType.Armor),
    "Memory of Fishing": ItemData(BaseId.Armor + 38, ItemClassification.useful, ItemType.Armor),
    "Memory of Defeat": ItemData(BaseId.Armor + 83, ItemClassification.useful, ItemType.Armor),
    "Memory of Memories": ItemData(BaseId.Armor + 87, ItemClassification.progression, ItemType.Armor),
    "Memory of Faith": ItemData(BaseId.Armor + 50, ItemClassification.useful, ItemType.Armor),
    "Holy Care Shield": ItemData(BaseId.Skill + 40, ItemClassification.progression, ItemType.Skill),
    "Memory of Puns": ItemData(BaseId.Armor + 55, ItemClassification.useful, ItemType.Armor),
    "Memory of Stargazing": ItemData(BaseId.Armor + 60, ItemClassification.useful, ItemType.Armor),
    "WE WILL WIN!!!": ItemData(BaseId.Skill + 29, ItemClassification.useful, ItemType.Skill),
    "Memory of Secret Quest": ItemData(BaseId.Armor + 70, ItemClassification.useful, ItemType.Armor),
    "Craft Break α": ItemData(BaseId.Skill + 50, ItemClassification.useful, ItemType.Skill),
    "Memory of Training": ItemData(BaseId.Armor + 80, ItemClassification.useful, ItemType.Armor),
    "Billion Blows Technique": ItemData(BaseId.Skill + 59, ItemClassification.filler, ItemType.Skill),
    "Stylish Bow": ItemData(BaseId.Armor + 16, ItemClassification.useful, ItemType.Armor),
    "Griddle Pan": ItemData(BaseId.Weapon + 32, ItemClassification.useful, ItemType.Weapon),
    "Your Dagger": ItemData(BaseId.Item + 12, ItemClassification.progression, ItemType.Item),
    "(Call Loop.)": ItemData(BaseId.Skill + 160, ItemClassification.filler, ItemType.Skill),
    "Stostorage Roomoom Openphrase": ItemData(BaseId.Misc + 3, ItemClassification.progression, ItemType.Variable),
    "Memory of Looping": ItemData(BaseId.Armor + 82, ItemClassification.useful, ItemType.Armor),
    "Loop's Silver Coin": ItemData(BaseId.Item + 62, ItemClassification.progression, ItemType.Item),
    "Memory of Family": ItemData(BaseId.Armor + 86, ItemClassification.useful, ItemType.Armor),
    "(Just attack.)": ItemData(BaseId.Skill + 13, ItemClassification.useful, ItemType.Skill),
    "Change Openphrase": ItemData(BaseId.Misc + 17, ItemClassification.progression, ItemType.Variable),
    "Saucepan": ItemData(BaseId.Weapon + 34, ItemClassification.useful, ItemType.Weapon),
    "Cast Iron Pan": ItemData(BaseId.Weapon + 35, ItemClassification.useful, ItemType.Weapon),
    "Memory of Emptiness": ItemData(BaseId.Armor + 88, ItemClassification.progression, ItemType.Armor),
    "(Rock.)": ItemData(BaseId.Skill + 183, ItemClassification.useful, ItemType.Skill),
    "(Paper.)": ItemData(BaseId.Skill + 184, ItemClassification.useful, ItemType.Skill),
    "(Scissors.)": ItemData(BaseId.Skill + 182, ItemClassification.useful, ItemType.Skill),
    "(Breathe.)": ItemData(BaseId.Skill + 185, ItemClassification.useful, ItemType.Skill),
    "(Heal.)": ItemData(BaseId.Skill + 186, ItemClassification.useful, ItemType.Skill),
}

entrance_items: Dict[str, ItemData] = {
    "Memory of Sadnesses": ItemData(BaseId.Armor + 34, ItemClassification.useful, ItemType.Armor),
    "Circle Key": ItemData(BaseId.Item + 22, ItemClassification.progression, ItemType.Item),
    "Bell Pendant": ItemData(BaseId.Item + 51, ItemClassification.progression, ItemType.Item),
    "Memory of Tonics": ItemData(BaseId.Armor + 63, ItemClassification.useful, ItemType.Armor),
}

floor_1_items: Dict[str, ItemData] = {
    "Memory of Barrels": ItemData(BaseId.Armor + 39, ItemClassification.useful, ItemType.Armor),
    "Memory of Pillars": ItemData(BaseId.Armor + 40, ItemClassification.useful, ItemType.Armor),
    "Teardrop Star Crest": ItemData(BaseId.Item + 32, ItemClassification.progression, ItemType.Item),
    "Egg Key": ItemData(BaseId.Item + 23, ItemClassification.progression, ItemType.Item),
    "Wok": ItemData(BaseId.Weapon + 33, ItemClassification.useful, ItemType.Weapon),
    "Needle Sword": ItemData(BaseId.Weapon + 20, ItemClassification.useful, ItemType.Weapon),
    "Sharpening Stone": ItemData(BaseId.Item + 50, ItemClassification.progression, ItemType.Item),
    "Drawn Card": ItemData(BaseId.Item + 53, ItemClassification.filler, ItemType.Item),
    "Broken Egg Key": ItemData(BaseId.Item + 24, ItemClassification.progression, ItemType.Item),
    "Pillow Hat": ItemData(BaseId.Armor + 24, ItemClassification.useful, ItemType.Armor),
    "Opaque Glasses": ItemData(BaseId.Item + 20, ItemClassification.useful, ItemType.Armor),
    "Memory of Keys": ItemData(BaseId.Armor + 33, ItemClassification.filler, ItemType.Armor),
}

floor_2_items: Dict[str, ItemData] = {
    "Memory of Snacks": ItemData(BaseId.Armor + 73, ItemClassification.useful, ItemType.Armor),
    "Crying Key": ItemData(BaseId.Item + 30, ItemClassification.progression, ItemType.Item),
    "Clock Star Crest": ItemData(BaseId.Item + 33, ItemClassification.progression, ItemType.Item),
    "Garden Scissors": ItemData(BaseId.Weapon + 9, ItemClassification.useful, ItemType.Weapon),
    "Rock Key": ItemData(BaseId.Item + 25, ItemClassification.progression, ItemType.Item),
    "Bonding Earring": ItemData(BaseId.Item + 60, ItemClassification.progression, ItemType.Item),
    "Heavy Book": ItemData(BaseId.Weapon + 26, ItemClassification.useful, ItemType.Weapon),
    "Paper Key": ItemData(BaseId.Item + 26, ItemClassification.progression, ItemType.Item),
    "Crumpled Poem": ItemData(BaseId.Item + 45, ItemClassification.filler, ItemType.Item),
    "Adorable Moving Shield": ItemData(BaseId.Skill + 38, ItemClassification.progression, ItemType.Skill),
    "Broken Doll": ItemData(BaseId.Item + 56, ItemClassification.filler, ItemType.Item),
    "Drop Earring": ItemData(BaseId.Armor + 12, ItemClassification.filler, ItemType.Armor),
    "Shiny Piece of Glass": ItemData(BaseId.Item + 44, ItemClassification.filler, ItemType.Item),
    "Scissors Key": ItemData(BaseId.Item + 27, ItemClassification.progression, ItemType.Item),
    "Memory of Learning": ItemData(BaseId.Armor + 45, ItemClassification.useful, ItemType.Armor),
}

floor_3_items: Dict[str, ItemData] = {
    "Memory of Promise": ItemData(BaseId.Armor + 74, ItemClassification.useful, ItemType.Armor),
    "Empty Key": ItemData(BaseId.Item + 31, ItemClassification.filler, ItemType.Item),
    "Papier-mâché Hands": ItemData(BaseId.Weapon + 16, ItemClassification.useful, ItemType.Weapon),
    "Lumpy Clay": ItemData(BaseId.Item + 48, ItemClassification.filler, ItemType.Item),
    "Massive Chain": ItemData(BaseId.Item + 52, ItemClassification.progression, ItemType.Item),
    "Mirror Picture": ItemData(BaseId.Item + 49, ItemClassification.filler, ItemType.Item),
    "Smiling Key": ItemData(BaseId.Item + 28, ItemClassification.progression, ItemType.Item),
    "Starry Hat": ItemData(BaseId.Armor + 10, ItemClassification.useful, ItemType.Armor),
    "Angry Key": ItemData(BaseId.Item + 29, ItemClassification.progression, ItemType.Item),
    "Short Gizmo-Gadget": ItemData(BaseId.Item + 58, ItemClassification.progression, ItemType.Item),
    "Double Star Crest": ItemData(BaseId.Item + 34, ItemClassification.progression, ItemType.Item),
    "Openphrase123 Openphrase": ItemData(BaseId.Misc + 56, ItemClassification.progression, ItemType.Variable),
    "KeyKnife": ItemData(BaseId.Item + 35, ItemClassification.progression, ItemType.Item),
    "Memory of Ghosts": ItemData(BaseId.Armor + 36, ItemClassification.filler, ItemType.Armor),
    "KnifeKey": ItemData(BaseId.Weapon + 12, ItemClassification.progression, ItemType.Weapon),
    "Memory of Change God": ItemData(BaseId.Armor + 44, ItemClassification.useful, ItemType.Armor),
    "Memory of Reflection": ItemData(BaseId.Armor + 53, ItemClassification.useful, ItemType.Armor),
    "Memory of First Strike": ItemData(BaseId.Armor + 65, ItemClassification.useful, ItemType.Armor),
}

the_end_items: Dict[str, ItemData] = {
    "Secret Ingredient": ItemData(BaseId.Item + 59, ItemClassification.progression, ItemType.Item),
    "Memory of Safe Rooms": ItemData(BaseId.Armor + 75, ItemClassification.useful, ItemType.Armor),
    "Memory of Butt Kicking": ItemData(BaseId.Armor + 43, ItemClassification.useful, ItemType.Armor),
    "Bomb": ItemData(BaseId.Item + 13, ItemClassification.useful, ItemType.Item),
    "Memory of Victory": ItemData(BaseId.Armor + 84, ItemClassification.useful, ItemType.Armor),
    "Memory of A Journey": ItemData(BaseId.Armor + 89, ItemClassification.useful, ItemType.Armor),
    "Eternal Snacks": ItemData(BaseId.Item + 61, ItemClassification.filler, ItemType.Item),
}

filler_items: Dict[str, ItemData] = {
    "Sour Tonic": ItemData(BaseId.Item + 2, ItemClassification.filler, ItemType.Item),
    "Super Sour Tonic": ItemData(BaseId.Item + 3, ItemClassification.filler, ItemType.Item),
    "Crafted Water": ItemData(BaseId.Item + 4, ItemClassification.filler, ItemType.Item),
    "Pepper Juice": ItemData(BaseId.Item + 5, ItemClassification.filler, ItemType.Item),
    "Ginger Juice": ItemData(BaseId.Item + 6, ItemClassification.filler, ItemType.Item),
    "Thyme Juice": ItemData(BaseId.Item + 7, ItemClassification.filler, ItemType.Item),
    "Sweet Tonic": ItemData(BaseId.Item + 9, ItemClassification.filler, ItemType.Item),
    "Super Sweet Tonic": ItemData(BaseId.Item + 10, ItemClassification.filler, ItemType.Item),
    "Salty Broth": ItemData(BaseId.Item + 11, ItemClassification.filler, ItemType.Item),
    "Memory of Skirmish": ItemData(BaseId.Item + 66, ItemClassification.filler, ItemType.Item),
    "Memory of Battle": ItemData(BaseId.Item + 67, ItemClassification.filler, ItemType.Item),
    "Memory of Conflict": ItemData(BaseId.Item + 68, ItemClassification.filler, ItemType.Item),
}

# This name could be confusing. TODO: Rename
SHUFFLED_ITEMS = {
    **level_items,
    **dormont_items,
    **entrance_items,
    **floor_1_items,
    **floor_2_items,
    **floor_3_items,
    **the_end_items,
}

ALL_ITEMS = {
    **starting_items,
    **SHUFFLED_ITEMS,
    **filler_items,
    "Goal Clear": ItemData(
        BaseId.Victory, ItemClassification.progression, ItemType.Achievement
    ),  # Dummy object with which to populate the ending achievement
}

# Create Item Table
ITEM_TABLE = {name: data.id for name, data in ALL_ITEMS.items()}


def get_random_filler_item_name(world: InStarsAndTimeWorld):
    return random.choice([name for name in filler_items])  # Temp


def create_item_with_correct_classification(world: InStarsAndTimeWorld, name: str) -> InStarsAndTimeItem:
    return InStarsAndTimeItem(name, ALL_ITEMS[name].classification, ALL_ITEMS[name].id, world.player)


def create_all_items(world: InStarsAndTimeWorld) -> None:
    itempool: list[Item] = [world.create_item(name) for name, data in SHUFFLED_ITEMS.items()]

    # Starting Items
    match world.options.starting_craft:
        case 0:
            for name in starting_items:
                world.push_precollected(world.create_item(name))
        case _:
            itempool += [world.create_item(name) for name, data in starting_items.items()]
            pass

    # Based off of APQuest Code
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items - 1  # Clear condition
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
