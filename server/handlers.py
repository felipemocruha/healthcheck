from server import utils
from aiohttp import web


async def get_services(redis, request, utils=utils):
    services = utils.load_services(redis)
    return web.json_response(services)


async def get_service(redis, request, utils=utils):
    s_id = request.match_info['s_id']
    service = utils.load_service(redis, s_id)
    return web.json_response(service)


async def create_service(redis, request, utils=utils):
    data = await request.json()
    service = utils.new_service(**data)
    redis.lpush('services', service)
    return web.Response(body='', status=201)


async def delete_service(redis, request, utils=utils):
    s_id = request.match_info['s_id']
    utils.delete_service(redis, s_id)
    return web.Response(body='', status=204)
