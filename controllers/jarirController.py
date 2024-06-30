#Dependencies
from requests_html import AsyncHTMLSession
from utils import getStringBetweenTwoWords , extract_and_stringify_object
from models.Product import ProductDetailDTO
import json

async def scrape_Jarir_full(url):  
    session = AsyncHTMLSession()
    response = await session.get(url)
    soup=response.content.decode()
    stringObj = getStringBetweenTwoWords(soup, 'original:', ',related').replace('!1', 'true').replace('!0', 'false')
    obj = json.loads(extract_and_stringify_object(stringObj))

    specs = getStringBetweenTwoWords(str(obj), 'homedelivery_enable', 'check_availability_status')
    specs_list = [spec.strip() for spec in specs.split(',') if ":" in spec]
    concatenated_specs = ', '.join(specs_list)

    name_global = obj.get("name", "")
    isAvailable = obj.get("check_availability_status", 0) == 1
    PriceAfterDiscount = obj.get("final_price_ex_tax", obj.get("price", None))
    rating = None  
    
    images = ["https://ak-asset.jarir.com/akeneo-prod/asset/"+image["image"] for image in obj.get("media_gallery", []) if image.get("type") == "image"]
    item_data = ProductDetailDTO(name_Global=name_global, price=PriceAfterDiscount,images=images,productlink1=url,description_Global=concatenated_specs,is_available=isAvailable,rating=rating,domainId=1)
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