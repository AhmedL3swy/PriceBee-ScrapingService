#Dependencies
from bs4 import BeautifulSoup
import requests
from models.Product import ProductDetailDTO

async def scrape_amazon_full(url: str) -> dict:
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, 'html.parser')
    price = float(soup.select_one('span.a-offscreen').get_text().strip().replace('$',''))
    title = soup.select_one('span.a-size-large').get_text().strip()
    rating = soup.select_one('#averageCustomerReviews_feature_div span.a-color-base').get_text().strip()
    discription = soup.select_one('.a-spacing-mini span.a-list-item').get_text().strip()
    soup_images = soup.select("#imageBlock img")
    images = []
    for i in soup_images:
        if 'data-a-dynamic-image' in i.attrs:
            images = eval(i['data-a-dynamic-image'])
            images = list(images.keys())
    item_data = ProductDetailDTO(name_Global=title, price=price, rating=rating, description_Global=discription,images=images,productlink1=url)
    return item_data






















# async def scrape_amazon_price(url: str) -> dict:
#     # configure the request to be from Saudi Arabia
#     response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
#     soup = BeautifulSoup(response.content, 'html.parser')
#     #Data
#     price = soup.select_one('span.a-offscreen').get_text().strip()

#     item_data = ItemPrice(price=price)
#     return item_data

# async def scrape_amazon_images(url: str) -> dict:
#      # configure the request to be from Saudi Arabia
#     response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
#     soup = BeautifulSoup(response.content, 'html.parser')
#     result=soup.select("#imageBlock img")
#     for i in result:
#         if 'data-a-dynamic-image' in i.attrs:
#             images= eval(i['data-a-dynamic-image'])
#             images = list(images.keys())
#     item_data= ItemImages(images=images)
#     return item_data