from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region, DEFAULT_COLLECTION_RULE

if TYPE_CHECKING:
    from .World import RobloxEggHuntWorld

region_names = [
    "Spawn",
]


def create_and_connect_regions(world: RobloxEggHuntWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: RobloxEggHuntWorld) -> None:
    # print([Region(name, world.player, world.multiworld) for name in region_names])
    regions = [Region(name, world.player, world.multiworld) for name in region_names]
    world.multiworld.regions += regions


def create_one_way(world: RobloxEggHuntWorld, a: Region, b: Region, rule: Callable = DEFAULT_COLLECTION_RULE) -> None:
    pass


def connect_regions(world: RobloxEggHuntWorld) -> None:
    pass
