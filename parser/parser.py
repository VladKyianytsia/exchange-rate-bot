import requests
from bs4 import BeautifulSoup


def get_exchange_rate():
    res = requests.get("https://www.google.com/finance/quote/USD-UAH?hl=uk")
    soup = BeautifulSoup(res.content, "html.parser")
    exchange_rate = soup.find("div", {"jsname": "LXPcOd"}).find("div").text

    return float(exchange_rate.replace(",", "."))
