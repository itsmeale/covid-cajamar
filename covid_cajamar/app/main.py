from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def predict():
    return {
        "response": "dummy_response",
        "status": "200",
    }
