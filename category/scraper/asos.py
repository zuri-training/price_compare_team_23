from scraper_api import ScraperAPIClient
from bs4 import BeautifulSoup
# import aiohttp
# import asyncio


def asos_scraper_bot(key):
    client = ScraperAPIClient('336a156effbd79b23a86d3f1c3f46988')
    result = client.get(url='https://www.asos.com/search/?q='+key)
    page_web = BeautifulSoup(result.text, 'html.parser')

    articles = page_web.find_all(
        'a', attrs={'class': '_3TqU78D'})
    items = []
    for article in articles:
        item = {}
        try:
            item['link'] = article['href']
            item['image'] = 'https:' + article.find('img')['src']
            item['title'] = article.find(
                'div', attrs={'class': '_3J74XsK'}).find('p').text
            item['price'] = article.find(
                'span', attrs={'class': '_16nzq18'}).text
            item['from'] = 'asos'
            items.append(item)
        except Exception:
            pass

    return items


# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()


# async def asos_scraper_bot_async(key):
#     # client = ScraperAPIClient('336a156effbd79b23a86d3f1c3f46988')
#     # result = client.get(url=url)
#     url = 'https://www.asos.com/search/?q='+key
#     async with aiohttp.ClientSession() as session:
#         reponse_page = await fetch(session, url)
#         page_web = BeautifulSoup(reponse_page, 'html.parser')

#         articles = page_web.find_all(
#             'a', attrs={'class': '_3TqU78D'})
#         items = []
#         for article in articles:
#             item = {}
#             try:
#                 item['link'] = article['href']
#                 item['image'] = 'https:' + article.find('img')['src']
#                 item['title'] = article.find(
#                     'div', attrs={'class': '_3J74XsK'}).find('p').text
#                 item['price'] = article.find(
#                     'span', attrs={'class': '_16nzq18'}).text
#                 item['from'] = 'asos'
#                 items.append(item)
#             except Exception:
#                 pass

#         return items


if __name__ == '__main__':
    asos_scraper_bot('sneakers')