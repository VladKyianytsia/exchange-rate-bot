from sqlalchemy import Column, Integer, DateTime, Float, func

from db.engine import Base, engine


class ExchangeRate(Base):
    __tablename__ = "exchange_rate"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=func.now())
    exchange_rate = Column(Float)


Base.metadata.create_all(engine)
