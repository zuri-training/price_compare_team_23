import requests
from scraper_api import ScraperAPIClient
# import aiohttp
# import asyncio
from bs4 import BeautifulSoup


def ebay_scraper_bot(key):
    link = "https://kol.jumia.com/api/click/link/29315728-22fa-420d-94a9-2a87c22ca25c/16a93b99-b499-4fab-b4e7-60d8f58dd09f"
    url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=computer+hp&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=computer+hp"

    client = ScraperAPIClient('336a156effbd79b23a86d3f1c3f46988')
    result = client.get(url=url)
    page_web = BeautifulSoup(result.text, 'html.parser')

    print(page_web)
    articles = page_web.find_all(
        'article', attrs={'class': 's-item__wrapper clearfix'})

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
    print(len(items))
    return items


# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()


# async def jumia_scraper_bot_async(key):
#     link = "https://www.jumia.ng"
#     url = "https://www.jumia.ng/catalog/?q=" + key

#     async with aiohttp.ClientSession() as session:
#         reponse_page = await fetch(session, url)

#         page_web = BeautifulSoup(reponse_page, 'html.parser')

#         articles = page_web.find_all(
#             'article', attrs={'class': 'prd _fb col c-prd'})

#         items = []
#         for article in articles:
#             item = {}
#             item['link'] = link + article.find('a')['href']
#             item['image'] = article.find('img')['data-src']
#             item['title'] = article.find('h3', attrs={'class': 'name'}).text
#             item['price'] = article.find('div', attrs={'class': 'prc'}).text
#             item['from'] = 'jumia'
#             if item['price']:
#                 items.append(item)

#         return items


if __name__ == '__main__':
    ebay_scraper_bot('computer')