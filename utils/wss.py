''' websocket test '''
import json
import websocket
import time


def on_open(ws):
    print('on_open')
    d = '{"op": "subscribe", "args": ["trade": ["ETHXBT","LTCXBT","DASHXBT","ZECXBT","ETCXBT","XMRXBT","XRPXBT",XTZXBT"]]}'
    ws.send(d)


def on_message(ws, message):
    message = json.loads(message)
    print('message', message)
    the_time = int(message.get('date')[:-3])
    print(time.localtime(the_time))


url = 'wss://www.bitmex.com/realtime/'
websocket.enableTrace(True)
ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message)
# ws.run_forever(http_proxy_host='127.0.0.1', http_proxy_port=9999)
ws.run_forever()

print('end...')
