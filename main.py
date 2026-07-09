from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# เปิดให้ทุกเว็บเข้าถึง API ได้
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatIn(BaseModel):
    message: str

# API ที่ทำงานได้จริง
@app.post("/api/chat")
async def chat(payload: ChatIn, authorization: str = Header(None)):
    # เช็ค Key ความปลอดภัย
    if authorization != "Bearer my-secret-key-123":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"reply": "สวัสดีครับ! ผมบอทจาก Bangk พร้อมช่วยเหลือครับ"}

# หน้าแรกให้ตอบกลับว่า "Online" เพื่อแก้ปัญหา 404
@app.get("/")
async def root():
    return {"status": "Online"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
