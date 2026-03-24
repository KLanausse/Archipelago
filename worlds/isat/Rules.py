from __future__ import annotations

from typing import TYPE_CHECKING

from worlds.generic.Rules import add_rule, set_rule

from .Locations import all_locations

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
    for location_name in all_locations:
        location = world.get_location(location_name)
        data = all_locations[location_name]

        match data.rule_type:
            case "has":
                set_rule(location, lambda state, args=data.rule_args: state.has(args, world.player))
            case "has_any":
                set_rule(location, lambda state, args=data.rule_args: state.has_any(args, world.player))
            case "has_all":
                set_rule(location, lambda state, args=data.rule_args: state.has_all(args, world.player))
            case _: # Default
                pass

        # Acts
        match data.act:
            case "Act 2":
                add_rule(location, lambda state: state.has("Circle Key", world.player))
            case "Act 3":
                add_rule(location, lambda state: state.has("Circle Key", world.player))
                add_rule(location, lambda state: state.has_any(["Lovely Moving Shield", "Holy Care Shield"], world.player))

            case _:  # Default
                pass
        # all_locations[location_name].rule_type