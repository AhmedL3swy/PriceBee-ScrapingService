#Dependencies
from bs4 import BeautifulSoup
import requests
import json
from models.Product import ItemData, ItemImages, ItemPrice ,ProductDetailDTO

async def scrape_extra_full(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <script> tag containing ACC.config.productDetails
    script_tag = soup.find('script', {'type': 'text/javascript'})

    if script_tag:
        # Extract the JavaScript content from the <script> tag
        script_content = script_tag.string
        
        # Locate and extract the ACC.config.productDetails object
        start_index = script_content.find('ACC.config.productDetails')
        stop_index = script_content.find('ACC.config.currentCity')

        
        if start_index != -1 and stop_index != -1:
            product_details = script_content[start_index:stop_index]
            product_details = product_details.replace('ACC.config.productDetails = ', '').strip()
            product_details = product_details[:-1]
            product_details = json.loads(product_details)
            #printSoupToJson(product_details)
            print(product_details)
            title = product_details.get('name', 'N/A')
            total_price = product_details.get('price', {}).get('formattedValue', 'N/A')
            discount = product_details.get('percentageDiscount', {}).get('value', 'N/A')
            PriceAfterDiscount = float(total_price) - (float(total_price) * discount / 100)
            description = product_details.get('description', 'N/A')
            rating = product_details.get('averageRating', 'N/A')
            image= product_details.get('highlights')
            soup = BeautifulSoup(image, 'html.parser')
            image = soup.find_all('img')
            images= [ img['src'] for img in image]
        item_data = ProductDetailDTO(name_Global=title, price=PriceAfterDiscount, rating=rating, description_Global=description,images=images)
        return item_data
async def scrape_extra_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <script> tag containing ACC.config.productDetails
    script_tag = soup.find('script', {'type': 'text/javascript'})

    if script_tag:
        # Extract the JavaScript content from the <script> tag
        script_content = script_tag.string
        
        # Locate and extract the ACC.config.productDetails object
        start_index = script_content.find('ACC.config.productDetails')
        stop_index = script_content.find('ACC.config.currentCity')

        
        if start_index != -1 and stop_index != -1:
            product_details = script_content[start_index:stop_index]
            product_details = product_details.replace('ACC.config.productDetails = ', '').strip()
            product_details = product_details[:-1]
            product_details = json.loads(product_details)
            total_price = product_details.get('price', {}).get('formattedValue', 'N/A')
            discount = product_details.get('percentageDiscount', {}).get('value', 'N/A')
            PriceAfterDiscount = float(total_price) - (float(total_price) * discount / 100)
        item_data = ItemPrice(price=PriceAfterDiscount)
        return item_data
    
async def scrape_extra_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <script> tag containing ACC.config.productDetails
    script_tag = soup.find('script', {'type': 'text/javascript'})

    if script_tag:
        # Extract the JavaScript content from the <script> tag
        script_content = script_tag.string
        
        # Locate and extract the ACC.config.productDetails object
        start_index = script_content.find('ACC.config.productDetails')
        stop_index = script_content.find('ACC.config.currentCity')

        
        if start_index != -1 and stop_index != -1:
            product_details = script_content[start_index:stop_index]
            product_details = product_details.replace('ACC.config.productDetails = ', '').strip()
            product_details = product_details[:-1]
            product_details = json.loads(product_details)
            image= product_details.get('highlights')
            soup = BeautifulSoup(image, 'html.parser')
            image = soup.find_all('img')
            images= [ img['src'] for img in image]
        item_data = ItemImages(images=images)
        return item_data
