from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.chatbot_routes import router as chatbot_router

app = FastAPI()

# Mount the static folder for HTML and other static assets
app.mount("/static", StaticFiles(directory="static"), name="static")

# Mount the videos folder to serve video files
app.mount("/videos1", StaticFiles(directory="videos1"), name="videos1")


# Include the router from chatbot_routes.py
app.include_router(chatbot_router)

@app.get("/")
async def root():
    return {"message": "hi"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
