from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    
    uvicorn.run(
        "app:app",
        host    = "0.0.0.0",
        port    = 8036, 
        reload  = True
    )