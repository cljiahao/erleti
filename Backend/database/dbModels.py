from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

class StockPrice(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    stockname = Column(String, unique=True, index=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volumne = Column(Float)
