from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from BaseClasses import ItemClassification
from rule_builder.rules import (  # rule_builder is new to Archi 0.6.7 - misch13vous
    And,
    Has,
    HasAll,
    HasAny,
    Rule,
    True_,
)

from .Items import InStarsAndTimeItem
from .Locations import all_locations

RULE_DEFAULT = True_()
RULE_FLOOR_1 = Has("Circle Key")
RULE_FLOOR_2 = And(RULE_FLOOR_1, Has("Broken Egg Key"))
RULE_LOOP = And(RULE_FLOOR_1, Has("Loop's Silver Coin"))
RULE_FLOOR_3 = And(RULE_FLOOR_2, Has("Scissors Key"))
RULE_KING = And(RULE_FLOOR_3, Has("KeyKnife"))
RULE_VICTORY = And(RULE_KING, HasAny("Holy Care Shield", "Adorable Moving Shield"))
RULE_LIBRARY = And(RULE_KING, Has("Rock Key"))
RULE_MIRABELLE = And(RULE_VICTORY, Has("Smiling Key"))
RULE_LOVED = And(RULE_MIRABELLE, Has("Rock Key"))
RULE_TIME_CRAFT = And(RULE_LOVED, Has("Egg Key"))
RULE_BETRAYED = And(RULE_TIME_CRAFT, Has("Double Star Crest"))
RULE_WISH_CRAFT = And(RULE_BETRAYED, Has("Memory of Memories"))
RULE_FAVOR_TREE = And(RULE_WISH_CRAFT, Has("Stostorage Roomoom Openphrase"))
RULE_INCIDENT = And(RULE_WISH_CRAFT, Has("Siffrin's Silver Coin"))
RULE_FINALE = And(RULE_FAVOR_TREE, HasAll("Teardrop Star Crest", "Clock Star Crest", "Angry Key", "Smiling Key"))
RULE_TWO_HATS = And(RULE_FINALE, RULE_LOOP)

rule_table: dict[str, Rule] = {
    "Default": RULE_DEFAULT,
    "Shopkeeper": RULE_FLOOR_1,
    "Openphrase": RULE_FLOOR_1,
    "Floor 1": RULE_FLOOR_1,
    "Stylish One": RULE_FLOOR_2,
    "Floor 2": RULE_FLOOR_2,
    "Loop": RULE_LOOP,
    "Last Issue": RULE_FLOOR_3,
    "Floor 3": RULE_FLOOR_3,
    "King": RULE_KING,
    "Victory": RULE_VICTORY,
    "Library": RULE_LIBRARY,
    "Confession": RULE_VICTORY,
    "Mirabelle": RULE_MIRABELLE,
    "Odile": RULE_LIBRARY,
    "Loved": RULE_LOVED,
    "Time Craft": RULE_TIME_CRAFT,
    "Betrayed": RULE_BETRAYED,
    "Wish Craft": RULE_WISH_CRAFT,
    "Favor Tree": RULE_FAVOR_TREE,
    "Incident": RULE_INCIDENT,
    "Finale": RULE_FINALE,
    "Two Hats": RULE_TWO_HATS,
}


if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld


def set_all_rules(world: InStarsAndTimeWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    # set_all_entrance_rules(world)
    set_all_location_rules(world)
    # set_completion_condition(world)


def set_all_location_rules(world: InStarsAndTimeWorld) -> None:
    print("In Stars And Time: set_all_location_rules running...")
    for location_name in all_locations:
        location = world.get_location(location_name)
        data = all_locations[location_name]

        try:
            composed_rule = rule_table[data.prog_rule]
            if data.extra_rule is not None:
                composed_rule = And(composed_rule, data.extra_rule)
            world.set_rule(location, composed_rule)
        except KeyError:
            logging.warning(f"Error setting rule for {location_name} ({data.prog_rule})")
    world.get_location("The End - Aaaaaand SCENE!!!").place_locked_item(world.create_item("Goal Clear"))


def set_completion_condition(world: InStarsAndTimeWorld) -> None:
    world.set_completion_rule(Has("Goal Clear"))
