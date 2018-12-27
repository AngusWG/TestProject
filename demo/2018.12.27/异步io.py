import time
import asyncio
from threading import Thread
import redis
import aiohttp


def get_redis():
    connection_pool = redis.ConnectionPool(host='127.0.0.1', db=3)
    return redis.Redis(connection_pool=connection_pool)


rcon = get_redis()


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            return await resp.text()


async def do_some_work(x):
    print('Waiting ', x)
    try:
        ret = await fetch(url='http://127.0.0.1:5000/{}'.format(x))
        print(ret)
    except Exception as e:
        try:
            print(await fetch(url='http://127.0.0.1:5000/error'))
        except Exception as e:
            print(e)
    else:
        print('Done {}'.format(x))


new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.setDaemon(True)
t.start()

try:
    while True:
        task = rcon.rpop("queue")
        if not task:
            time.sleep(1)
            continue
        asyncio.run_coroutine_threadsafe(do_some_work(int(task)), new_loop)
except Exception as e:
    print('error')
    new_loop.stop()
finally:
    pass
