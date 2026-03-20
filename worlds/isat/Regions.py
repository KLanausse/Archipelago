from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld

region_names = [
    "Level",

    # Village
    "Dormont",
    "Dormont - Storage House",

    # Castle
    "Entrance",
    "Floor 1 - Main Room",  # 017 Locked by Circle Key
    "Floor 1 - Kitchen",
    "Floor 1 - Left Hallway",
#    "Floor 1 - Storage Room",
]


def create_and_connect_regions(world: InStarsAndTimeWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: InStarsAndTimeWorld) -> None:
    # print([Region(name, world.player, world.multiworld) for name in region_names])
    regions = [Region(name, world.player, world.multiworld) for name in region_names]
    world.multiworld.regions += regions


def connect_regions(world: InStarsAndTimeWorld) -> None:
    level = world.get_region("Level")
    dormont = world.get_region("Dormont")
    entrance = world.get_region("Entrance")

    floor_1_main_room = world.get_region("Floor 1 - Main Room")
    floor_1_kitchen = world.get_region("Floor 1 - Kitchen")
    floor_1_left_hallway = world.get_region("Floor 1 - Left Hallway")

    # One Ways.
    dormont_to_entrance = Entrance(world.player, "Dormont to Entrance", parent=dormont)
    dormont.exits.append(dormont_to_entrance)
    dormont_to_entrance.connect(entrance)

    entrance_to_floor_1 = Entrance(world.player, "Entrance To Floor 1", parent=entrance)
    entrance_to_floor_1.access_rule = lambda state: state.has("Circle Key", world.player)
    entrance.exits.append(entrance_to_floor_1)
    entrance_to_floor_1.connect(floor_1_main_room)

    # Two Ways
    floor_1_main_room.connect(floor_1_kitchen, "Floor 1 Main Room to Floor 1 Kitchen",
                              lambda state: state.has("Teardrop Star Crest", world.player))

    floor_1_main_room.connect(floor_1_left_hallway, "Floor 1 Main Room to Floor 1 Left Hallway",
                              lambda state: state.has("Egg Key", world.player))

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
