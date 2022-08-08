from scraper_api import ScraperAPIClient
from django.utils.text import slugify
from bs4 import BeautifulSoup
import json


def query_slugify(value, seperator="-"):
    v = value.split(" ", 3)
    val = ""
    for i in range(0, 3):
        val += v[i] + " "
    return slugify(val).replace("-", seperator)


def konga_category(category: str):
    """@category : string
    -> konga category : string
    """
    switch = {
        "smartphones": "smartphones-7539",
        "laptops": "ultrabooks-5253",
        "desktop-computers": "desktop-bundles-5242",
        "television": "televisions-5266",
        "smart-tvs": "smart-tvs-7773",
        "digital-cameras": "digital-cameras-5276",
        "generators": "generators-1184",
    }
    return switch.get(category.lower(), "")


def konga_scraper_bot(key):
    product_link = "http://www.konga.com/"
    image_link = "https://www-konga-com-res.cloudinary.com/w_auto,f_auto,fl_lossy,dpr_auto,q_auto/media/catalog/product"
    client = ScraperAPIClient("fc0603cdc494888c3873340b62d7b5ce")
    result = client.get(url="https://www.konga.com/search?search=" + key)
    page_web = BeautifulSoup(result.text, "html.parser")

    articles = page_web.find("script", attrs={"id": "__NEXT_DATA__"})
    json_data = json.loads(articles.text)

    articles = json_data["props"]["initialProps"]["pageProps"]["resultsState"][
        "_originalResponse"
    ]["results"][0]["hits"]

    items = []
    for article in articles:
        item = {}
        item["link"] = product_link + article["url_key"]
        item["image"] = image_link + article["image_thumbnail_path"]
        item["name"] = article["name"]
        item["price"] = "₦" + str(article["price"])
        item["platform_name"] = "konga"
        item["brand"] = article["brand"]

        items.append(item)

    return items


if __name__ == "__main__":
    konga_scraper_bot("computer")
