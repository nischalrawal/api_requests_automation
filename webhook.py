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


@app.post("/cover")
async def cover(response : Request):
    print("Response received from cover")
    data = await response.json()
    print(f"cover {data}")


@app.post("/deecho")
async def deecho (response : Request):
    print("Response received from deecho")
    data = await response.json()
    print(f"deecho {data}")
    
    
@app.post("/remix")
async def remix (response : Request):
    print("Response received from remix")
    data = await response.json()
    print(f"deecho {data}")




    
    
