from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# region import local Scrapers
from controllers.aliexpressController import scrape_aliexpress_full, scrape_aliexpress_images, scrape_aliexpress_price
from controllers.amazonController import scrape_amazon_full, scrape_amazon_images, scrape_amazon_price
from controllers.amazonSaController import scrape_amazonSa_full, scrape_amazonSa_images, scrape_amazonSa_price
from controllers.extraController import scrape_extra_full, scrape_extra_images, scrape_extra_price
from controllers.jarirController import scrape_Jarir_full, scrape_Jarir_images, scrape_Jarir_price
from controllers.noonController import  scrape_noon_full, scrape_noon_images, scrape_noon_price
# endregion

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")
#region Noon
@app.get("/details/noon/") 
async def get_noon_details(url: str):
   return await scrape_noon_full(url)
@app.get("/price/noon/")
async def get_noon_price(url: str):
    return await scrape_noon_price(url)
@app.get("/images/noon/")
async def get_noon_images(url: str):
    return await scrape_noon_images(url)
#endregion
#region aliexpress
@app.get("/details/aliexpress/")
async def get_aliexpress_details(url: str):
    return await scrape_aliexpress_full(url)
@app.get("/price/aliexpress/")
async def get_aliexpress_price(url: str):
    return await scrape_aliexpress_price(url)
@app.get("/images/aliexpress/")
async def get_aliexpress_images(url: str):
    return await scrape_aliexpress_images(url)
#endregion
#region amazon
@app.get("/details/amazon/")
async def get_amazon_details(url: str):
    return await scrape_amazon_full(url)
@app.get("/price/amazon/")
async def get_amazon_price(url: str):
    return await scrape_amazon_price(url)
@app.get("/images/amazon/")
async def get_amazon_images(url: str):
    return await scrape_amazon_images(url)
#endregion
#region amazonSa
@app.get("/details/amazonSa/")
async def get_amazonSa_details(url: str):
    return await scrape_amazonSa_full(url)
@app.get("/price/amazonSa/")
async def get_amazonSa_price(url: str):
    return await scrape_amazonSa_price(url)
@app.get("/images/amazonSa/")
async def get_amazonSa_images(url: str):
    return await scrape_amazonSa_images(url)
#region Jarir
@app.get("/details/jarir/")
async def get_jarir_details(url: str):
    return await scrape_Jarir_full(url)
@app.get("/price/jarir/")
async def get_jarir_price(url: str):
    return await scrape_Jarir_price(url)
@app.get("/images/jarir/")
async def get_jarir_images(url: str):
    return await scrape_Jarir_images(url)
#endregion
#region Extra
@app.get("/details/extra/")
async def get_extra_details(url: str):
    return await scrape_extra_full(url)
@app.get("/price/extra/")
async def get_extra_price(url: str):
    return await scrape_extra_price(url)
@app.get("/images/extra/")
async def get_extra_images(url: str):
    return await scrape_extra_images(url)

#region Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0", port=8080)
