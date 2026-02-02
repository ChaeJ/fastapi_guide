import logging
import os
from fastapi import FastAPI
from api.v1.router import router as v1_router
from global_exception import setup_global_exception_handler
from middlewares import setup_middlewares
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(
    level=logging.INFO,
    format=os.getenv("LOG_FORMAT", "%(asctime)s %(levelname)s [%(name)s] %(message)s"),
)

app = FastAPI()

app.add_middleware(CORSMiddleware,                   
                   allow_origins=["http://localhost:8000"],
                   allow_credentials=False,
                   allow_methods=["GET", "POST", "PUT", "DELETE"],
                   allow_headers=["*"],)

setup_middlewares(app)


app.include_router(v1_router, prefix="/v1")

setup_global_exception_handler(app)