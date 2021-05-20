#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/5/20 13:36

# https://stackoverflow.com/questions/65361686/websockets-stream-audio-in-json-out-w-fastapi-and-two-websockets
import asyncio

from fastapi import FastAPI, WebSocket
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
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
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


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    fwd_task = asyncio.create_task(send(websocket))
    rev_task = asyncio.create_task(recv(websocket))
    await asyncio.gather(fwd_task, rev_task)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
