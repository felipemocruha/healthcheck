import requests
from redis import StrictRedis
import logging
from uuid import uuid4
from collections import namedtuple
import pickle
import sys
from os import getenv
from datetime import datetime


def get_env_vars(getenv=getenv):
    return {
        'REDIS_HOST': getenv('REDIS_HOST', 'localhost'),
        'REDIS_PORT': int(getenv('REDIS_PORT'), 6379),
        'CHECK_INTERVAL': int(getenv('CHECK_INTERVAL')), 60)
    }


def new_service(**kwargs):
    return pickle.dumps((uuid4().hex, kwargs['name'],kwargs['url']))


def load_services(redis):
    return [pickle.loads(s) for s in redis.lrange('services', 0, -1)]


def load_service(redis, s_id):
    services = load_services(redis)
    load_service = lambda item: item[0] == s_id
    return [*filter(load_service, services)]


def delete_service(redis, s_id):
    service = load_service(redis, s_id)[0]
    redis.lrem('services', 1, pickle.dumps(service))



def make_requests(env, requests=requests):
    redis = StrictRedis(
        host=env['REDIS_HOST'], port=env['REDIS_PORT'])
    urls = [s[2]+'/healthcheck' for s in load_services(redis)]
    logger = get_logger()

    for url in urls:
        r = requests.get(url)
        if r.status_code != 200:
            logger.info('[*] Service at {} is unrecheable!'.format(url))


def initialize_scheduler(scheduler, env):
    kwargs = {
        'scheduled_time': datetime.utcnow(),
        'func': make_requests,
        'args': [env],
        'interval': env['CHECK_INTERVAL']
    }
    scheduler.schedule(**kwargs)


def get_logger():
    handler = logging.StreamHandler(sys.stdout)
    logger = logging.getLogger('asyncio')
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
