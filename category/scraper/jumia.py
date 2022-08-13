import requests
from django.utils.text import slugify
from bs4 import BeautifulSoup

# use + instead of - for the search query
def query_slugify(value, seperator="-"):
    v = value.split(" ", 3)
    val = ""
    for i in range(0, 3):
        val += v[i] + " "
    return slugify(val).replace("-", seperator)


def jumia_category(category):
    switch = {
        "smartphones": "smartphones",
        "laptops": "laptops",
        "desktop-computers": "desktop-computers",
        "television": "television",
        "smart-tvs": "smart-tvs",
        "digital-cameras": "digital-cameras",
        "generators": "generators",
    }

    return switch.get(category.lower(), "")


def get_jumia_products():
    """
    argument is a dictionary with name and brand e.g {
        'name',
        'brand'
    }

    returns a dictionary with name, price , link and img_src e.g {
        'name',
        'price',
        'link',
        'img_src',
        'platform name'
    }
    """

    # return {
    #     'name': 'samsung',
    #     'price': 'N 33,000',
    #     'link': 'samsung/jumia.com',
    #     'img_src': 'somewher.jpg'
    # }

    phones = []
    page = 1
    while page <= 5:
        URL = f"https://www.jumia.com.ng/smartphones/&sort=lowest-price&page={page}"
        response = requests.get(URL)
        parsed_response = BeautifulSoup(response.text, "html.parser")
        for tag in parsed_response.find_all(class_="prd"):
            if tag.a.get("data-brand") != None:
                phones.append(
                    {
                        "name": tag.a.find(class_="name").get_text(),
                        "brand": tag.a.get("data-brand"),
                        "price": tag.a.find(class_="prc").get_text(),
                        "link": tag.a.get("href"),
                        "image_src": tag.a.find("img")["data-src"],
                        "platform_name": "jumia",
                    }
                )
        page += 1
    return phones


def get_jumia_product(product):
    """
    argument is a dictionary with name and brand e.g {
        'name',
        'brand'
    }

    returns a dictionary with name, price , link and img_src e.g {
        'name',
        'price',
        'link',
        'img_src',
        'platform name'
    }
    """

    # return {
    #     'name': 'samsung',
    #     'price': 'N 33,000',
    #     'link': 'samsung/jumia.com',
    #     'img_src': 'somewher.jpg'
    # }

    prd_category = jumia_category(product["category"])
    phones = []
    page = 1
    while page <= 2:
        URL = f"https://www.jumia.com.ng/{prd_category}/?page={page}"
        response = requests.get(URL)
        parsed_response = BeautifulSoup(response.text, "html.parser")
        for tag in parsed_response.find_all(class_="prd"):
            if (
                product["name"].lower() in tag.a.find(class_="name").get_text().lower()
                and product["brand"].lower() in tag.a.get("data-brand").lower()
            ):
                return {
                    "name": tag.a.find(class_="name").get_text(),
                    "brand": tag.a.get("data-brand"),
                    "price": tag.a.find(class_="prc").get_text(),
                    "link": "https://jumia.com.ng" + tag.a.get("href"),
                    "image_src": tag.a.find("img")["data-src"],
                    "platform_name": "jumia",
                }

    #         phones.append(
    #             {
    #                 'name': tag.a.find(class_='name').get_text(),
    #                 'brand': tag.a.get('data-brand'),
    #                 'price': tag.a.find(class_='prc').get_text(),
    #                 'link': tag.a.get('href'),
    #                 'img_src': tag.a.find('img')['data-src'],
    #                 'platform_name': 'jumia'
    #             }
    #         )
    #     page += 1
    # for phone in phones:
    #     print(phone)
    #     if product['name'].lower() in phone['name'].lower() and product['brand'].lower() in phone['brand'].lower():
    #         return phone
    #     for tag in parsed_response.find_all(class_="prd _fb col c-prd"):
    #         link = 'https://www.jumia.com.ng/'
    #         phones.append(
    #             {
    #                 'name': tag.a.find(class_='name').get_text(),
    #                 'brand': tag.a.get('data-brand'),
    #                 'price': tag.find('div', attrs={'class': 'prc'}).text,
    #                 'link': link+tag.find('a')['href'],
    #                 'img_src': tag.a.find('img')['data-src'],
    #                 'platform_name': 'jumia'
    #             }
    #         )
    #     page += 1
    # for phone in phones:
    #     if product['name'].lower() in phone['name'].lower() and product['brand'].lower() in phone['brand'].lower():
    #         return phone


def jumia_scraper_bot(key):
    link = "https://jumia.com.ng/"
    url = "https://www.jumia.com.ng/mobile-phones/" + key

    reponse_page = requests.get(url)

    page_web = BeautifulSoup(reponse_page.content, "html.parser")

    articles = page_web.find_all("article", attrs={"class": "prd _fb col c-prd"})

    items = []
    for article in articles:
        item = {}
        item["link"] = link + article.find("a")["href"]
        item["image"] = article.find("img")["data-src"]
        item["title"] = article.find("h3", attrs={"class": "name"}).text
        item["price"] = article.find("div", attrs={"class": "prc"}).text
        item["category"] = article.find("a")["data-category"]
        item["brand"] = article.find("a")["data-brand"]
        item["from"] = "jumia"
        if item["price"]:
            items.append(item)

    return items


if __name__ == "__main__":
    jumia_scraper_bot("computer")
