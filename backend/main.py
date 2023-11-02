from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserLogin(BaseModel):
    username: str
    password: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/login")
async def login(userlogin: UserLogin):
    if userlogin.username == "admin" and userlogin.password == "password":
        return {"username": "admin", "role": "admin"}
    else:
        return {"username": f"{userlogin.username}", "role": "user"}