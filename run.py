import uvicorn
# from backend.app import main

if __name__ == "__main__":
    uvicorn.run("backend.app.main:app", host="localhost", port=8080, reload=True)