import random
from typing import List
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from library.dao import RestaurantTagsDao

router = APIRouter(
    prefix="/search",
    tags=["search"]
)

template = Jinja2Templates(directory="resources/frontend")

@router.get("/", response_class=HTMLResponse, description="首頁")
async def index(request: Request):
    return template.TemplateResponse(request, "Restaurant.html")

@router.get("/popular-tags", description="取得熱門標籤資料")
async def popular_tags():
    tags = RestaurantTagsDao().query_all_tags()
    return JSONResponse(content={
        "message": "Success",
        "content": random.sample(tags, 10)
    })

@router.post("/restaurant", description="取得餐廳資料")
async def restaurant(tags: List[str]):
    from library import dqn
    from library.dao import RestaurantDao
    tags = [tag.replace("式", "") for tag in tags]
    code_list = dqn.get_recommendations_json(tags)
    restr_list = RestaurantDao().query_restr_by_codes(code_list)
    result_list = []
    for restr in restr_list:
        result_list.append({
            "name": restr.name,
            "code": restr.code,
            "desc": restr.desc,
            "address": restr.address,
            "url": restr.url,
            "images": restr.get_img_url_list(),
            "tags": restr.get_tag_list()
        })
    return JSONResponse(content={
        "message": "Success",
        "content": result_list
    })