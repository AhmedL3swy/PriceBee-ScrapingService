from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
from models.Product import ProductDetailDTO

async def scrape_noon_full(url: str) -> dict:
    if "saudi-en" in url:
        url = url.replace("saudi-en", "saudi-ar")

    g_name = url.split('/')[4]
    asession = AsyncHTMLSession(mock_browser=True)
    response = await asession.get(url=url, headers=headers, timeout=20)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Use null coalescing to set default values if elements are not found
    title = soup.find('h1').get_text().strip() if soup.find('h1') else ""
    price = float(soup.find('div', class_='priceNow').get_text().split('.')[0].strip()) if soup.find('div', class_='priceNow') else 0.0
    rating = float(soup.find('div', class_='sc-e7071e85-2').get_text().strip()) if soup.find('div', class_='sc-e7071e85-2') else 0.0
    description = soup.find('div', class_='sc-97eb4126-2').get_text().strip() if soup.find('div', class_='sc-97eb4126-2') else ""
    d_local = soup.find('div', class_='sc-966c8510-2').get_text().strip() if soup.find('div', class_='sc-966c8510-2') else ""

    image_soup = soup.find_all('img')
    img = [i['src'] for i in image_soup if "&width" in i['src']]

    item_data = ProductDetailDTO(
        domainId=5,
        name_Global=g_name,
        name_Local=title,
        price=price,
        rating=rating,
        description_Global=description,
        images=img,
        productlink1=url,
        description_Local=d_local
    )
    return item_data












headers = {
    'authority': 'www.noon.com',
    'method': 'GET',
    'path': '/saudi-ar/iphone-15-pro-max-256gb-natural-titanium-5g-with-facetime-middle-east-version/N53432547A/p/?o=b693a3ec8486f04bn.com/es',
    'scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'visitor_id=b09fb844-4111-4d5e-9732-0ad68c5952da; _gcl_au=1.1.1242871984.1719750234; _ga=GA1.2.1126567816.1719750236; _scid=552fac0e-02a8-445c-922c-60b066dc53f9; _tt_enable_cookie=1; _ttp=H2P_6eEiDhjjVIBMepGQWVV_SUf; _ScCbts=%5B%5D; _sctr=1%7C1719694800000; nloc=ar-sa; x-whoami-headers=eyJ4LWxhdCI6IjI0NzMxMTM4MiIsIngtbG5nIjoiNDY2NzAwODE0IiwieC1hYnkiOiJ7XCJwZHBfYm9zLmVuYWJsZWRcIjoxLFwib3RwX2xvZ2luLmVuYWJsZWRcIjoxLFwicGRwX2ZseW91dC5mbHlvdXRfdmFsdWVcIjowfSIsIngtZWNvbS16b25lY29kZSI6IlNBLVJVSC1TMTciLCJ4LWFiLXRlc3QiOls3MzEsODMwLDg1MV0sIngtcm9ja2V0LXpvbmVjb2RlIjoiVzAwMDgzNDk2QSIsIngtcm9ja2V0LWVuYWJsZWQiOnRydWUsIngtYm9yZGVyLWVuYWJsZWQiOnRydWV9; AKA_A2=A; _etc=riXwINHqMvQ9lt3T; bm_mi=6F6686D85E388F01FE98E2CC3A66FC0E~YAAQtjwSAowXUn2QAQAAR0DQgRjfjzEB8MwLRdj1T7l7bEadSljcp4rKDIu+gnUCiGbJX+2eoSp2YnAei+VSXjixh5ckzU/J1HWUIsW8Bn/3YFaKh3rFELx9H/CRBjIn3unY1I6Lk20YMpH6h9hzT0JJN6hAG8bbQhStkESclQ2cK5e+zbNL9mba+a9TfabGBEPr0x5VuIJaJgDpoDTgbqLOsfke2SDxzmQbLPzRat8wuljsXezLrWZOrOLVMBnODkVmZ3/8oR0O7SWwYjZq01vQ3TiYln4OpkUb0urVTo7zRXHRnnR78xvrXiOHgTYwE4OIt7NEupy7YYvvIQRr3lnL+leb7Teu~1; nguestv2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiI2NGNiNjRjNzZiZjM0YjQzYTZkMzc1MTdlZjllOWRiMyIsImlhdCI6MTcyMDE2NDgyNywiZXhwIjoxNzIwMTY1MTI3fQ.wQKCiNSagNeQ9j4PPU244hR2Bl8OExwbyHul1NNDzd0; ak_bmsc=C6915AA994AB33139E3E1AE0D0EAEAAB~000000000000000000000000000000~YAAQtjwSAqAXUn2QAQAAUkPQgRhvQf6T507zHf1aG9p2M+x8A4j/OIay9fA1aSmEff7DwmTXWxLYNKZMbjNuV/8kMDZRWGhxzcJTfdaehGcCBHoS2gwP28piEhffjotAymMkEhi5HcbpChA6UxWDPVBfmcDg0CIbatlqLfa4lLGDr0VIC3QjukJeExbbGonNgB1xujtMmrs2IkkSbNWR7wvlUyvVPlQx//dwMwDEAKGoWFrpIg2Ge/t504+OKuIThqlKfxEVtkR/Sawm2vQxxFc2mxpJGLdgv5l/Wgy2uxRCdR59lMwIbJF+keB2nloB3dcgs4ZpnYh4zxaywxlsQczVsBP00JH3U3LRuCrjC+ly7Amq2I5rXSVoGciQfICSqH6jftcR4Z+VtRdnsTXtVvONnFnm/LgZMsv+TJt8+oZ2QeXk08Y/y/i9pTW/9lkbUNR+zTn4OHlBwHo6LrAyjrzjDoXR0zXY2D2nL/0n8gYBiRCIAGAQ6g1fjBg+; _gid=GA1.2.2073415255.1720164830; _gat_UA-84507530-14=1; _uetsid=ec332cb03aa011efaf824f7c4b2c47c1; _uetvid=9e8695c036db11ef85245b580ea796db; _scid_r=552fac0e-02a8-445c-922c-60b066dc53f9; _clck=1tjuy3l%7C2%7Cfn7%7C0%7C1642; _clsk=tjc6bk%7C1720164834897%7C1%7C0%7Cu.clarity.ms%2Fcollect; RT="z=1&dm=noon.com&si=pp82uykpu6&ss=ly8dpuw3&sl=1&tt=e02&ld=e06&ul=ory"',
    'Priority': 'u=0, i',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}





















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