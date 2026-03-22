from sqlalchemy import Column,Integer,String,Float
from .database import Base

class Reward(Base):
    __tablename__ = "rewards"

    id = Column(Integer,primary_key=True, index = True)
    user_id = Column(String)
    order_id = Column(String, unique=True)
    order_total = Column(Float)
    bonus_amount = Column(Float)