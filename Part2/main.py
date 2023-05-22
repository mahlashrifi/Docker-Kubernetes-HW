import os

import redis
from fastapi import FastAPI, Request
import httpx
import json
import socket

app = FastAPI()
client = httpx.AsyncClient()

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
@app.post(os.getenv("END_POINT"))
async def get_shorter_url(data: Request):
    data = await data.json()

    headers = {'accept': 'application/json',
               'apikey': os.getenv("API_KEY"),
               'content-type': 'application/json'}

    apiUrl = 'https://api.rebrandly.com/v1/links'

    destination = data["destination"]
    is_cached = False
    short_url = None

    if (r.exists(destination) == 1):
        short_url = r.get(destination)
        is_cached = True
    else:
        json_data = json.dumps(data)
        response = await client.post(apiUrl, headers=headers, data=json_data)
        short_url = response.json()["shortUrl"]
        r.set(destination, short_url)
        r.expire(destination, os.getenv("VALID_CACHED_TIME") * 60)

    result = {}
    result["longUrl"] = destination
    result["shortUrl"] = short_url
    result["isCached"] = is_cached
    result["hostname"] = socket.gethostname()

    return result

@app.get("/")
async def get_shorter_url(data: Request): 
    return socket.gethostname()