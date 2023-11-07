import datetime
import traceback
from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Users

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

# Authentication
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")

# To get a string like this, run: openssl rand -hex 32
SECRET_KEY = 'f61969a11a278ee4da65432a2d5130c699debbcfe0ea87c47e0871e9e733478c'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class CreateUserRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request: CreateUserRequest, db: db_dependency):
    create_user_model = Users(
        username=create_user_request.username,
        hashed_password=bcrypt_context.hash(create_user_request.password)
    )

    db.add(create_user_model)
    db.commit()


async def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return None
    if not bcrypt_context.verify(password, user.hashed_password):
        return None
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.datetime.now() + expires_delta
    try:
        return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    except jwt.PyJWTError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Could not create access token")


@router.post("/token")
async def login_for_access_token(
        db: db_dependency,
        form_data: OAuth2PasswordRequestForm = Depends()
):
    try:
        user = await authenticate_user(form_data.username, form_data.password, db)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate the user.')

        token = create_access_token(user.username, user.id, timedelta(minutes=20))
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        print("Error:", e)  # Log the error
        print(traceback.format_exc())  # Log the full traceback
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred")


@router.post("/user")
async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
        return {'username': username, 'id': user_id}
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
