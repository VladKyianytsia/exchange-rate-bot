from sqlalchemy import Column, Integer, DateTime, Float, func
from sqlalchemy.orm import declarative_base

from db.engine import engine

Base = declarative_base()


class ExchangeRate(Base):
    __tablename__ = "exchange_rate"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=func.now())
    exchange_rate = Column(Float)


def db_init() -> None:
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    db_init()
