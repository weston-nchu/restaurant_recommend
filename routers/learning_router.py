import random
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from library.dao import RestaurantDao

router = APIRouter(
    prefix="/learning",
    tags=["learning"]
)

template = Jinja2Templates(directory="resources/frontend")

@router.get("/", response_class=HTMLResponse, description="嗜好學習首頁")
async def index(request: Request):
    return template.TemplateResponse(request, "HabitLearning.html")

@router.get("/restaurant", description="取得3筆餐廳資料")
async def restaurant():
    result_list = []
    restaurants = RestaurantDao().get_list()
    for restr in random.sample(restaurants, 3):
        result_list.append({
            "uid": restr.uid,
            "name": restr.name,
            "desc": restr.desc,
            "images": restr.get_img_url_list()
        })

    return JSONResponse(content={
        "message": "Success",
        "content": result_list
    })