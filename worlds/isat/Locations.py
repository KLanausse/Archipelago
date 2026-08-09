from __future__ import annotations

from typing import TYPE_CHECKING, Dict

from BaseClasses import ItemClassification, Location
from rule_builder.rules import (  # rule_builder is new to Archi 0.6.7 - misch13vous
    And,
    Has,
    HasAll,
    HasAny,
    Rule,
    True_,
)

from .Types import BaseId, LocData

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld


class InStarsAndTimeLocation(Location):
    game = "In Stars and Time"


# Location IDs should match their item counterpart. If there is none associated, use BaseId.Misc
# TODO: Most of these locations don't have their rules properly set. Review each location and set them.
level_table: Dict[str, LocData] = {  # Levels
    "Siffrin - Buy One Get One Three": LocData(BaseId.Skill + 20, "Floor 1"),
    "Siffrin - Done Heal": LocData(BaseId.Skill + 16, "Floor 1"),
    "Siffrin - In A While, Rockodile": LocData(BaseId.Skill + 17, "Floor 1"),
    "Siffrin - Regener-ade": LocData(BaseId.Skill + 155, "Floor 1"),
    "Siffrin - Rose Printed Glasses": LocData(BaseId.Skill + 18, "Floor 1"),
    "Siffrin - Tear You Apart": LocData(BaseId.Skill + 157, "Floor 1"),
    "Siffrin - Rock Bottom": LocData(BaseId.Skill + 156, "Floor 1"),
    "Mirabelle - Lovely Moving Cure": LocData(BaseId.Skill + 36, "Floor 1"),
    "Mirabelle - Shining Life": LocData(BaseId.Skill + 37, "Floor 1"),
    "Mirabelle - Mega Sparkle Heal": LocData(BaseId.Skill + 39, "Floor 1"),
    "Isabeau - SO WEAK!!!": LocData(BaseId.Skill + 25, "Floor 1"),
    "Isabeau - BREAK, BREAK!!!": LocData(BaseId.Skill + 26, "Floor 1"),
    "Isabeau - NOT OVER YET!!!": LocData(BaseId.Skill + 28, "Floor 1"),
    "Odile - Paper α V": LocData(BaseId.Skill + 46, "Floor 1"),
    "Odile - Craft Buff": LocData(BaseId.Skill + 48, "Floor 1"),
    "Odile - Craft Break": LocData(BaseId.Skill + 49, "Floor 1"),
}

