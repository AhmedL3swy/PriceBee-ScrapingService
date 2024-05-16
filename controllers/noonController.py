import time
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
from models.Product import ItemData, ItemImages, ItemPrice

async def scrape_noon_full(url: str) -> dict:
    start_time = time.time()
    asession = AsyncHTMLSession()
    response = await asession.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('h1').get_text().strip()
    price = soup.find('div', class_='priceNow').get_text().split('.')[0].strip()
    rating = soup.find('div', class_='sc-e7071e85-2').get_text().strip()
    description = soup.find('div', class_='sc-97eb4126-2').get_text().strip()
    image_soup = soup.find_all('img')
    img=[]
    for i in image_soup:
        if "&width" in i['src']:
            img.append(i['src'])
    end_time = time.time()
    item_data = ItemData(title=title, price=price, rating=rating, description=description, images=img)
    return item_data

async def scrape_noon_price(url: str) -> dict:
    start_time = time.time()
    asession = AsyncHTMLSession()
    response = await asession.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    price = soup.find('div', class_='priceNow').get_text().split('.')[0].strip()

    end_time = time.time()
    elapsed_time = end_time - start_time

    item_data = ItemPrice(price=price)
    return item_data

async def scrape_noon_images(url: str) -> dict:
    asession = AsyncHTMLSession()
    response = await asession.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    result= soup.select('img')
    img=[]
    for i in result:
        if "&width" in i['src']:
            img.append(i['src'])
    item_data = ItemImages(images=img)
    return item_data