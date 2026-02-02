from fastapi import FastAPI
from .logging import RequestLogMiddleware

def setup_middlewares(app: FastAPI):
    app.add_middleware(RequestLogMiddleware)
