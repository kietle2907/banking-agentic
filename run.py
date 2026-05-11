import uvicorn

if __name__ == "__main__":
    # Khởi chạy server FastAPI tại cổng 8001
    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)