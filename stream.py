import asyncio
import json
from datetime import datetime
from websockets import connect

websocket_url = "wss://fstream.binance.com/ws/!forceOrder@arr"

async def binance_liquidations():
    async for websocket in connect(websocket_url):
        try:
            while True:
                msg = await websocket.recv()
                print(msg)
                msg = json.loads(msg)['o']
                data = {
                    'symbol': msg['s'],
                    'side': msg['S'],
                    'order_type': msg['o'],  
                    'time_in_force': msg['f'],
                    'original_quantity': msg['q'],
                    'price': msg['p'],
                    'average_price': msg['ap'],
                    'order_status': msg['X'],
                    'order_last_filled_quantity': msg['l'],
                    'order_filled_accumulated_quantity': msg['z'],
                    'order_trade_time': datetime.now().isoformat()
                }
                # Save data to a database or perform any other required processing here
        except Exception as e:
            print(e)
            continue

asyncio.get_event_loop().run_until_complete(binance_liquidations())
