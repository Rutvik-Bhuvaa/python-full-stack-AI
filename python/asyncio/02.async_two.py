import asyncio

async def brew_chai(name):
    print(f"Brewing {name}")
    await asyncio.sleep(2)
    print(f"{name} chai is ready")

async def main():
    await asyncio.gather(
        brew_chai("Masala"),
        brew_chai("Ginger"),
        brew_chai("Green"),
    )

asyncio.run(main())




