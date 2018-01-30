''' websocket test '''
import json
import time

import websocket


def on_open(ws):
    print('on_open')
    symbols = ['BCNBTC',
               'BTCUSD',
               'DASHBTC',
               'DOGEBTC',
               'DOGEUSD',
               'DSHBTC',
               'EMCBTC',
               'ETHBTC',
               'FCNBTC'
               ]

    for i in symbols:
        d = {
            "method": "subscribeTicker",
            "params": {
                "symbol": i
            },
            "id": 123
        }
        ws.send(json.dumps(d))
        # time.sleep(5)
        # d = {
        #     "method": "subscribeTrades",
        #     "params": {
        #         "symbol": i
        #     },
        #     "id": 123
        # }
        # ws.send(json.dumps(d))
        # time.sleep(5)
        d = {
            "method": "subscribeOrderbook",
            "params": {
                "symbol": i
            },
            "id": 123
        }
        ws.send(json.dumps(d))
        print("finis send")


def on_message(ws, message):
    message = json.loads(message)
    print(message)


url = 'wss://api.hitbtc.com/api/2/ws'
websocket.enableTrace(True)
ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message)
ws.run_forever(http_proxy_host='127.0.0.1', http_proxy_port=9999)
# run_forever_kwargs = {'http_proxy_host': '127.0.0.1', 'http_proxy_port': 9999}
# ws.run_forever()
