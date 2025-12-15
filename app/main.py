from fastapi import FastAPI

app = FastAPI(title="API Health Monitor")

@app.get("/")
def root():
    return {"status": "API Health Monitor is running"}

