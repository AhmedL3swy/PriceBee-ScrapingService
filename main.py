from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# region import local Scrapers
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