

import asyncio
import websockets
import requests
import json
import time


async def fetch_data():

    uri = "ws://localhost:8765"
    url = "https://yh-finance-complete.p.rapidapi.com/yhprice"

    querystring = {"ticker":"TSLA"}

    headers = {
        "X-RapidAPI-Key": "e2b46d24b2msh3da3abc9da6a3c5p1380b6jsn32b090fed49e",
        "X-RapidAPI-Host": "yh-finance-complete.p.rapidapi.com"
    }

    async with websockets.connect(uri) as websocket:
        # while True:
            try:
                # if request_count < 3:
                response = requests.get(url,
                                        headers=headers,
                                        params=querystring)
                
                resp = json.dumps(response.json())

                await(websocket.send(resp))
                print(f'>>>sent response {type(resp)} to the server')

                greeting = await websocket.recv()
                print(f'<<< received from server {greeting}')
                # else:
                #     print("Rate limit exceeded. Waiting for 60 seconds.")
                #     time.sleep(60)
                #     request_count = 0

            # except KeyboardInterrupt:
            #     break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":

    request_count = 0
    while request_count < 3:
        asyncio.run(fetch_data())
        request_count += 1