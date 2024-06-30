# main.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from scrape.web_scrape import PRICE_MAP

app = FastAPI()


@app.get("/")
def read_root():
    content = PRICE_MAP
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Expose-Headers": "Content-Length, X-Content-Length",
        "Access-Control-Max-Age": "3600",
    }
    return JSONResponse(content=content, headers=headers)
