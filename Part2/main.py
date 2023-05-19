from fastapi import FastAPI, Request
app = FastAPI()

@app.get("/")
async def test():
   return "I am working"
