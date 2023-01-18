import asyncio

async def get_value():
    await asyncio.sleep(1)
    return 123

async def slow_operation():
    value = await get_value()
    print(">>", value)
    
slow_operation()