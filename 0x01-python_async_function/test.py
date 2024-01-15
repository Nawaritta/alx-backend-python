import asyncio


async def main():
    print('A')
    await func()
    print ('B')

async def func():
    print('1')
    await asyncio.sleep(3)
    print('2')

asyncio.run(main())