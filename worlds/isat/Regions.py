from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld

region_names = [
    "Dormont",
    "Entrance",
    "Floor 1",
    "Floor 2",
    "Floor 3",
    "The End"
]


def create_and_connect_regions(world: InStarsAndTimeWorld) -> None:
    create_all_regions(world)
    #connect_regions(world)

def create_all_regions(world: InStarsAndTimeWorld) -> None:

    regions = [Region(name, world.player, world.multiworld) for name in region_names]
    world.multiworld.regions += regions