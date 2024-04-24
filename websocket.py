import asyncio
import pyautogui
import pydirectinput
import websockets
 
# create handler for each connection
 
pydirectinput.FAILSAFE = False
pydirectinput.PAUSE = 0

async def handler(websocket, path):
 
    while True:
        data = await websocket.recv()

        datalist = data.split()

        if(datalist[0] == "2"):

            if(datalist[2] == "control"):
                datalist[2] = "ctrl"

            if(datalist[2] == "space"):
                datalist[2] = " "


            if(datalist[1] == "1"):
                pydirectinput.keyDown(datalist[2])
            if(datalist[1] == "0"):
                pydirectinput.keyUp(datalist[2])

        if(datalist[0] == "1"):
            deltax = datalist[1]
            deltay = datalist[2]
            pydirectinput.move(int(deltax), int(deltay), relative=True)

        if(datalist[0] == "0"):
            if(datalist[1] == "1"):
                pydirectinput.mouseDown()
            if(datalist[1] == "0"):
                pydirectinput.mouseUp()
            if(datalist[1] == "3"):
                pydirectinput.mouseDown(button = "right")
            if(datalist[1] == "2"):
                pydirectinput.mouseUp(button = "right")


 

 
 
 
start_server = websockets.serve(handler, "0.0.0.0", 8765)
 
 
 
asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()
