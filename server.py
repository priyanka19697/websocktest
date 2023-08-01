

import asyncio
import websockets
from datetime import datetime

async def hello(websocket):
    data = await websocket.recv()
    print(f" <<<<< {data}")

    greeting = f"Hello from server {datetime.now()}"
    print(f" >>>> {greeting}")


async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())