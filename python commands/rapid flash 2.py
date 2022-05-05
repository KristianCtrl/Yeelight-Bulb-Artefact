from yeelight import Bulb
from yeelight.aio import AsyncBulb
import asyncio
import time

async def do_nothing(param):
    pass

async def main():
    bulb = AsyncBulb("IP HERE")
    await bulb.async_listen(do_nothing)
    bulb.turn_on()
    bulb.start_music()
    print(bulb.music_mode)

    counter = 0
    while True:
        await bulb.async_set_rgb(255, 0, 0)
        counter += 1
        print(counter)
        await asyncio.sleep(0.1)
        await bulb.async_set_rgb(0, 255, 0)
        counter += 1
        print(counter)
        await asyncio.sleep(0.1)
        await bulb.async_set_rgb(0, 0, 255)
        counter += 1
        print(counter)
        await asyncio.sleep(0.1)

# asyncio.run(main())

def main_sync():
    bulb = Bulb("IP HERE")
    bulb.turn_on()
    bulb.start_music()

    counter = 0
    while True:
        bulb.set_rgb(255, 0, 0)
        counter += 1
        print(counter)
        time.sleep(0.1)
        bulb.set_rgb(0, 255, 0)
        counter += 1
        print(counter)
        time.sleep(0.1)
        bulb.set_rgb(0, 0, 255)
        counter += 1
        print(counter)
        time.sleep(0.1)

main_sync()
