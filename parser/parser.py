import requests
from bs4 import BeautifulSoup


EXCHANGE_RATE_URL = "https://www.google.com/finance/quote/USD-UAH?hl=uk"


def get_exchange_rate() -> float:
    res = requests.get(EXCHANGE_RATE_URL)
    soup = BeautifulSoup(res.content, "html.parser")
    exchange_rate = soup.find("div", {"jsname": "LXPcOd"}).find("div").text

    return float(exchange_rate.replace(",", "."))
