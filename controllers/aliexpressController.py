#Dependencies
from bs4 import BeautifulSoup
import requests
import json
from utils import getStringBetweenTwoWords
from models.Product import ProductDetailDTO

async def scrape_aliexpress_full(url: str) -> dict:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    script_tag = soup.find('script')
    if script_tag:
        script_content = script_tag.string
        script_target_object= getStringBetweenTwoWords(script_content, 'window.runParams =', 'window.runParams.is23').replace(';', '')
        script_target_object = script_target_object.replace('data', '"data"')
        script_target_object = json.loads(script_target_object)
        price = script_target_object['data']['metaDataComponent']['ogTitle'].split('|')[0].strip()
        title = script_target_object['data']['metaDataComponent']['title'].split('|')[0].strip()
        ImageList = script_target_object['data']['imageComponent']['imagePathList']

    item_data = ProductDetailDTO(name_Global=title, price=price,images=ImageList,productlink1=url)
    return item_data
























# async def scrape_aliexpress_price(url: str) -> dict:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     script_tag = soup.find('script')
#     if script_tag:
#         script_content = script_tag.string
#         script_target_object= getStringBetweenTwoWords(script_content, 'window.runParams =', 'window.runParams.is23').replace(';', '')
#         script_target_object = script_target_object.replace('data', '"data"')
#         script_target_object = json.loads(script_target_object)
#         price = script_target_object['data']['metaDataComponent']['ogTitle'].split('|')[0].strip()
#     item_data = ItemPrice(price=price)
#     return item_data

# async def scrape_aliexpress_images(url: str) -> dict:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     script_tag = soup.find('script')
#     if script_tag:
#         script_content = script_tag.string
#         script_target_object= getStringBetweenTwoWords(script_content, 'window.runParams =', 'window.runParams.is23').replace(';', '')
#         script_target_object = script_target_object.replace('data', '"data"')
#         script_target_object = json.loads(script_target_object)
#         ImageList = script_target_object['data']['imageComponent']['imagePathList']
#     item_data = ItemImages(images=ImageList)
#     return item_data