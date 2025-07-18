from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial

class RobloxEggHuntWebWorld(WebWorld):
    theme = "grassFlowers"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Roblox with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        [""]
    )

    setup_es = Tutorial(
        setup_en.tutorial_name,
        setup_en.description,
        "Español",
        "setup_es.md",
        "setup/es",
        [""]
    )

    tutorials = [setup_en, setup_es]


class RobloxEggHuntWorld(World):
    """This is the description for the Roblox Egg Hunt that will be displayed on the AP website."""

    game = "Roblox Egg Hunt"
    web = RobloxEggHuntWebWorld()
    item_name_to_id = {
        # 2008
        "Stationary Egg of Boring": 1,
        "Blinking Egg of Relocation": 2,
        "Bouncing Egg of Boing Boing": 3,
        "Kind Egg of Sharing": 4,
        "Puzzling Egg of Enigma": 5,
        "Invisible Egg of Shadow": 6,
        "Golden Egg of Kings": 7,
        "Bombastic Egg of Annihilation": 8,
        "Wanwood Egg of ZOMG!": 9,
        "Legendary Egg of Gygax": 10,
        "Cracked Egg of Pwnage": 11,

        # 2010
        "Rusty Egg of Magnetism": 12,
        "Chrome Egg of Speeding Bullet": 13,
        "Shiny Gold Egg of Switcheroo": 14,
        "POW! To the Moon! Egg": 15,
        "Agonizingly Ugly Egg of Screensplat": 16,
        "Unassuming Egg of Shyness": 17,
        "Egg of Equinox: Day": 18,
        "Egg of Equinox: Night": 19,
        "Specular Egg of Red, No Blue": 20,
        "Vicious Egg of Singularity": 21,
        
        
    }
    location_name_to_id = {
        "2008": 1,
        "2010": 2,
        "2012": 3,
        "2013_1": 4,

    }