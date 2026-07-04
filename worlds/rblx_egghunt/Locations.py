from __future__ import annotations
from typing import TYPE_CHECKING, Dict

from BaseClasses import Location, ItemClassification

from .Types import baseId, RobloxEggHuntLocation

if TYPE_CHECKING:
    from .World import RobloxEggHuntWorld

eggs: Dict[str, int] = {
    "MeteorEgg":        76679882,
    "CrystalEgg":       76679360,
    "Eggcognito":       76680203,
    "EggTimer":         76677482,
    "LockedEgg":        76680033,
    "TerrorEgg":        76677639,
    "JanitorEgg":       76680734,
    "GreyGooEgg":       76680530,
    "VampireEgg":       76677323,
    "AntiGravityEgg":   76677756,
    "HyperactiveEgg":   76680247,
    "OfficeEgg":        76678200,
    "SubterraneanEgg":  76677735,
    "SFOTHEgg":         76678056,
    "ChaosCanyonEgg":   76678370,
    "CrossRoadsEgg":    76678590,
    "EndOfDaysEgg":     76680855,
    "StoogeEgg":        76769033,
    "SkyEgg":           76677877,
    "GhostEgg":         76680696,
    "LastEgg":          76680134,
    "WaterEgg":         76677061,
    "BinaryFabrege":    76678050,
    "EnigmaFabrege":    76693143,
    "RedRubyFabrege":   76692912
}

all_locations: Dict[str, int] = {
    **eggs,
}

LOCATION_TABLE = {location_name: all_locations[location_name]+baseId for location_name in all_locations}

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: all_locations[location_name]+baseId for location_name in location_names}

def create_location(world: RobloxEggHuntWorld, region_name: str, location_table) -> None:
    region = world.get_region(region_name)
    locations = get_location_names_with_ids([location_name for location_name in location_table])
    region.add_locations(locations, RobloxEggHuntLocation)

def create_all_locations(world: RobloxEggHuntWorld) -> None:
    create_location(world, "Spawn", eggs)


def create_events(world: RobloxEggHuntWorld) -> None:
    pass