import pandas as pd

from db.engine import SessionLocal
from db.models import ExchangeRate


FILE_PATH = "../exchange_rates.xlsx"


def add_exchange_rate_to_db(rate: float) -> None:
    session = SessionLocal()
    new_rate = ExchangeRate(exchange_rate=rate)
    session.add(new_rate)
    session.commit()
    session.close()


def generate_exchange_rates_xlsx() -> str:
    session = SessionLocal()
    rates = session.query(ExchangeRate).all()
    session.close()

    data = {
        "ID": [rate.id for rate in rates],
        "Rate": [rate.exchange_rate for rate in rates],
        "Date": [rate.date.strftime('%d.%m.%Y %H:%M:%S') for rate in rates],
    }
    df = pd.DataFrame(data)
    file_path = FILE_PATH
    df.to_excel(file_path, index=False)
    return file_path
