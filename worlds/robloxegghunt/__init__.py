from worlds.AutoWorld import World, WebWorld

class RobloxEggHuntWebWorld(WebWorld):
    theme = "grass"

class RobloxEggHuntWorld(World):
    """This is the description for the Roblox Egg Hunt that will be displayed on the AP website."""

    game = "Roblox Egg Hunt"
    web = RobloxEggHuntWebWorld()
    item_name_to_id = {
        "placeholder": 1
    }
    location_name_to_id = {
        "2008": 1
    }