dormont_table: Dict[str, LocData] = {
    "Dormont - Castle-Loving One's Sidequest": LocData(BaseId.Weapon + 27, "Last Issue"),
    "Dormont - Stylish One's Sidequest": LocData(BaseId.Item + 55, "Stylish One"),
    "Dormont - Sky-Loving Kid": LocData(BaseId.Item + 47, "Default"),
    "Dormont - Flower Growing One": LocData(BaseId.Item + 43, "Default"),
    "Dormont - Drawing Kid": LocData(BaseId.Item + 54, "Default"),
    "Dormont - Blind One's House": LocData(BaseId.Item + 69, "Openphrase", Has("Change Openphrase")),
    "Dormont - Reminder Note": LocData(BaseId.Item + 46, "Default"),
    "Dormont - Memory of Touch": LocData(BaseId.Armor + 37, "Confession"),
    "Dormont - Memory of Fishing": LocData(BaseId.Armor + 38, "Floor 1"),
    "Dormont - Memory of Defeat": LocData(BaseId.Armor + 83, "King"),
    "Dormont - Memory of Memories": LocData(BaseId.Armor + 87, "Betrayed"),
    "Dormont - Mirabelle's Friendquest": LocData(BaseId.Armor + 50, "Mirabelle"),
    "Dormont - Memory of Puns": LocData(BaseId.Armor + 55, "Betrayed"),
    "Dormont - Isabeau's Friendquest": LocData(BaseId.Armor + 60, "Loved"),
    "Dormont - Odile's Friendquest": LocData(BaseId.Armor + 70, "Odile"),
    "Dormont - Bonnie's Friendquest": LocData(BaseId.Armor + 80, "Victory"),
    "Dormont - Gifted Fanmail": LocData(BaseId.Armor + 16, "Floor 2", Has("Loving Fanmail")),
    "Dormont - Beautiful One's Cupboard": LocData(BaseId.Weapon + 32, "Default"),
    "Dormont - Tutorial Kid Victory": LocData(BaseId.Misc + 1, "Default"),
    "Dormont - Tutorial Kid Clean Sweep": LocData(BaseId.Misc + 2, "Default"),
    "Dormont - Warning! Sharp!": LocData(BaseId.Item + 12, "Floor 1"),
    "Dormont - Call Loop": LocData(BaseId.Skill + 160, "Floor 1"),
    "Dormont - Shopkeeper's Openphrase": LocData(BaseId.Misc + 3, "Shopkeeper"),
    "Dormont - Mystery Book": LocData(BaseId.Misc + 4, "Default", Has("Memory of Memories")),
    "Dormont - Bonnie Flower": LocData(BaseId.Misc + 5, "Default", Has("Bright Flower")),
    "Dormont - Isabeau Flower": LocData(BaseId.Misc + 6, "Default", Has("Bright Flower")),
    "Dormont - Mirabelle Flower": LocData(BaseId.Misc + 7, "Default", Has("Bright Flower")),
    "Dormont - Odile Flower": LocData(BaseId.Misc + 8, "Default", Has("Bright Flower")),
    "Dormont - No thanks, stardust!": LocData(
        BaseId.Misc + 9, "Floor 1", HasAny("Bright Flower", "Four-Pointed Leaf", "Loving Fanmail")
    ),
    "Dormont - What was that about...?": LocData(BaseId.Misc + 10, "Incident"),
    # "Dormont - Loop Flower": LocData(BaseId.Misc+11,     "Act 2", "has", "Bright Flower"),
    "Dormont - Welcome to the show!": LocData(BaseId.Misc + 12, "Default"),
    "Dormont - Encore!": LocData(BaseId.Armor + 82, "Victory"),
    "Dormont - Loop Battle": LocData(BaseId.Misc + 13, "Floor 1", Has("Loop's Silver Coin")),
    "Dormont - Loop's Coin": LocData(BaseId.Item + 62, "Two Hats"),
    "Dormont - In this moment...": LocData(BaseId.Armor + 86, "Loved"),
    "Dormont - ...You are loved.": LocData(BaseId.Misc + 14, "Loved"),
    "Dormont - Nostalgie": LocData(BaseId.Skill + 13, "Betrayed"),
    "Dormont - IS THIS IT?": LocData(BaseId.Misc + 15, "Wish Craft"),
    "Dormont - Here's some change": LocData(BaseId.Misc + 16, "Incident"),
    "Dormont - Memory of Emptiness": LocData(BaseId.Armor + 88, "Favor Tree"),
}

entrance_table: Dict[str, LocData] = {
    "Entrance - Main Room - Circle Key": LocData(BaseId.Item + 22, "Default"),
    "Entrance - Storage Room - Vial 1": LocData(BaseId.Misc + 18, "Default"),
    "Entrance - Storage Room - Vial 2": LocData(BaseId.Misc + 19, "Default"),
    "Entrance - Storage Room - Vial 3": LocData(BaseId.Misc + 20, "Default"),
    "Entrance - Storage Room - Vial 4": LocData(BaseId.Misc + 21, "Default"),
    "Entrance - Jackpot!": LocData(BaseId.Misc + 22, "Default"),
    "Entrance - Storage Room - Closet": LocData(BaseId.Item + 51, "Default"),
    "Entrance - Memory of Tonics": LocData(BaseId.Armor + 63, "Floor 1"),
}

