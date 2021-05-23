from tech_news.database import search_news
from requests.exceptions import HTTPError
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Busca pelo título"""
    try:
        news_by_title = search_news({
            "title": {"$regex": title, "$options": 'i'}
        })
        return [(new["title"], new["url"]) for new in news_by_title]
    except HTTPError:
        return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        format = "%Y-%m-%d"
        datetime.strptime(date, format)
        news_by_date = search_news({
            "timestamp": {"$regex": date}
        })
        return [(new["title"], new["url"]) for new in news_by_date]
    except ValueError:
        raise ValueError("Data inválida")
    except HTTPError:
        return []


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
