import random
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from library.dao import RestaurantTagsDao

router = APIRouter(
    prefix="/index",
    tags=["index"]
)

template = Jinja2Templates(directory="resources/frontend")

@router.get("/", response_class=HTMLResponse, description="首頁")
async def index(request: Request):
    return template.TemplateResponse(request, "index.html")

@router.get("/popular-tags", description="取得熱門標籤資料")
async def popular_tags():
    tags = RestaurantTagsDao().query_all_tags()
    return JSONResponse(content={
        "message": "Success",
        "content": random.sample(tags, 10)
    })