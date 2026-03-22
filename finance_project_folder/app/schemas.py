from pydantic import BaseModel

class BonusRequest(BaseModel):
    user_id: str
    order_id: str
    order_total: float