floor_1_table: Dict[str, Dict[str, LocData]] = {
    "Main Room": {
        "Floor 1 - Memory of Barrels": LocData(BaseId.Armor + 39, "Floor 1"),
        "Floor 1 - Memory of Pillars": LocData(BaseId.Armor + 40, "Floor 1"),
        "Floor 1 - Locked Storage Room - Vial 1": LocData(
            BaseId.Misc + 23, "Floor 1", Has("Stostorage Roomoom Openphrase")
        ),
        "Floor 1 - Locked Storage Room - Vial 2": LocData(
            BaseId.Misc + 24, "Floor 1", Has("Stostorage Roomoom Openphrase")
        ),
        "Floor 1 - Nostalgie": LocData(BaseId.Item + 32, "Floor 1"),
        "Floor 1 - Armory - Sword Rack": LocData(BaseId.Weapon + 20, "Floor 1"),
        "Floor 1 - Armory - Vial": LocData(BaseId.Misc + 29, "Floor 1"),
        "Floor 1 - Armory - Forge": LocData(BaseId.Item + 50, "Floor 1"),
        "Floor 1 - Calamité": LocData(BaseId.Misc + 31, "Floor 1", Has("Broken Egg Key")),
        "Floor 1 - Did you see that?": LocData(BaseId.Misc + 32, "Floor 1", HasAny("Egg Key", "Broken Egg Key")),
    },
    "Storage Room": {
        "Floor 1 - Locked Storage Room - Vial 1": LocData(
            BaseId.Misc + 25, "Floor 1", Has("Stostorage Roomoom Openphrase")
        ),
        "Floor 1 - Locked Storage Room - Vial 2": LocData(
            BaseId.Misc + 26, "Floor 1", Has("Stostorage Roomoom Openphrase")
        ),
    },
    "Kitchen": {
        "Floor 1 - Kitchen - Spice Rack": LocData(BaseId.Misc + 27, "Floor 1", Has("Teardrop Star Crest")),
        "Floor 1 - Kitchen - Vial": LocData(BaseId.Misc + 28, "Floor 1", Has("Teardrop Star Crest")),
        "Floor 1 - Kitchen - Closet": LocData(BaseId.Item + 23, "Floor 1", Has("Teardrop Star Crest")),
        "Floor 1 - Kitchen - Sink": LocData(BaseId.Weapon + 33, "Floor 1", Has("Teardrop Star Crest")),
    },
    "Left Hallway": {
        "Floor 1 - Bedroom - Closet": LocData(BaseId.Item + 53, "Floor 1", Has("Egg Key")),
        "Floor 1 - Bedroom - Drawer": LocData(BaseId.Item + 24, "Floor 1", Has("Egg Key")),
        "Floor 1 - Bedroom - Bed": LocData(BaseId.Armor + 24, "Floor 1", Has("Egg Key")),
        "Floor 1 - Candle Room - Closet": LocData(BaseId.Item + 20, "Floor 1", Has("Egg Key")),
        "Floor 1 - Candle Room - Vial": LocData(BaseId.Misc + 30, "Floor 1", Has("Egg Key")),
        "Floor 1 - Memory of Keys": LocData(BaseId.Armor + 33, "Floor 1", Has("Egg Key")),
    },
}

