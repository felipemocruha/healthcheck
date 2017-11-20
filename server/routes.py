from server.handlers import *
from cytoolz import partial


def add_route(app, method, path, handler):
    app.router.add_route(method, path, handler)


def create_routes(app, redis):
    route = partial(add_route, app)
    handler = lambda fn: partial(fn, redis)

    route('GET', '/api/services', handler(get_services))
    route('POST', '/api/services', handler(create_service))
    route('GET', '/api/services/{s_id}', handler(get_service))
    route('DELETE', '/api/services/{s_id}', handler(delete_service))
