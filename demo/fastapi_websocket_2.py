#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/5/20 13:36

# https://stackoverflow.com/questions/65361686/websockets-stream-audio-in-json-out-w-fastapi-and-two-websockets
import asyncio
from typing import Optional

from fastapi import Cookie, Depends, FastAPI, Query, WebSocket, status
from fastapi.responses import HTMLResponse

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


data_list = []


async def send(ws_a: WebSocket, ):
    while True:
        await ws_a.send_text("data list = {}".format(data_list))
        print("websocket A sent:", data_list)
        await asyncio.sleep(3)


async def recv(ws_a: WebSocket, ):
    while True:
        data = await ws_a.receive_text()
        data_list.append(data)
        print("websocket A sent:", data_list)


async def get_cookie_or_token(
        websocket: WebSocket,
        session: Optional[str] = Cookie(None),
        token: Optional[str] = Query(None),
):
    if session is None and token is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    return session or token


@app.websocket("/items/{item_id}/ws")
async def websocket_endpoint(
        websocket: WebSocket,
        item_id: str,
        q: Optional[int] = None,
        # cookie_or_token: str = Depends(get_cookie_or_token),
):
    await websocket.accept()
    fwd_task = asyncio.create_task(send(websocket))
    rev_task = asyncio.create_task(recv(websocket))
    await asyncio.gather(fwd_task, rev_task)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
