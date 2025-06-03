from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/login",
    tags=["login"]
)

template = Jinja2Templates(directory="templates")

@router.get("/index", response_class=HTMLResponse, description="登入畫面")
async def index(request: Request):
    return template.TemplateResponse(request, "login.html")

@router.post("/", description="登入")
async def login(account: str):
    return JSONResponse(content={
        "message": "Success",
        "content": True
    })