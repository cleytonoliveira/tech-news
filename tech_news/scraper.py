from parsel import Selector
import requests
from requests.exceptions import HTTPError, ReadTimeout
import time


# Requisito 1
def fetch(url):
    """Faz requisição para a url desejada"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.text
    except ReadTimeout:
        return None
    except HTTPError:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Busca informações do site"""
    selector = Selector(html_content)
    url = selector.css('[rel="canonical"]::attr(href)').get()
    title = selector.css('.tec--article__header__title::text').get()
    timestamp = selector.css('#js-article-date::attr(datetime)').get()

    writer = selector.css('.tec--author__info__link::text').get().strip()
    shares_count = int(
        selector.css('.tec--toolbar__item::text').get().split()[0]
    )
    comments_count = int(selector.css('.tec--btn::attr(data-count)').get())
    summary = ''.join(
        selector.css('.tec--article__body p:first-child *::text')
        .getall()
    )
    sources = [
        space.strip()
        for space in selector.css('[rel="noopener nofollow"]::text')
        .getall()
    ]
    categories = [
        space.strip()
        for space in selector.css('#js-categories a::text')
        .getall()
    ]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 3
def scrape_novidades(html_content):
    """Busca os links das novidades"""
    try:
        selector = Selector(html_content)
        url_list = selector.css('h3.tec--card__title a::attr(href)').getall()
        return url_list
    except HTTPError:
        return []


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
