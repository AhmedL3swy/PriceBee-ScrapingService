from .aliexpressController import scrape_aliexpress_full
from .amazonController import scrape_amazon_full
from .amazonSaController import scrape_amazonSa_full
from .extraController import scrape_extra_full
from .jarirController import scrape_Jarir_full
from .noonController import scrape_noon_full
from models.Product  import ProductDetailDTO
# Make api that take Array of Urls and return Array of ProductDetailDTO
async def Scrape(urls):
    result = []
    for url in urls:
        try:
            if "noon" in url:
                result.append(await scrape_noon_full(url))
            elif "aliexpress" in url:
                result.append(await scrape_aliexpress_full(url))
            elif "amazon.sa" in url:
                result.append(await scrape_amazonSa_full(url))
            elif "amazon" in url:
                result.append(await scrape_amazon_full(url))
            elif "jarir" in url:
                result.append(await scrape_Jarir_full(url))
            elif "extra" in url:
                result.append(await scrape_extra_full(url))
        except Exception as e:
            print(f"Error scraping URL: {url}. Error message: {str(e)}")
    return result
