import requests
from bs4 import BeautifulSoup
from celery import Celery

from db.actions import add_exchange_rate_to_db

EXCHANGE_RATE_URL = "https://www.google.com/finance/quote/USD-UAH?hl=uk"

celery_app = Celery("parser", broker="redis://localhost")
celery_app.conf.broker_connection_retry_on_startup = True


@celery_app.task
def get_exchange_rate() -> None:
    res = requests.get(EXCHANGE_RATE_URL)
    soup = BeautifulSoup(res.content, "html.parser")
    exchange_rate = soup.find("div", {"jsname": "LXPcOd"}).find("div").text

    add_exchange_rate_to_db(float(exchange_rate.replace(",", ".")))


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(3600.0, get_exchange_rate.s())
