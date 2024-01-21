from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from management.UserOperations import UserOperations
from services.UserServiceInterface import UserServiceInterface
from data_base.DataBaseInterface import DataBaseInterface

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def welcome(request: Request):
    return templates.TemplateResponse(name="welcome.html", request=request)
