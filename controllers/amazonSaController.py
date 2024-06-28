#Dependencies
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
from models.Product import  ProductDetailDTO


async def scrape_amazonSa_full(url: str) -> dict:
    asession=AsyncHTMLSession(
        mock_browser=True,
    )
    response = await asession.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    #Data
    price = float(soup.select_one('.aok-align-center span.a-price-whole').get_text().split(".")[0])
    title = soup.select_one('span.product-title-word-break').get_text().strip()
    rating = soup.select_one('#averageCustomerReviews_feature_div span.a-color-base').get_text().strip()
    discription = soup.select_one('ul.a-spacing-mini').get_text().strip()
    soup_images = soup.select("#imageBlock img")
    images = []
    for i in soup_images:
        if 'data-a-dynamic-image' in i.attrs:
            images = eval(i['data-a-dynamic-image'])
            images = list(images.keys())
    
    item_data = ProductDetailDTO(name_Global=title, price=price, rating=rating, description_Global=discription,images=images,productlink1=url)
    return item_data


















# async def scrape_amazonSa_price(url: str) -> dict:
#     asession=AsyncHTMLSession(
#         mock_browser=True,
#     )
#     response = await asession.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     #Data
#     price = soup.select_one('.aok-align-center span.a-price-whole').get_text().split(".")[0]
#     item_data = ItemPrice(price=price)
#     return item_data

# async def scrape_amazonSa_images(url: str) -> dict:
#     asession=AsyncHTMLSession(
#         mock_browser=True,
#     )
#     response = await asession.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     result=soup.select("#imageBlock img")
#     images=[]
#     for i in result:
#         if 'data-a-dynamic-image' in i.attrs:
#             images= eval(i['data-a-dynamic-image'])
#             images = list(images.keys())
#     item_data= ItemImages(images=images)
#     return item_data
       

   