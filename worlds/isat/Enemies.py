from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .World import InStarsAndTimeWorld

ENEMIES = [
    1, 2, 3, 4, 5, 6, 7, 8,
    11, 12, 13, 14, 15, 16,
    17, 18, 19, # NOSTALGIE
    20, # Tutorial Kid
    21, 22, 23, 24, # Mini-Boss
    26, 27, 28, 29, 30, 31, 34, 35, # Bosses
    37, 38, 39, # Tutorial
    40, # Test baby
    42, 43, 44, 46, 47,
    50, 51, 52,
    54, 55, 56, 57, 58, 59, 60, 61,
    63, 64
]

TROOPS = []

def randomize_enemies(world: InStarsAndTimeWorld) -> None:
    # Took this from v6's APWorld
    enemies_shuffled = ENEMIES.copy()
    if world.options.enemy_rando:
        world.multiworld.random.shuffle(enemies_shuffled)
    world.enemy_map = dict(zip(ENEMIES, enemies_shuffled))

def randomize_troops(world: InStarsAndTimeWorld):
    print("In Stars And Time: randomize_troops stub...")
    world.troop_map = {1: 1}