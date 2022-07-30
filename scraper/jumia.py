import requests
from django.utils.text import slugify
from bs4 import BeautifulSoup

#use + instead of - for the search query
def query_slugify(value, seperator='-'):
    return slugify(value).replace('-', seperator)

def jumia_category(category):
    switch = {
        'smartphones':'smartphones' ,
        'laptops':'laptops',
        'desktop-computers':'desktop-computers',
        'television':'television',
        'smart-tvs':'smart-tvs',
        'digital-cameras':'digital-cameras',
        'generators':'generators'
    }

    return switch.get(category.lower(),"")



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

    prd_category = jumia_category(product['category'])
    phones = []
    page = 1
    while page <= 1:
        URL = f"https://www.jumia.com.ng/{prd_category}/?q={query_slugify(product['name'])}&sort=lowest-price&page={page}"
        response = requests.get(URL)
        parsed_response = BeautifulSoup(response.text,'html.parser')
        for tag in parsed_response.find_all(class_="prd"):
            phones.append(
                {
                    'name': tag.a.find(class_='name').get_text(),
                    'brand': tag.a.get('data-brand'),
                    'price': tag.a.find(class_='prc').get_text(),
                    'link': tag.a.get('href'),
                    'img_src': tag.a.find('img')['data-src'],
                    'platform_name': 'jumia'
                }
            )
        page += 1
    for phone in phones:
        if product['name'].lower() in phone['name'].lower() and product['brand'].lower() in phone['brand'].lower():
            return phone



def jumia_scraper_bot(key):
    link = "https://kol.jumia.com/api/click/link/29315728-22fa-420d-94a9-2a87c22ca25c/16a93b99-b499-4fab-b4e7-60d8f58dd09f"
    url = "https://www.jumia.ng/catalog/?q=" + key

    reponse_page = requests.get(url)

    page_web = BeautifulSoup(reponse_page.content, 'html.parser')

    articles = page_web.find_all(
        'article', attrs={'class': 'prd _fb col c-prd'})

    items = []
    for article in articles:
        item = {}
        item['link'] = link + article.find('a')['href']
        item['image'] = article.find('img')['data-src']
        item['title'] = article.find('h3', attrs={'class': 'name'}).text
        item['price'] = article.find('div', attrs={'class': 'prc'}).text
        item['from'] = 'jumia'
        if item['price']:
            items.append(item)

    return items



if __name__ == '__main__':
    jumia_scraper_bot('computer')