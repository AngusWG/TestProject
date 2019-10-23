''' websocket test '''
import json
import time

import websocket


def on_open(ws):
    print('on_open')


def on_message(ws, message):
    message = json.loads(message)
    print("on_message")
    print(message)


def on_error(ws, error):  # 程序报错时，就会触发on_error事件
    print("on_error")
    print(error)


def on_close(ws):
    print("Connection closed ……")


# url = 'ws://172.18.0.213:10305/socket.io/order'
url = 'ws://127.0.0.1:10305/socket.io'
# url = 'ws://k.com:10305/socket.io'
cookie = "io=51139d4350ae4b6f8795e363cbd867f9; jwt=eyJhbGciOiAiSFMyNTYiLCAiaWF0IjogMTU2OTU3NDc0OCwgImV4cCI6IDE1NzIxNjY3NDh9.eyJ1c2VybmFtZSI6ICIrODYxODY3MDMwNjMxNSIsICJlbWFpbCI6ICI3NDA3MTM2NTFAcXEuY29tIiwgImlkIjogMTIzNDU2NzgxMjM0NjI2MSwgImZ1bGxuYW1lIjogImFiY1Rlc3QiLCAicGljdHVyZSI6ICJodHRwczovL2Nkbi5yaWNlcXVhbnQuY29tL2ltZy9hdmF0YXIvYzgyMzY5ZjAtYWU1OS00ODdhLWJlNTQtOTRlMTJlMjcwYmUyLnBuZyJ9.3To1gfL_e_duBQplp4jvubgwt9DsKO5N0I0jYiyKeA0; jupyter-hub-token=; sid=2cc1bd6a-e8ad-43ad-a38c-5d813eb33d96|50f068fee4d4a755fc472e0163827db5a37f86147e252396e646326470c8a3951597ef0dd6ab75b32292085f94b09b1d7baa526323f2e5c8adab9f1aea447097"
websocket.enableTrace(True)
ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close,cookie=cookie)
ws.run_forever()
# run_forever_kwargs = {'http_proxy_host': '127.0.0.1', 'http_proxy_port': 9999}
# ws.run_forever()
