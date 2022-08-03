from scraper_api import ScraperAPIClient
from bs4 import BeautifulSoup
import json
# import aiohttp
# import asyncio


def konga_scraper_bot(key):
    product_link = 'http://www.konga.com/?k_id=taiwokassim03'
    image_link = 'https://www-konga-com-res.cloudinary.com/w_auto,f_auto,fl_lossy,dpr_auto,q_auto/media/catalog/product'
    client = ScraperAPIClient('336a156effbd79b23a86d3f1c3f46988')
    result = client.get(url='https://www.konga.com/search?search='+key+'sort=asc')
    page_web = BeautifulSoup(result.text, 'html.parser')
    # print(page_web.prettify())

    articles = page_web.find(
        'script', attrs={'id': '__NEXT_DATA__'})
    json_data = json.loads(articles.text)

    articles = json_data['props']['initialProps']['pageProps']['resultsState']['_originalResponse']['results'][0]['hits']

    items = []
    for article in articles:
        item = {}
        item['link'] = product_link + article['url_key']
        item['image'] = image_link + article['image_thumbnail_path']
        item['title'] = article['name']
        item['price'] = '₦' + str(article['price'])
        
        items.append(item)

    print(len(items))

    return items


# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()


# async def konga_scraper_bot_async(key):
#     product_link = 'https://www.konga.com/product/'
#     image_link = 'https://www-konga-com-res.cloudinary.com/w_auto,f_auto,fl_lossy,dpr_auto,q_auto/media/catalog/product'
#     # client = ScraperAPIClient('336a156effbd79b23a86d3f1c3f46988')
#     url = 'https://www.konga.com/search?search='+key
#     # result = await client.get(url=url)

#     async with aiohttp.ClientSession() as session:
#         reponse_page = await fetch(session, url)

#         page_web = BeautifulSoup(reponse_page, 'html.parser')

#         articles = page_web.find(
#             'script', attrs={'id': '__NEXT_DATA__'})
#         json_data = json.loads(articles.string)

#         articles = json_data['props']['initialProps']['pageProps']['resultsState']['_originalResponse']['results'][0]['hits']

#         items = []
#         for article in articles:
#             item = {}
#             item['link'] = product_link + article['url_key']
#             item['image'] = image_link + article['image_thumbnail_path']
#             item['title'] = article['name']
#             item['price'] = '₦' + str(article['price'])
#             item['from'] = 'konga'
#             items.append(item)

#         print(len(items))

    # return items


if __name__ == '__main__':
    konga_scraper_bot('computer')