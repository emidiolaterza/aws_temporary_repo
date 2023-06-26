from fastapi import FastAPI
import uvicorn
from mangum import Mangum

app = FastAPI()
lambda_handler = Mangum(app)



@app.get("/")
async def hello():
    return {"message":"Hello World"}

if __name__ == "__main__":
    uvicorn.run("first_sample:app", host="127.0.0.1", port=8000, reload=True)