floor_2_table: Dict[str, Dict[str, LocData]] = {
    "Main Room": {
        "Floor 2 - Memory of Snacks": LocData(BaseId.Armor + 73, "Floor 2"),
        "Floor 2 - Classroom - Notebook": LocData(
            BaseId.Item + 30, "Floor 3", HasAll("Smiling Key", "Double Star Crest")
        ),
        "Floor 2 - Classroom - Vial": LocData(BaseId.Misc + 33, "Floor 2"),
        "Floor 2 - Nostalgie": LocData(BaseId.Item + 33, "Floor 2"),
        "Floor 2 - Garden Room - Closet": LocData(BaseId.Weapon + 9, "Floor 2"),
        "Floor 2 - Garden Room - Vial": LocData(BaseId.Misc + 34, "Floor 2"),
        "Floor 2 - Head Housemaiden's Office - Desk": LocData(BaseId.Item + 25, "Floor 2"),
        "Floor 2 - Accablement & Abattement": LocData(BaseId.Misc + 39, "Floor 2", Has("Scissors Key")),
        "Floor 2 - Memory of Learning": LocData(BaseId.Armor + 45, "Loved"),
    },
    "Library": {
        "Floor 2 - Partner Seeking One": LocData(BaseId.Item + 60, "Floor 2", Has("Rock Key")),
        "Floor 2 - Library - Vial": LocData(BaseId.Misc + 35, "Floor 2", Has("Rock Key")),
        "Floor 2 - Library - Book": LocData(BaseId.Weapon + 26, "Floor 2", Has("Rock Key")),
        "Floor 2 - Library - Bookshelf": LocData(BaseId.Item + 26, "Floor 2", Has("Rock Key")),
        "Floor 2 - Library - Poem": LocData(BaseId.Item + 45, "Floor 2", Has("Rock Key")),
        "Floor 2 - Secret Library - Bookshelf": LocData(BaseId.Skill + 38, "Library"),
    },
    "Crest Locked": {
        "Floor 2 - Infirmary - Vial": LocData(BaseId.Misc + 36, "Floor 2", HasAll("Paper Key", "Clock Star Crest")),
        "Floor 2 - Infirmary - Closet": LocData(BaseId.Item + 56, "Floor 2", HasAll("Paper Key", "Clock Star Crest")),
        "Floor 2 - Infirmary - Bed": LocData(BaseId.Armor + 12, "Floor 2", HasAll("Paper Key", "Clock Star Crest")),
        "Floor 2 - Trap Room - Counter": LocData(BaseId.Item + 27, "Floor 2", HasAll("Paper Key", "Clock Star Crest")),
    },
    "Break Room": {
        "Floor 2 - Locked Break Room - Dresser": LocData(
            BaseId.Misc + 37, "Floor 2", HasAll("Paper Key", "Openphrase123 Openphrase")
        ),
        "Floor 2 - Locked Break Room - Vial": LocData(
            BaseId.Misc + 38, "Floor 2", HasAll("Paper Key", "Openphrase123 Openphrase")
        ),
        "Floor 2 - Locked Break Room - Broken Vial": LocData(
            BaseId.Item + 44, "Floor 2", HasAll("Paper Key", "Openphrase123 Openphrase")
        ),
    },
}

floor_3_table: Dict[str, Dict[str, LocData]] = {
    "Main Room": {
        "Floor 3 - Memory of Promise": LocData(BaseId.Armor + 74, "Victory"),
        "Floor 3 - Best idea you've ever had!": LocData(BaseId.Misc + 48, "Floor 3"),
        "Floor 3 - Main Room - Key": LocData(BaseId.Item + 31, "Floor 3"),
        "Floor 3 - Pottery Room - Closet": LocData(BaseId.Misc + 49, "Floor 3"),
        "Floor 3 - Pottery Room - Shelf": LocData(BaseId.Weapon + 16, "Floor 3"),
        "Floor 3 - Pottery Room - Clay": LocData(BaseId.Item + 48, "Floor 3"),
        "Floor 3 - Break Room - Vial": LocData(BaseId.Misc + 50, "Floor 3"),
        "Floor 3 - Break Room - Chain": LocData(BaseId.Item + 52, "Floor 3"),
        "Floor 3 - Secret Room - Drawer": LocData(BaseId.Misc + 51, "Floor 3"),
        "Floor 3 - Mirror Room - Mirror": LocData(BaseId.Item + 49, "Floor 3"),
        "Floor 3 - Mirror Room - Key": LocData(BaseId.Item + 28, "Floor 3"),
        "Floor 3 - Nostalgie": LocData(BaseId.Item + 34, "Floor 3", Has("Angry Key")),
        "Floor 3 - Memory of Ghosts": LocData(
            BaseId.Armor + 36, "Floor 3", HasAll("Smiling Key", "Crying Key", "Double Star Crest", "Egg Key")
        ),
        "Floor 3 - Memory of KnifeKey": LocData(
            BaseId.Weapon + 12, "Floor 3", HasAll("KeyKnife", "Sharpening Stone", "Clock Star Crest")
        ),
        "Floor 3 - Memory of Reflection": LocData(BaseId.Armor + 53, "Floor 3"),
        "Floor 3 - Memory of First Strike": LocData(BaseId.Armor + 65, "Floor 3"),
    },
    "Crest Locked": {
        "Floor 3 - Star Room - Drawer": LocData(
            BaseId.Armor + 10, "Floor 3", HasAll("Smiling Key", "Memory of Memories")
        ),
        "Floor 3 - Poem Room - Vial": LocData(BaseId.Misc + 55, "Floor 3", Has("Double Star Crest")),
        "Floor 3 - Poem Room - Openphrase": LocData(BaseId.Misc + 56, "Floor 3", Has("Double Star Crest")),
    },
    "Left Hallway": {
        "Floor 3 - Change Room - Vial 1": LocData(BaseId.Misc + 52, "Floor 3", Has("Smiling Key")),
        "Floor 3 - Change Room - Vial 2": LocData(BaseId.Misc + 53, "Floor 3", Has("Smiling Key")),
        "Floor 3 - Change Room - Closet": LocData(BaseId.Item + 29, "Floor 3", Has("Smiling Key")),
        "Floor 3 - Mirabelle's Dorm - Vial": LocData(BaseId.Misc + 54, "Floor 3", Has("Smiling Key")),
        "Floor 3 - Mirabelle's Dorm - Closet": LocData(BaseId.Item + 58, "Floor 3", Has("Smiling Key")),
        "Floor 3 - Prayer Room - Statue": LocData(
            BaseId.Item + 35, "Floor 3", HasAll("Smiling Key", "Crying Key", "Double Star Crest")
        ),
        "Floor 3 - Memory of Change God": LocData(
            BaseId.Armor + 44, "Mirabelle", HasAll("Smiling Key", "Crying Key", "Double Star Crest")
        ),
    },
}

