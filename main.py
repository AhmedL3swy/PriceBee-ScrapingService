from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from controllers.scrapingController import Scrape
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()
# allow cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# Define request model
class URLList(BaseModel):
    urls: List[str]


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")
@app.post("/scrape/")
async def get_details(urls: URLList):
    return await Scrape(urls.urls)
@app.get("/SingleScrape/")
async def get_details(url: str):
    result= await Scrape([url])
    return result[0]
#region Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0", port=8080)
