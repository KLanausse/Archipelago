from enum import Enum
from typing import NamedTuple, Optional

from BaseClasses import Location, Item, ItemClassification

class BaseId(int):
    Base = 1677310
    Skill = 1677310
    Item = 1677310 + 240
    Weapon = 1677310 + 240 + 100
    Armor = 1677310 + 240 + 100 + 60
    Misc = 1677310 + 240 + 100 + 60 + 100

class ItemType(Enum):
    Skill  = 0
    Item   = 1
    Weapon = 2
    Armor  = 3
    Variable = 4
    Switch = 5
    Achievement = 6

class InStarsAndTimeLocation(Location):
    game = "In Stars And Time"

class InStarsAndTimeItem(Item):
    game = "In Stars And Time"

class LocData(NamedTuple):
    id: Optional[int]
    act: Optional[str] = "Act 1"
    # region: Optional[str]
    rule_type: Optional[str] = None
    rule_args: Optional[any] = None


class ItemData(NamedTuple):
    id: Optional[int]
    classification: Optional[ItemClassification]
    type: Optional[ItemType]