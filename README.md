from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatIn(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(payload: ChatIn, authorization: str = Header(None)):
    if authorization != "Bearer my-secret-key-123":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"reply": "สวัสดีครับ! ผมบอทจาก Bangk พร้อมช่วยเหลือครับ"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
