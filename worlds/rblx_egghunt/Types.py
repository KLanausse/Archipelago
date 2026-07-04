from enum import Enum
from typing import NamedTuple, Optional

from BaseClasses import Location, Item, ItemClassification

baseId = 76530952

class RobloxEggHuntLocation(Location):
    game = "Roblox Egg Hunt"

class RobloxEggHuntItem(Item):
    game = "Roblox Egg Hunt"

class ItemData(NamedTuple):
    id: Optional[int]
    classification: Optional[ItemClassification]