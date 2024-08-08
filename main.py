import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/health", tags=["HEALTH"])
async def get_health_check():
    return {'status': 'ok'}

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
