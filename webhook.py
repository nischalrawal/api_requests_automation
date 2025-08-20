import json

from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
async def home_hook(response : Request):
    data = await response.json()       #if async and await is not inserted then it may fail silently
    print(data)

# Endpoint to receive the webhook response. This webhook endpoints must use with the https://ngrokURl/nis_hook
@app.post("/nis_hook")
async def webhook(response : Request):
    data = await response.json()       #if async and await is not inserted then it may fail silently
    print(data)


@app.post("/musicgpt/cover")
async def cover(response : Request):
    print("Response received from musicgpt/cover")
    data = await response.json()
    print(f"cover : {data}")


@app.post("/musicgpt/deecho")
async def deecho (response : Request):
    print("Response received from musicgpt/deecho")
    data = await response.json()
    print(f"deecho : {data}")
    
    
@app.post("/conversions/remix")
async def remix (response : Request):
    print("Response received from conversions/remix")
    data = await response.json()
    print(f"remix : {data}")

@app.post("/conversions/music_ai")
async def music_ai (response : Request):
    print("Response received from conversions/music_ai")
    data = await response.json()
    print(f"music_ai :  {data}")




    
    
