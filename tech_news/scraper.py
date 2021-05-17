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
    except requests.ReadTimeout:
        return None
    except requests.HTTPError:
        return None


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
