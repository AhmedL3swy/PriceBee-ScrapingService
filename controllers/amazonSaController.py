#Dependencies
# from bs4 import BeautifulSoup
# from requests_html import AsyncHTMLSession
from models.Product import  ProductDetailDTO


# async def scrape_amazonSa_full(url: str) -> dict:
#     attemps=10
#     asession=AsyncHTMLSession(
#         mock_browser=True,
#     )
#     response = await asession.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     #Data
#     while attemps > 0:
#         try:
#             price = float(soup.select_one('.aok-align-center span.a-price-whole').get_text().split(".")[0])
#             break
#         except:
#             attemps -= 1
#             asession = AsyncHTMLSession(mock_browser=True)
#             response = await asession.get(url)
#             soup = BeautifulSoup(response.content, 'html.parser')
#     price = float(soup.select_one('.aok-align-center span.a-price-whole').get_text().split(".")[0].replace(",",""))
#     title = soup.select_one('span.product-title-word-break').get_text().strip()
#     rating = soup.select_one('#averageCustomerReviews_feature_div span.a-color-base').get_text().strip()
#     discription = soup.select_one('ul.a-spacing-mini').get_text().strip()
#     soup_images = soup.select("#imageBlock img")
#     images = []
#     for i in soup_images:
#         if 'data-a-dynamic-image' in i.attrs:
#             images = eval(i['data-a-dynamic-image'])
#             images = list(images.keys())
    
#     item_data = ProductDetailDTO(name_Global=title, price=price, rating=rating, description_Global=discription,images=images,productlink1=url)
#     return item_data



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Dependencies
from bs4 import BeautifulSoup
async def scrape_amazonSa_full(url: str) -> dict:
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # just go to url and get the page source
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # wait for the page to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body'))
    )
    # get the page source
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    price =  float(soup.select_one('.aok-align-center span.a-price-whole').get_text().split(".")[0].replace(",",""))
    title = soup.select_one('span.product-title-word-break').get_text().strip()
    rating = float(soup.select_one('#averageCustomerReviews_feature_div span.a-color-base').get_text().strip())
    discription = soup.select_one('ul.a-spacing-mini').get_text().strip()
    #get all data from table where selector table.a-spacing-micro
    table = soup.select_one('table.a-normal.a-spacing-micro')
    table_data = {}
    if table:
        for tr in table.select('tr'):
            key = tr.select_one('td.a-span3 span.a-size-base.a-text-bold').get_text().strip()
            value = tr.select_one('td.a-span9 span.a-size-base.po-break-word').get_text().strip()
            table_data[key] = value
    ## Concat table data into string
    table_data = "|".join([f"{key} : {value}" for key, value in table_data.items()])
    images = []
    soup_images = soup.select("#imageBlock img")
    for i in soup_images:
        if 'data-a-dynamic-image' in i.attrs:
            images = eval(i['data-a-dynamic-image'])
            images = list(images.keys())
    table = soup.select_one('table.a-normal.a-spacing-micro')
    table_data = {}
    if table:
        for tr in table.select('tr'):
            key = tr.select_one('td.a-span3 span.a-size-base.a-text-bold').get_text().strip()
            value = tr.select_one('td.a-span9 span.a-size-base.po-break-word').get_text().strip()
            table_data[key] = value
    ## Concat table data into string
    table_data = "|".join([f"{key} : {value}" for key, value in table_data.items()])
    return ProductDetailDTO(name_Global=title,name_Local=title,is_available=1, price=price, rating=rating, description_Global=table_data,images=images,productlink1=url)















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
       

   