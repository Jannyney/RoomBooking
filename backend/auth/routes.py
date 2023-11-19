from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from .utils import authenticate_user, create_access_token
from .models import Token
from datetime import timedelta

MINIUTES = 360

authRouter = APIRouter()


@authRouter.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    """
    Takes Username and password from form data and signs a token
    :param form_data:
    :return:
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    access_token_expires = timedelta(minutes=MINIUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    print(access_token)
    return Token(access_token=access_token, token_type="bearer", role=user.role)
