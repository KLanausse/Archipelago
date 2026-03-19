from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld


def set_all_rules(world: InStarsAndTimeWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    #set_all_entrance_rules(world)
    set_all_location_rules(world)
    #set_completion_condition(world)


def set_all_location_rules(world: InStarsAndTimeWorld) -> None:
    print("In Stars And Time: set_all_location_rules Stub...")
