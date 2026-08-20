from worlds.LauncherComponents import Component, Type, components, launch, icon_paths

def run_client(*args: str) -> None:
    from .client.RobloxClient import launch_client

    launch(launch_client, name="Roblox Client", args=args)

icon_paths["roblox"] = f"ap:{__name__}/data/rbxap_50x50.png"

components.append(
    Component(
        "Roblox Client",
        func=run_client,
        component_type=Type.CLIENT,
        icon="roblox",
        description="For connecting supported games on Roblox to Archipelago.",
        supports_uri=True,
    )
)