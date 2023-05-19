from fastapi import FastAPI, Request
import httpx
import json

app = FastAPI()

@app.post("/shorten")
async def get_shorter_url(data: Request):
   data = await data.json()

   # I did not push my key to github
   headers = {'accept': 'application/json',
             'apikey': "My Key",
             'content-type': 'application/json'}
   apiUrl = 'https://api.rebrandly.com/v1/links'

   json_data = json.dumps(data)
   response = await client.post(apiUrl, headers=headers, data=json_data)  

   result = {}
   result["longUrl"] = data["destination"]
   result["shortUrl"] = response.json()["shortUrl"] 
   result["isCached"] = False
   result["hostname"] = "mahla"

   return result
