#Dependencies
from bs4 import BeautifulSoup
import requests
import json
from models.Product import ProductDetailDTO


async def scrape_extra_full(url):
    #change request from en-sa to ar-sa
    if url.find("/en-sa/")!=-1:
        url=url.replace("/en-sa/","/ar-sa/")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    #printSoupToHtml(soup.prettify(),'extra.html')

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
            #printJsonToFile(product_details,'extra.json')
            #product_details = json.loads(open('extra.json').read())
            name_global = product_details.get('nameEn', 'N/A')
            name_local = product_details.get('displayName', 'N/A')
            isAvailable = product_details.get('stock', {}).get('stockLevel', 'N/A')>0
            total_price = product_details.get('price', {}).get('formattedValue', 'N/A')
            discount = product_details.get('percentageDiscount', {}).get('value', 'N/A')
            PriceAfterDiscount = float(total_price) - (float(total_price) * discount / 100)
            description = product_details.get('descriptionEn', 'N/A')
            description_local = product_details.get('summary', 'N/A')
            rating = product_details.get('rating', 'N/A')
            rating = round(float(rating),1)
            p=url.split("/p/")[1].split("/")[0]
            images = [f"https://media.extra.com/i/aurora/{p}_100_0{i}" for i in range(1,6)]
            result = []
            for classification in product_details.get("classifications", []):
                for feature in classification.get("features", []):
                    name = feature.get("name")
                    value = feature.get("featureValues", [{}])[0].get("value")
                    if name and value:
                        result.append(f"{name}:{value}")
            #convert list to string
            result = ','.join(result)
            item_data = ProductDetailDTO(name_Global=name_global,name_Local=name_local,is_available=isAvailable,description_Local=result, price=PriceAfterDiscount, rating=rating, description_Global=description,images=images,productlink1=url,domainId=2)
            return item_data
    


















# async def scrape_extra_price(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find the <script> tag containing ACC.config.productDetails
#     script_tag = soup.find('script', {'type': 'text/javascript'})

#     if script_tag:
#         # Extract the JavaScript content from the <script> tag
#         script_content = script_tag.string
        
#         # Locate and extract the ACC.config.productDetails object
#         start_index = script_content.find('ACC.config.productDetails')
#         stop_index = script_content.find('ACC.config.currentCity')

        
#         if start_index != -1 and stop_index != -1:
#             product_details = script_content[start_index:stop_index]
#             product_details = product_details.replace('ACC.config.productDetails = ', '').strip()
#             product_details = product_details[:-1]
#             product_details = json.loads(product_details)
#             total_price = product_details.get('price', {}).get('formattedValue', 'N/A')
#             discount = product_details.get('percentageDiscount', {}).get('value', 'N/A')
#             PriceAfterDiscount = float(total_price) - (float(total_price) * discount / 100)
#         item_data = ItemPrice(price=PriceAfterDiscount)
#         return item_data
    
# async def scrape_extra_images(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find the <script> tag containing ACC.config.productDetails
#     script_tag = soup.find('script', {'type': 'text/javascript'})

#     if script_tag:
#         # Extract the JavaScript content from the <script> tag
#         script_content = script_tag.string
        
#         # Locate and extract the ACC.config.productDetails object
#         start_index = script_content.find('ACC.config.productDetails')
#         stop_index = script_content.find('ACC.config.currentCity')

        
#         if start_index != -1 and stop_index != -1:
#             product_details = script_content[start_index:stop_index]
#             product_details = product_details.replace('ACC.config.productDetails = ', '').strip()
#             product_details = product_details[:-1]
#             product_details = json.loads(product_details)
#             image= product_details.get('highlights')
#             soup = BeautifulSoup(image, 'html.parser')
#             image = soup.find_all('img')
#             images= [ img['src'] for img in image]
#         item_data = ItemImages(images=images)
#         return item_data
