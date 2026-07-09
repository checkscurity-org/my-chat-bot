from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

class ChatIn(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(payload: ChatIn):
    return {"reply": "สวัสดีครับ! ผมบอทจาก Bangk พร้อมช่วยเหลือครับ"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
    
