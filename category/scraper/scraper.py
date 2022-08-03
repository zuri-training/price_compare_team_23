import requests
from bs4 import BeautifulSoup
from category.models import Product

# import schedule
import time


# this base url is what each has in common in the href

# container for the extract links
def jumia_scraper_bot(key):
    # browser agent settings
    headers = {
        "X-RapidAPI-Key": "6b28618dc7mshaab549a1ca56647p1f7cafjsnddabc557ad37",
        "X-RapidAPI-Host": "jumia-service.p.rapidapi.com",
    }
    # if you want the whole jumia phones increase the page range below max=50
    for page in range(1, 55, 1):
        # request from jumia phone page1
        url = f"https://www.jumia.com.ng/mobile-{key}/?page={page}#catalog-listing"
        response = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(response.content, "lxml")
        # scrapping the reccurent div class
        product_list = soup.find_all("article", class_="prd _fb col c-prd")
        store = []

        # the code below will loop through the link and merge the base url with each product

        for article in product_list:
            item = {}
            item["name"] = article.find("a", class_="core")["data-brand"]
            item["properties"] = article.find("h3", class_="name").text
            link = article.find("a", href=True)["href"]
            item["link"] = f"https://www.jumia.com.ng{link}"
            item["price"] = article.find("div", class_="prc").text
            item["image"] = article.find("img")["data-src"]
            item["from"] = "Jumia"
            item["category"] = "electronics"
            if item["price"]:
                store.append(item)

        return store


# key ='mobile-phone'
# schedule.every(5).do(jumia_scraper_bot(key))
# while 1:
#     schedule.run_pending()
#     time.sleep(3600)
if __name__ == "__main__":
    jumia_scraper_bot("computer")
