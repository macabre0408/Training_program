from fastapi import APIRouter
order_app = APIRouter(
    prefix ='/order',
    tags = ['order']
)
@order_app.get('/')
async def hello():
    return {
        "message" : "Welocome user from Togo!!"
    }