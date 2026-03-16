from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld

region_names = [
    "Dormont",
    "Entrance",

    "Floor 1 - Main Room",
    # "Floor 1 - Forge",
    # "Floor 1 - Crest"
    # "Floor 1 - Kitchen",
    # "Floor 1 - Left Hallway",
    # "Floor 1 - Bedroom A",
    # "Floor 1 - Bedroom B",
    # "Floor 1 - Storage Room 1",

    "Floor 2 - Main Room",
    # "Floor 2 - Classroom",
    # "Floor 2 - Crest",
    # "Floor 2 - Housemaiden's Office",
    # "Floor 2 - Trap Room",
    # "Floor 2 - Poem Room",
    # "Floor 2 - Library",
    # "Floor 2 - Secret Library",

    "Floor 3 - Main Room",
    # "Floor 3 - Mirror Room",
    # "Floor 3 - Secret Room",
    # "Floor 3 - Pottery Studio"
    # "Floor 3 - Observatory"
    # "Floor 3 - Crest",
    # "Floor 3 - Poem Room",
    # "Floor 3 - Crest",
    # "Floor 3 - Mirabell's Room",
    # "Floor 3 - Body Crafting Room",
    # "Floor 3 - In-Between Room",
    # "Floor 3 - Shrine",

    "The End"
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