from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld

region_names = [
    # Village
    "Dormont",

    # Castle
    "Entrance",
    "Floor 1 - Main Room" # 017 Locked by Circle Key
    "Floor 1 - Armory",
    "Floor 1 - Left Hallway" # 078 Locked by Egg Key
    "Floor 1 - Candle Dorm", # HAS OPAQUE GLASSES
    "Floor 1 - Writing Dorm",
    
    "Floor 1 - Right Hallway",
]


def create_and_connect_regions(world: InStarsAndTimeWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: InStarsAndTimeWorld) -> None:

    regions = [Region(name, world.player, world.multiworld) for name in region_names]
    world.multiworld.regions += regions

def connect_regions(world: InStarsAndTimeWorld) -> None:
    dormont = world.get_region("Dormont")
    entrance = world.get_region("Entrance")
    floor_1 = world.get_region("Floor 1 - Main Room")
    floor_2 = world.get_region("Floor 2 - Main Room")
    floor_3 = world.get_region("Floor 3 - Main Room")
    the_end = world.get_region("The End")

    # One Ways.
    dormont_to_entrance = Entrance(world.player, "Dormont to Entrance", parent=dormont)
    dormont.exits.append(dormont_to_entrance)
    dormont_to_entrance.connect(entrance)

    entrance.connect(floor_1, "Entrance to Floor 1", lambda state: state.has("Circle Key", world.player))
    floor_1.connect(floor_2, "Floor 1 to Floor 1", lambda state: state.has("Broken Egg Key", world.player))
    floor_2.connect(floor_3, "Floor 2 to Floor 1", lambda state: state.has("Scissors Key", world.player))
    floor_3.connect(the_end, "Floor 3 to The End", lambda state: state.has("Knife Key", world.player))

    # An even easier way is to use the region.connect helper.
    # overworld.connect(right_room, "Overworld to Right Room")
    # right_room.connect(final_boss_room, "Right Room to Final Boss Room")