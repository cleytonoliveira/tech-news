from requests.exceptions import HTTPError, ReadTimeout
from tech_news.database import create_news
from parsel import Selector
import requests
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

    writer = selector.css('.tec--author__info__link::text').get()
    shares_count = selector.css('.tec--toolbar__item::text').get()
    comments_count = int(selector.css('.tec--btn::attr(data-count)').get())
    summary = ''.join(
        selector.css('.tec--article__body p:first-child *::text')
        .getall()
    )
    sources = [
        space.strip()
        for space in selector.css('.z--mb-16 .tec--badge::text')
        .getall()
    ]
    categories = [
        space.strip()
        for space in selector.css('#js-categories a::text')
        .getall()
    ]

    if writer is not None:
        writer = writer.strip()

    if shares_count is None:
        shares_count = 0
    else:
        shares_count = int(shares_count.split()[0])

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
    """Busca a url para a próxima página"""
    try:
        selector = Selector(html_content)
        next_page_link = selector.css('.tec--btn::attr(href)').get()
        return next_page_link
    except HTTPError:
        return None


# Requisito 5
def get_tech_news(amount):
    """Busca a quantidade de noticias solicitadas"""
    url = 'https://www.tecmundo.com.br/novidades'
    news_box = []

    while True:
        content_page = fetch(url)
        news_links = scrape_novidades(content_page)
        for link in news_links:
            url_news = fetch(link)
            news = scrape_noticia(url_news)
            news_box.append(news)
            if len(news_box) == amount:
                create_news(news_box)
                return news_box
        url = scrape_next_page_link(content_page)
