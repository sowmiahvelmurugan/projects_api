from .database import engine
from .schemas import BonusRequest
from .models import Base
from .reward_service import grant_bonus
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/grant-bonus")
def create_bonus(data:BonusRequest):
    bonus = grant_bonus(data)

    return{
        "user_id":data.user_id,
        "order_id":data.order_id,
        "bonus_amount":bonus
    }