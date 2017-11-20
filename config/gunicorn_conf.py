import multiprocessing


workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'aiohttp.GunicornUVLoopWebWorker'
loglevel = 'debug'
access_log = '-'
error_log = '-'
timeout = 120
