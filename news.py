import requests
from config import NEWS_API_KEY

def get_news():
    url = f"https://newsapi.org/v2/everything?q=stock india&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    return [a["title"] for a in res["articles"][:5]]


def get_order_news():
    url = f"https://newsapi.org/v2/everything?q=order win OR contract india&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    return [a["title"] for a in res["articles"][:5]]