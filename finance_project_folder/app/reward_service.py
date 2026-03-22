from .models import Reward
from .database import sessionLocal

def grant_bonus(data):
    db = sessionLocal()
    existing = db.query(Reward).filter(Reward.order_id == data.order_id).first()

    if existing:
        return existing.bonus_amount
    
    bonus = data.order_total * 0.30
    #30 percent means 0.30 
    reward = Reward(user_id=data.user_id,
                    order_id = data.order_id,
                    order_total = data.order_total,
                    bonus_amount = bonus)
    
    db.add(reward)
    db.commit()

    return bonus
