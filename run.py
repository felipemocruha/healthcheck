from server import utils, create_app
from aiohttp import web
import uvloop
import asyncio
import logging
import sys


env = utils.get_env_vars()
app = create_app(env)

if __name__ == '__main__':
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    web.run_app(app, access_log='-')