the_end_table: Dict[str, LocData] = {
    "The End - Claude": LocData(BaseId.Item + 59, "King", Has("Smiling Key")),
    "The End - Memory of Safe Rooms": LocData(BaseId.Armor + 75, "King"),
    "The End - Memory of Butt Kicking": LocData(BaseId.Armor + 43, "King"),
    "The End - Memory of Bomb": LocData(
        BaseId.Item + 13, "King", HasAll("Smiling Key", "Short Gizmo-Gadget", "Long Thingy-Thing", "Secret Ingredient")
    ),
    "The End - The King": LocData(BaseId.Armor + 84, "King", HasAny("Adorable Moving Shield", "Holy Care Shield")),
    "The End - 1000 ways to die": LocData(BaseId.Misc + 65, "King", Has("Your Dagger")),
    "The End - King Flower": LocData(BaseId.Misc + 66, "Victory", Has("Bright Flower")),
    # "The End - Head Housemaiden Flower":    LocData(BaseId.Misc+67),
    "The End - Your favorite play": LocData(BaseId.Misc + 68, "Victory", Has("Bright Flower")),
    "The End - Memory of A Journey": LocData(BaseId.Armor + 89, "Finale"),
    "The End - Epilogue": LocData(BaseId.Misc + 69, "Finale"),
    "The End - Eternal Snacks": LocData(BaseId.Item + 61, "Finale"),
    "The End - Aaaaaand SCENE!!!": LocData(BaseId.Misc + 70, "Finale"),
}


all_locations: Dict[str, LocData] = {
    **level_table,
    **dormont_table,
    **entrance_table,
    **floor_1_table["Main Room"],
    **floor_1_table["Storage Room"],
    **floor_1_table["Kitchen"],
    **floor_1_table["Left Hallway"],
    **floor_2_table["Main Room"],
    **floor_2_table["Library"],
    **floor_2_table["Crest Locked"],
    **floor_2_table["Break Room"],
    **floor_3_table["Main Room"],
    **floor_3_table["Crest Locked"],
    **floor_3_table["Left Hallway"],
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

    for idx, region_table in enumerate([floor_1_table, floor_2_table, floor_3_table]):
        for sub_region in region_table:
            region_name = f"Floor {idx + 1}" if sub_region == "Main Room" else f"Floor {idx + 1} - {sub_region}"
            create_location(world, region_name, region_table[sub_region])

    create_location(world, "The End", the_end_table)


def create_events(world: InStarsAndTimeWorld) -> None:
    pass
