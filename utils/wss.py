''' websocket test '''
import json
import websocket
import time


def on_open(ws):
    print('on_open')
    d = {
        "method": "subscribeOrderbook",
        "params": {
            "symbol": "ETHBTC"
        },
        "id": 123
    }
    ws.send(json.dumps(d))


def on_message(ws, message):
    message = json.loads(message)
    print('message', message)


url = 'wss://stream.binance.com:9443/ws/bnbbtc@depth'
websocket.enableTrace(True)
ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message)
# ws.run_forever(http_proxy_host='127.0.0.1', http_proxy_port=9999)
ws.run_forever()

print('end...')
