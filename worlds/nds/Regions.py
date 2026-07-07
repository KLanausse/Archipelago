from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region, DEFAULT_COLLECTION_RULE
from rule_builder.rules import Has

from .Types import nds_maps
from ..generic.Rules import set_rule

if TYPE_CHECKING:
    from .World import NaturalDisasterSurvivalWorld

region_names = [
    "Spawn",
]
region_names += nds_maps


def create_and_connect_regions(world: NaturalDisasterSurvivalWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: NaturalDisasterSurvivalWorld) -> None:
    # print([Region(name, world.player, world.multiworld) for name in region_names])
    regions = [Region(name, world.player, world.multiworld) for name in region_names]
    world.multiworld.regions += regions


def connect_regions(world: NaturalDisasterSurvivalWorld) -> None:
    spawn = world.get_region("Spawn")
    for region_name in nds_maps:
        region = world.get_region(region_name)
        temp_entrance = Entrance(world.player, f"Spawn {region_name}", spawn)
        spawn.exits.append(temp_entrance)
        temp_entrance.connect(region)
        set_rule(temp_entrance, lambda state: state.has(region_name, world.player))
