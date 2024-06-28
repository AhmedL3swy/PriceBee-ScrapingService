from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
from models.Product import ProductDetailDTO
from fake_headers import Headers


async def scrape_noon_full(url: str) -> dict:
    asession = AsyncHTMLSession()
    try:
     response = await asession.get(url,timeout=10)
    except:
        raise Exception("timeout")
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1').get_text().strip()
    price = float(soup.find('div', class_='priceNow').get_text().split('.')[0].strip())
    rating = soup.find('div', class_='sc-e7071e85-2').get_text().strip()
    description = soup.find('div', class_='sc-97eb4126-2').get_text().strip()
    image_soup = soup.find_all('img')
    img=[]
    for i in image_soup:
        if "&width" in i['src']:
            img.append(i['src'])
    item_data = ProductDetailDTO(name_Global=title, price=price, rating=rating, description_Global=description,images=img,productlink1=url)
    return item_data


































# async def scrape_noon_price(url: str) -> dict:
#     headers = Headers(headers=True).generate()
#     asession = AsyncHTMLSession()
#     try:
#      response = await asession.get(url, headers=headers,timeout=10)
#     except:
#         return {"error": "timeout"}
#     soup = BeautifulSoup(response.content, 'html.parser')

#     price = soup.find('div', class_='priceNow').get_text().split('.')[0].strip()


#     item_data = ItemPrice(price=price)
#     return item_data

# async def scrape_noon_images(url: str) -> dict:
#     headers = Headers(headers=True).generate()
#     asession = AsyncHTMLSession()
#     try:
#      response = await asession.get(url, headers=headers,timeout=10)
#     except:
#         return {"error": "timeout"}   
#     soup = BeautifulSoup(response.content, 'html.parser')
#     result= soup.select('img')
#     img=[]
#     for i in result:
#         if "&width" in i['src']:
#             img.append(i['src'])
#     item_data = ItemImages(images=img)
#     return item_data