from fastapi import FastAPI
import sys

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "Welcome to the DevOps CI/CD Pipeline!"}

@app.get("/info")
def get_info():
    return {
        "app_name": "docker-ci-cd-pipeline",
        "python_version": sys.version.split(" ")[0]
    }
