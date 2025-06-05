from typing import List
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from library import dqn
from library.dao import RestaurantDao

router = APIRouter(
    prefix="/learning",
    tags=["learning"]
)

template = Jinja2Templates(directory="resources/frontend")

@router.get("/", response_class=HTMLResponse, description="嗜好學習首頁")
async def index(request: Request):
    return template.TemplateResponse(request, "HabitLearning.html")

@router.get("/restaurant", description="取得5筆餐廳資料")
async def restaurant():
    restr_codes_batch = dqn.start()
    dao = RestaurantDao()
    result_list = []
    for restr_codes in restr_codes_batch:
        restr_list = []
        for code in list(restr_codes.values()):
            restr = dao.get_one(code=code)
            restr_list.append({
                "uid": restr.uid,
                "name": restr.name,
                "desc": restr.desc,
                "images": restr.get_img_url_list()
            })
        result_list.append(restr_list)

    return JSONResponse(content={
        "message": "Success",
        "content": result_list
    })

@router.post("/train", description="接收用戶選擇餐廳並開始學習")
async def train(restr_list: List[str]):
    code_list = RestaurantDao().query_code_by_uid_list(restr_list)
    dqn.train(code_list)
    return JSONResponse(content={
        "message": "Success",
        "content": ""
    })