from CommonClient import ClientCommandProcessor, CommonContext, logger, server_loop, gui_enabled

class RobloxContext(CommonContext):
    tags = CommonContext.tags | {"TextOnly"}
    game = ""
    items_handling = 0b111  # receive all items for /received
    want_slot_data = True
    slot_data = {}
    hint_points = 0

    async def server_auth(self, password_requested: bool = False):

        if password_requested and not self.password:
            await super(RobloxContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game="")

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.slot_data = args["slot_data"]
            self.game = self.slot_info[self.slot].game

    def make_gui(self):
        ui = super().make_gui()

        class TextManager(ui):
            base_title = "Archipelago Roblox Client"
            icon = r"worlds/roblox/data/rbxap_alt.png"

        return TextManager

    def get_state(self) -> dict:
        return {
            "connected": self.server is not None,
            "game": self.game,
            "last_death_link": self.last_death_link,
            "hint_cost": self.hint_cost,
            "hint_points": self.hint_points,
            "finished_game": self.finished_game,
            "ready": self.ready,
            "team": self.team,
            "slot": self.slot,
            "auth": self.auth,
            "seed_name": self.seed_name,
            "slot_data": self.slot_data,
            "slot_info": self.slot_info,
            #"locations_checked": self.locations_checked,
            #"locations_scouted": self.locations_scouted,
            "items_received": self.items_received,
            "player_names": self.player_names,
            #"item_names": self.item_names,
            #"location_names": self.location_names,
        }