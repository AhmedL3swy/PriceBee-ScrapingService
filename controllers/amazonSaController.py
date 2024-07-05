#Dependencies
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
from models.Product import  ProductDetailDTO


async def scrape_amazonSa_full(url):
    success = False
    attempts = 0

    while not success and attempts < 100:
        try:
            asession = AsyncHTMLSession(mock_browser=True)
            if "language=en_AE" in url:
                url = url.replace("&language=en_AE", "")
            response = await asession.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Data
            price_element = soup.select_one('.aok-align-center span.a-price-whole')
            price = float(price_element.get_text().split(".")[0].replace(",", "")) 
            title_element = soup.select_one('span.product-title-word-break')
            title = title_element.get_text().strip() if title_element else ""
            rating_element = soup.select_one('#averageCustomerReviews_feature_div span.a-color-base')
            rating = float(rating_element.get_text().strip()) if rating_element else 0.0
            description_element = soup.select_one('ul.a-spacing-mini')
            description = description_element.get_text().strip() if description_element else ""

            # Get all data from table where selector table.a-spacing-micro
            table = soup.select_one('table.a-normal.a-spacing-micro')
            table_data = {}
            if table:
                for tr in table.select('tr'):
                    key_element = tr.select_one('td.a-span3 span.a-size-base.a-text-bold')
                    value_element = tr.select_one('td.a-span9 span.a-size-base.po-break-word')
                    if key_element and value_element:
                        key = key_element.get_text().strip()
                        value = value_element.get_text().strip()
                        table_data[key] = value

            # Concat table data into string
            table_data_str = "|".join([f"{key} : {value}" for key, value in table_data.items()])

            # Get images
            images = []
            soup_images = soup.select("#imageBlock img")
            for i in soup_images:
                if 'data-a-dynamic-image' in i.attrs:
                    images = eval(i['data-a-dynamic-image'])
                    images = list(images.keys())
            #sleep for 1 second
            url = url + '&language=en_AE&th=1'
            response = await asession.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Global data
            G_title_element = soup.select_one('span.product-title-word-break')
            G_title = G_title_element.get_text().strip() if G_title_element else ""
            G_table_data = {}
            table = soup.select_one('table.a-normal.a-spacing-micro')
            if table:
                for tr in table.select('tr'):
                    key_element = tr.select_one('td.a-span3 span.a-size-base.a-text-bold')
                    value_element = tr.select_one('td.a-span9 span.a-size-base.po-break-word')
                    if key_element and value_element:
                        key = key_element.get_text().strip()
                        value = value_element.get_text().strip()
                        G_table_data[key] = value

            # Concat global table data into string
            G_table_data_str = "|".join([f"{key} : {value}" for key, value in G_table_data.items()])

            domainId = 4
            if "amazon.eg" in url:
                domainId = 3

            success = True

            return ProductDetailDTO(
                domainId=domainId,
                name_Global=G_title,
                name_Local=title,
                is_available=1,
                price=price,
                rating=rating,
                description_Global=G_table_data_str,
                description_Local=table_data_str,
                images=images,
                productlink1=url
            )
        except Exception as e:
            attempts += 1
            pass
    return None



# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# #Dependencies
# from bs4 import BeautifulSoup
# async def scrape_amazonSa_full(url: str) -> dict:
#     options = Options()
#     options.add_argument("--headless")  # Run Chrome in headless mode
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     # just go to url and get the page source
#     with webdriver.Chrome(options=options) as driver:
#         driver.get(url)
#     # wait for the page to load
#         WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, 'body'))
#         )
#         # get the page source
#         page_source = driver.page_source
#         driver.quit()
#         soup = BeautifulSoup(page_source, 'html.parser')
#         price = soup.select_one('.aok-align-center span.a-price-whole').get_text().split(".")[0]
#         title = soup.select_one('span.product-title-word-break').get_text().strip()
#         rating = soup.select_one('#averageCustomerReviews_feature_div span.a-color-base').get_text().strip()
#         discription = soup.select_one('ul.a-spacing-mini').get_text().strip()
#         #get all data from table where selector table.a-spacing-micro
#         table = soup.select_one('table.a-normal.a-spacing-micro')
#         table_data = {}
#         if table:
#             for tr in table.select('tr'):
#                 key = tr.select_one('td.a-span3 span.a-size-base.a-text-bold').get_text().strip()
#                 value = tr.select_one('td.a-span9 span.a-size-base.po-break-word').get_text().strip()
#                 table_data[key] = value
#         ## Concat table data into string
#         table_data = "|".join([f"{key} : {value}" for key, value in table_data.items()])
#         images = []
#         soup_images = soup.select("#imageBlock img")
#         for i in soup_images:
#             if 'data-a-dynamic-image' in i.attrs:
#                 images = eval(i['data-a-dynamic-image'])
#                 images = list(images.keys())
#         table = soup.select_one('table.a-normal.a-spacing-micro')
#         table_data = {}
#         if table:
#             for tr in table.select('tr'):
#                 key = tr.select_one('td.a-span3 span.a-size-base.a-text-bold').get_text().strip()
#                 value = tr.select_one('td.a-span9 span.a-size-base.po-break-word').get_text().strip()
#                 table_data[key] = value
#         domainId=4
#         if (url.find("eg")!=-1):
#             domainId=3
#         ## Concat table data into string
#         table_data = "|".join([f"{key} : {value}" for key, value in table_data.items()])
#         return ProductDetailDTO(domainId=domainId,name_Global=title,name_Local=title,is_available=1, price=price, rating=rating, description_Global=table_data,images=images,productlink1=url)
















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
       

   