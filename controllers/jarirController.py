#Dependencies
from requests_html import AsyncHTMLSession
from utils import getStringBetweenTwoWords , extract_and_stringify_object
from models.Product import ProductDetailDTO
import json
import re

async def scrape_Jarir_full(url): 
     # ar-sa replace to en-sa 
    if "ar-sa" in url:
        url=url.replace("ar-sa", "en-sa")
    #Url Navigation if
    if "en-sa" not in url:
        url=url.replace("jarir.com", "jarir.com/en-sa")
    # if sa-en not included add them after the domain
    if "sa-en" not in url:
        url=url.replace("jarir.com", "jarir.com/sa-en")
    session = AsyncHTMLSession()
    response = await session.get(url)
    soup=response.content.decode()
    #printSoupToHtml(soup, "jarir.html")
    stringObj = getStringBetweenTwoWords(soup, 'original:', ',related').replace('!1', 'true').replace('!0', 'false')
    obj = json.loads(extract_and_stringify_object(stringObj))
    #load the json from the file jarir.json
    #obj = json.load(open("jarir.json"))    
    # Extracting the values from the specs string
    specs = getStringBetweenTwoWords(str(obj), 'homedelivery_enable', 'check_availability_status')
    specs_list = [spec.strip() for spec in specs.split(',') if ":" in spec]
    concatenated_specs = ', '.join(specs_list)
    # Extracting the values using regular expressions
    concatenated_specs = re.findall(r": '([^']*)'", concatenated_specs)
    concatenated_specs.insert(0, "1")  # Add the first value

    # Join the extracted values into a single string
    description = ', '.join(concatenated_specs)

    #printJsonToFile(obj, "jarir.json")
    name_Local = obj.get("name", "")
    name_global = obj.get("GTM_name", "")
    isAvailable = obj.get("check_availability_status", 0) == 1
    PriceAfterDiscount = obj.get("final_price_ex_tax", obj.get("price", None))
    rating = obj.get("starRatings", None)
    rating = round(float(rating),1)

    images = ["https://ak-asset.jarir.com/akeneo-prod/asset/"+image["image"] for image in obj.get("media_gallery", []) if image.get("type") == "image"]

    # Local Extraction..
    url=url.replace("sa-en/en-sa", "ar-sa")
    response = await session.get(url)
    soup = response.content.decode()
    stringObj = getStringBetweenTwoWords(soup, 'original:', ',related').replace('!1', 'true').replace('!0', 'false')
    obj = json.loads(extract_and_stringify_object(stringObj))
    # Extract the name and Description
    name_Local = obj.get("name", "")
    specs = getStringBetweenTwoWords(str(obj), 'homedelivery_enable', 'check_availability_status')
    specs_list = [spec.strip() for spec in specs.split(',') if ":" in spec]
    concatenated_specs = ', '.join(specs_list)
    # Extracting the values using regular expression
    concatenated_specs = re.findall(r": '([^']*)'", concatenated_specs)
    concatenated_specs.insert(0, "1")  # Add the first value
    concatenated_specs = ', '.join(concatenated_specs)
    description_Local = concatenated_specs
    item_data = ProductDetailDTO(description_Local=description_Local,name_Global=name_global,name_Local=name_Local, price=PriceAfterDiscount,images=images,productlink1=url,description_Global=description,is_available=isAvailable,rating=rating)
    return item_data



























# async def scrape_Jarir_price(url):
#     session = AsyncHTMLSession()
#     response = await session.get(url)
#     script_target_object=getStringBetweenTwoWords(response.content.decode(), 'window.__INITIAL_STATE__= ','</script>')
#     strat_index=response.content.decode().index('window.__INITIAL_STATE__')
#     end_index=response.content.decode().index('</script>',strat_index)
#     script_target_object=response.content.decode()[strat_index:end_index].replace('window.__INITIAL_STATE__=','')
#     price=getStringBetweenTwoWords(script_target_object, 'final_price_ex_tax:',',')
#     item_data = ItemPrice(price=price)
#     return item_data
# async def scrape_Jarir_images(url):
#     session = AsyncHTMLSession()
#     response = await session.get(url)
#     script_target_object=getStringBetweenTwoWords(response.content.decode(), 'window.__INITIAL_STATE__= ','</script>')
#     strat_index=response.content.decode().index('window.__INITIAL_STATE__')
#     end_index=response.content.decode().index('</script>',strat_index)
#     script_target_object=response.content.decode()[strat_index:end_index].replace('window.__INITIAL_STATE__=','')
#     images_string = getStringBetweenTwoWords(script_target_object, 'media_gallery','tsk').split("},{")
#     images=[]
#     for i in range(len(images_string)):
#         images.append("https://ak-asset.jarir.com/akeneo-prod/asset/"+getStringBetweenTwoWords(images_string[i], 'image:"','",lab'))
#     item_data = ItemImages(images=images)
#     return item_data