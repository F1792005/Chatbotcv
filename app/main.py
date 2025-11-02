from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from chat_router import router as chat_router

app = FastAPI(
    title="BaroDev Chat API",
    description="CV chatbot",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",  # nơi bạn chạy file index.html
        "http://localhost:5500",
        "http://127.0.0.1:8000",
        "http://localhost:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)


@app.get("/")
async def root():
    return {"message": "Conn is ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Get PORT from environment (Render) or default to 8000
    reload = os.environ.get("RENDER", "0") != "1"  # Disable reload on Render
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=reload)
