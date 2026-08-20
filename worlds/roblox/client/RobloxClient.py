import sys
import asyncio
import logging
from aiohttp import web

import Utils
from CommonClient import ClientCommandProcessor, CommonContext, logger, server_loop, gui_enabled, get_base_parser, \
    handle_url_arg

from .RobloxContext import RobloxContext

async def web_default(req: web.Request, ctx: RobloxContext) -> web.Response:
    return web.json_response(ctx.get_state())

def create_routes(app: web.Application, ctx: RobloxContext):
    app.router.add_route("GET", "/", lambda req: web_default(req, ctx))

# https://github.com/ArchipelagoMW/Archipelago/blob/main/worlds/_sc2common/bot/proxy.py#L167-L168
async def client_loop(ctx: RobloxContext) -> None:
    # Setup Webserver
    app = web.Application()
    create_routes(app, ctx)
    apprunner = web.AppRunner(app, access_log=None)
    await apprunner.setup()
    appsite = web.TCPSite(apprunner, port=38282)
    await appsite.start()
    logger.info(f'WebServer started on {appsite.name}')

    # Read Current Roblox Instance Logs

    await ctx.exit_event.wait()
    await apprunner.cleanup()


def launch_client(*args) -> None:
    async def main():
        logger.info(f'Launching with args: {args}')
        ctx = RobloxContext(args.connect, args.password)
        ctx.auth = args.name

        ctx.server_task = asyncio.create_task(server_loop(ctx), name="Server Loop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        ctx.client_loop = asyncio.create_task(client_loop(ctx), name="Client Loop")
        await ctx.exit_event.wait()
        await ctx.shutdown()

    Utils.init_logging("RobloxClient", exception_logger="Client")
    import colorama

    parser = get_base_parser()
    parser.add_argument('--name', default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")
    args = parser.parse_args(args)

    args = handle_url_arg(args, parser=parser)

    colorama.just_fix_windows_console()
    asyncio.run(main())
    colorama.deinit()
