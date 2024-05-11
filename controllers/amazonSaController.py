#Dependencies
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession


async def scrape_amazonSa_full(url: str) -> dict:
    success = False
    i=0
    while not success and i<1000:
        try:
            i+=1
            asession=AsyncHTMLSession(
                mock_browser=True,
            )
            response = await asession.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            #Data
            price = soup.select_one('.aok-align-center span.a-price-whole').get_text().split(".")[0]
            title = soup.select_one('span.product-title-word-break').get_text().strip()
            rating = soup.select_one('#averageCustomerReviews_feature_div span.a-color-base').get_text().strip()
            discription = soup.select_one('ul.a-spacing-mini').get_text().strip()

            item_data = {
                "title": title,
                "price": price,
                "rating": rating,
                "description": discription,
            }
            return item_data
        except:
            return []
async def scrape_amazonSa_price(url: str) -> dict:
    success = False
    i=0
    while not success and i<1000:
        try:
            i+=1
            asession=AsyncHTMLSession(
                mock_browser=True,
            )
            response = await asession.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            #Data
            price = soup.select_one('.aok-align-center span.a-price-whole').get_text().split(".")[0]
            item_data = {
                "price": price,
            }
            return item_data
        except:
            return []
async def scrape_amazonSa_images(url: str) -> dict:
    success = False
    i=0
    while not success and i<1000:
        try:
            i+=1
            asession=AsyncHTMLSession(
                mock_browser=True,
            )
            response = await asession.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            result=soup.select("#imageBlock img")
            images=[]
            for i in result:
                if 'data-a-dynamic-image' in i.attrs:
                    images= eval(i['data-a-dynamic-image'])
                    images = list(images.keys())
            success = True
            item_data = {
                "images": images
            }
            return item_data
        except:
            return await scrape_amazonSa_images(url)

   