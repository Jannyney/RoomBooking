from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends

from db.connector import connection
from .models import User, Token, TokenData
from datetime import timedelta, datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 360


def get_user_from_db(username: str):
    with connection.cursor() as cursor:
        sql = f"SELECT * FROM users WHERE username='{username}'"
        cursor.execute(sql)
        user = cursor.fetchone()
    with connection.cursor() as cursor:
        sql = f"SELECT * FROM admins WHERE adminUser = '{user.get('UserID')}';"
        cursor.execute(sql)
        is_admin = cursor.fetchone()
        if is_admin:
            print(user.get('UserID'))
            return User(UserID=user.get('UserID'), username=user.get('username'), password=user.get('password'),
                        role='admin', can_edit=is_admin.get("can_edit"), can_delete=is_admin.get("can_delete"),
                        ) if user else None
        else:
            print(user.get('UserID'))
            return User(UserID=user.get('UserID'), username=user.get('username'), password=user.get('password'),
                        role='user', Email=user.get("Email"), FirstName=user.get("FirstName"), LastName=user.get("LastName")
                        ) if user else None

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Takes in the plain password and verifies that its is the same as the password stored in the system
    :param plain_password:
    :param hashed_password:
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Get the hash of the password
    :param password:
    :return:
    """
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str) -> User | None:
    """
    Takes in a username and password and returns a User Class
    :param username:
    :param password:
    :return:
    """
    user = get_user_from_db(username)

    if not user:
        return None # todo handle not found user
    if verify_password(password, user.password):
        if user.role == 'admin':
            print(user.UserID)
            return User(UserID=user.UserID, username=user.username, password=user.password,
                        role='admin', can_edit=user.can_edit, can_delete=user.can_delete,
                        )
        else:
            return User(UserID=user.UserID, username=user.username, password=user.password,
                        role='user', Email=user.Email, FirstName=user.FirstName, LastName=user.LastName
                        ) if user else None
    else:
        return None


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Generates a JWT for the user
    :param data:
    :param expires_delta:
    :return:
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_user(username: str) -> User | None:
    """
    Gets username and returns the User Class
    :param username:
    :return: User class
    """
    user = get_user_from_db(username)

    if not user:
        return None #todo handle user not exist
    if user.role == 'admin':
        print(user.UserID)
        return User(UserID=user.UserID, username=user.username, password=user.password,
                    role='admin', can_edit=user.can_edit, can_delete=user.can_delete,
                    )
    else:
        return User(UserID=user.UserID, username=user.username, password=user.password,
                    role='admin', Email=user.Email, FirstName=user.FirstName, LastName=user.LastName
                    ) if user else None


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None:
            return None # todo handle user not exist
        token_data = TokenData(username=username, role=role)
    except JWTError:
        return None
    user = get_user(username=token_data.username)
    if user is None:
        return None # todo handle user not exist
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user
