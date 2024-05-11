#Dependencies
from bs4 import BeautifulSoup
import requests

async def scrape_amazon_full(url: str) -> dict:
     # configure the request to be from Saudi Arabia
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, 'html.parser')
    #Data
    price = soup.select_one('span.a-offscreen').get_text().strip()
    title = soup.select_one('span.a-size-large').get_text().strip()
    rating = soup.select_one('#averageCustomerReviews_feature_div span.a-color-base').get_text().strip()
    discription = soup.select_one('.a-spacing-mini span.a-list-item').get_text().strip()

    item_data = {
        "title": title,
        "price": price,
        "rating": rating,
        "description": discription,
    }
    return item_data

async def scrape_amazon_price(url: str) -> dict:
    # configure the request to be from Saudi Arabia
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, 'html.parser')
    #Data
    price = soup.select_one('span.a-offscreen').get_text().strip()

    item_data = {
        "price": price,
    }
    return item_data

async def scrape_amazon_images(url: str) -> dict:
     # configure the request to be from Saudi Arabia
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, 'html.parser')
    result=soup.select("#imageBlock img")
    for i in result:
        if 'data-a-dynamic-image' in i.attrs:
            images= eval(i['data-a-dynamic-image'])
            images = list(images.keys())
    item_data = {
        "images": images
    }
    return item_data