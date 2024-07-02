from fastapi import FastAPI
from user import *
from commande import *
app = FastAPI()
app.include_router(user_app)
app.include_router(order_app)