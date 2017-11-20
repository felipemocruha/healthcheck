from server import handlers, routes
from aiohttp import web
from redis import StrictRedis, Redis
from rq_scheduler import Scheduler
import asyncio


def create_app(env):
    app = web.Application()
    redis = StrictRedis(host=env['REDIS_HOST'], port=env['REDIS_PORT'])
    routes.create_routes(app, redis)

    scheduler = Scheduler(connection=redis)
    utils.initialize_scheduler(scheduler, env)

    return app
