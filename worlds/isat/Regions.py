from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region, DEFAULT_COLLECTION_RULE

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld

region_names = [
    "Level",

    # Village
    "Dormont",
    "Dormont - Storage House",

    # Castle
    "Entrance",
    "Floor 1",  # 017 Locked by Circle Key
    "Floor 1 - Kitchen",
    "Floor 1 - Left Hallway",
    "Floor 1 - Storage Room",

    "Floor 2",
    "Floor 2 - Library",
    "Floor 2 - Crest Locked",
    "Floor 2 - Break Room",

    "Floor 3",
    "Floor 3 - Crest Locked",
    "Floor 3 - Left Hallway",

    "The End"
]


def create_and_connect_regions(world: InStarsAndTimeWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: InStarsAndTimeWorld) -> None:
    # print([Region(name, world.player, world.multiworld) for name in region_names])
    regions = [Region(name, world.player, world.multiworld) for name in region_names]
    world.multiworld.regions += regions


def create_one_way(world: InStarsAndTimeWorld, a: Region, b: Region, rule: Callable = DEFAULT_COLLECTION_RULE) -> None:
    new_entrance = Entrance(world.player, f"{a.name} To {b.name}", parent=a)
    new_entrance.access_rule = rule
    a.exits.append(new_entrance)
    new_entrance.connect(b)


def connect_regions(world: InStarsAndTimeWorld) -> None:
    level = world.get_region("Level")
    dormont = world.get_region("Dormont")
    entrance = world.get_region("Entrance")

    floor_1 = world.get_region("Floor 1")
    floor_1_kitchen = world.get_region("Floor 1 - Kitchen")
    floor_1_left_hallway = world.get_region("Floor 1 - Left Hallway")
    floor_1_storage_room = world.get_region("Floor 1 - Storage Room")

    floor_2 = world.get_region("Floor 2")
    floor_2_library = world.get_region("Floor 2 - Library")
    floor_2_crest_locked = world.get_region("Floor 2 - Crest Locked")
    floor_2_break_room = world.get_region("Floor 2 - Break Room")

    floor_3 = world.get_region("Floor 3")
    floor_3_crest_locked = world.get_region("Floor 3 - Crest Locked")
    floor_3_left_hallway = world.get_region("Floor 3 - Left Hallway")

    the_end = world.get_region("The End")

    # One Ways.
    create_one_way(world, dormont, entrance)
    create_one_way(world, entrance, floor_1, lambda state: state.has("Circle Key", world.player))
    create_one_way(world, floor_1, floor_2, lambda state: state.has("Broken Egg Key", world.player))
    create_one_way(world, floor_2, floor_3, lambda state: state.has("Scissors Key", world.player))
    create_one_way(world, floor_3, the_end, lambda state: state.has("KnifeKey", world.player))

    # Two Ways
    # Floor 1
    floor_1.connect(floor_1_kitchen, "Floor 1 to Floor 1 - Kitchen",
                    lambda state: state.has("Teardrop Star Crest", world.player))

    floor_1.connect(floor_1_left_hallway, "Floor 1 to Floor 1 Left Hallway",
                    lambda state: state.has("Egg Key", world.player))

    floor_1.connect(floor_1_storage_room, "Floor 1 to Floor 1 Storage Room",
                    lambda state: state.has("Stostorage Roomoom Openphrase", world.player))

    # Floor 2
    floor_2.connect(floor_2_library, "Floor 2 to Floor 2 Library",
                    lambda state: state.has("Rock Key", world.player))

    floor_2.connect(floor_2_crest_locked, "Floor 2 to Floor 2 Crest Locked",
                    lambda state: state.has("Clock Star Crest", world.player))

    floor_2.connect(floor_2_break_room, "Floor 2 to Floor 2 Break Room",
                    lambda state: state.has("Openphrase123 Openphrase", world.player))

    # Floor 3
    floor_3.connect(floor_3_crest_locked, "Floor 3 to Floor 3 Crest Locked",
                    lambda state: state.has("Double Star Crest", world.player))

    floor_3.connect(floor_3_left_hallway, "Floor 3 to Floor 3 Left Hallway",
                    lambda state: state.has("Smiling Key", world.player))


    # Make Level A Global Region
    for region_name in region_names:
        region = world.get_region(region_name)
        temp_entrance = Entrance(world.player, f"{region_name} to Level", parent=region)
        region.exits.append(temp_entrance)
        temp_entrance.connect(level)

    # entrance.connect(floor_1_main_room, "Entrance to Floor 1", lambda state: state.has("Circle Key", world.player))

    # floor_1.connect(floor_2, "Floor 1 to Floor 1", lambda state: state.has("Broken Egg Key", world.player))

    # An even easier way is to use the region.connect helper.
    # overworld.connect(right_room, "Overworld to Right Room")
    # right_room.connect(final_boss_room, "Right Room to Final Boss Room")
