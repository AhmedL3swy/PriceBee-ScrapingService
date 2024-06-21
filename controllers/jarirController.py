#Dependencies
from requests_html import AsyncHTMLSession
from utils import getStringBetweenTwoWords
from models.Product import ProductDetailDTO

async def scrape_Jarir_full(url):  
    session = AsyncHTMLSession()
    response = await session.get(url)
    script_target_object=getStringBetweenTwoWords(response.content.decode(), 'window.__INITIAL_STATE__= ','</script>')
    strat_index=response.content.decode().index('window.__INITIAL_STATE__')
    end_index=response.content.decode().index('</script>',strat_index)
    script_target_object=response.content.decode()[strat_index:end_index].replace('window.__INITIAL_STATE__=','')
    price=getStringBetweenTwoWords(script_target_object, 'final_price_ex_tax:',',')
    Title=getStringBetweenTwoWords(script_target_object, 'GTM_name:',',')
    images_string = getStringBetweenTwoWords(script_target_object, 'media_gallery','tsk').split("},{")
    images=[]
    for i in range(len(images_string)):
        images.append("https://ak-asset.jarir.com/akeneo-prod/asset/"+getStringBetweenTwoWords(images_string[i], 'image:"','",lab'))
    item_data = ProductDetailDTO(name_Global=Title, price=price,images=images,productlink1=url)
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