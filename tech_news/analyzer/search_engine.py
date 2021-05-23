from tech_news.database import search_news
from requests.exceptions import HTTPError


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
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


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
