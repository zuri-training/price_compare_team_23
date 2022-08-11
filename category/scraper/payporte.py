from scraper_api import ScraperAPIClient
from bs4 import BeautifulSoup
import requests


def payporte_scraper_bot(key):
    url = "https://payporte.com/affiliate/index/index?u=961" + key
    reponse_page = requests.get(url)
    page_web = BeautifulSoup(reponse_page.content, "html.parser")
    articles = page_web.find_all("div", attrs={"class": "product-item-info"})

    items = []

    for article in articles:
        try:
            item = {}
            item["link"] = article.find("a")["href"]
            item["image"] = article.find("img")["src"]
            item["title"] = article.find("a", attrs={"class": "product-item-link"}).text
            item["price"] = ""
            if article.find("span", attrs={"class": "price"}):
                item["price"] = article.find("span", attrs={"class": "price"}).text
            item["from"] = "payporte"
            items.append(item)
        except Exception:
            pass

    print(len(items))
    return items


if __name__ == "__main__":
    payporte_scraper_bot("clothes")
