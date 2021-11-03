#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/5/20 13:36

import asyncio
import json
import typing
from typing import Optional

from fastapi import Cookie, FastAPI, Query, WebSocket, status
from fastapi.responses import HTMLResponse
from starlette.endpoints import WebSocketEndpoint
from starlette.types import Receive, Scope, Send

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <label>Item ID: <input type="text" id="itemId" autocomplete="off" value="foo"/></label>
            <label>Token: <input type="text" id="token" autocomplete="off" value="some-key-token"/></label>
            <button onclick="connect(event)">Connect</button>
            <hr>
            <label>Message: <input type="text" id="messageText" autocomplete="off"/></label>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
        var ws = null;
            function connect(event) {
                var itemId = document.getElementById("itemId")
                var token = document.getElementById("token")
                ws = new WebSocket("ws://localhost:8000/items/" + itemId.value + "/ws?token=" + token.value);
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages')
                    var message = document.createElement('li')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                };
                event.preventDefault()
            }
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


async def get_cookie_or_token(
        websocket: WebSocket,
        session: Optional[str] = Cookie(None),
        token: Optional[str] = Query(None),
):
    if session is None and token is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    return session or token


data_list = []


async def send(ws_a: WebSocket, ):
    while True:
        await ws_a.send_text("data list = {}".format(data_list))
        print("websocket A sent:", data_list)
        await asyncio.sleep(1)


@app.websocket_route("/items/{item_id}/ws")
class WebsocketTest(WebSocketEndpoint):

    def __init__(self, scope: Scope, receive: Receive, send: Send):
        super().__init__(scope, receive, send)
        self.last_message = "1"
        self.send_loop = False
        self.task = None

    async def on_connect(self, websocket: WebSocket) -> None:
        print(f"打开websocket连接")
        await websocket.accept()
        loop = asyncio.get_running_loop()
        task = asyncio.create_task(send(websocket))
        self.task = task
        asyncio.ensure_future(task, loop=loop)

    async def on_receive(self, websocket: WebSocket, data: typing.Any) -> None:
        print(f"收到消息{data}")
        self.last_message = data
        data_list.append(data)
        await websocket.send_text(f"后端接收到你发送的消息信息，{json.dumps(data)}, 已经处理完毕")

    async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
        self.task.cancel()
        print(f"断开了连接")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
