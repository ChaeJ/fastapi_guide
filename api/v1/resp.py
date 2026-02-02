from fastapi.responses import (
    HTMLResponse,
    PlainTextResponse,
    RedirectResponse,
    JSONResponse,
    StreamingResponse,
    FileResponse
)
from fastapi import APIRouter, FastAPI, Response, status


router = APIRouter()
    
@router.get("/htmlRes/")
async def html_res():
    html = "<html><body><h2>Welcome to out API</h2></body></html>"
    return HTMLResponse(content=html, status_code=status.HTTP_200_OK)


@router.get("/htmlRes_class/", response_class=HTMLResponse)
async def read_items2():
    return "<html><body><h2>Welcome to out API</h2></body></html>"



@router.get("/planText/")
async def planText():    
    return PlainTextResponse(content="Server Status:OK", status_code=status.HTTP_200_OK)



@router.get("/planText_class/", response_class=PlainTextResponse)
async def planText():
    return "Server Status:OK"



@router.get("/redirect/")
async def redirect():    
    return RedirectResponse(url="/new-feature-url", status_code=status.HTTP_301_MOVED_PERMANENTLY)


@router.get("/redirect_class/", response_class=RedirectResponse)
async def redirect():
    return "/new-feature-url"



@router.get("/json/")
async def json():    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"id":123},
        headers={"X-Custom-Header": "WWWWW"}
    )
    

#해더 지정
@router.get("/customHeader/")
async def setheader(response: Response):
    response.headers["X-My-Custom-Header"] = "this is my custom header"
    return {"message" : "header set"}


#쿠키 지정
@router.post("/setCookie/")
async def setheader(response: Response):
    response.set_cookie(
        key="user_session_id",       # 쿠키 이름
        value="asdasdasd",           # 쿠키 값
        max_age=60 * 60 * 24 * 7,    # 쿠키 제한 시간 (7일)
        path="/",                    # 쿠키 유효 경로
        domain=".modelic.xyz",       # 쿠키 유효 도메인 (서브도메인 포함)
        secure=True,                 # https일 때만 전송
        httponly=True,               # JS 접근 불가
        samesite="lax"               # 동일 사이트만 처리
    )
    return {"message": "cookie set"}