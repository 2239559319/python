# async 3.7+

import asyncio
import time

async def sayAfter(delay,what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    await sayAfter(1,'hello')
    await sayAfter(2,'world')
    print(f"started at {time.strftime('%X')}")

asyncio.run(main())