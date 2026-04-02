from fastapi import FastAPI, WebSocket,WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
app=FastAPI()
app.mount("/static",StaticFiles(directory="app/static"),name="static")
@app.get("/")
async def home():
        return FileResponse("app/static/index.html")
connections={}
@app.websocket("/ws")
async def ws_socet(websocket:WebSocket):
    await websocket.accept()
  
    username=await websocket.receive_text()
    connections[username]=websocket
    for ws in connections.values():
         await ws.send_text(f"{username} joined the chat")
    try:
        while True:
            data=await websocket.receive_text()
            for ws in connections.values():
                await ws.send_text(f"{username}:{data}")
    except WebSocketDisconnect:
        del connections[username]
        for ws in connections.values():
             await ws.send_text(f"{username} left the chat")
