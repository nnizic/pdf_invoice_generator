from fastapi import APIRouter, Depends, HTTPException, Form
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from database import dynamodb
from models import UserCreate

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@router.post("/register")
async def register(user: UserCreate):
    table = dynamodb.Table("Users")
    hashed_password = get_password_hash(user.password)
    table.put_item(Item={"username": user.username, "hashed_password": hashed_password})
    return {"message": "User registered"}

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    table = dynamodb.Table("Users")
    response = table.get_item(Key={"username": username})
    user = response.get("Item")
    if not user or not pwd_context.verify(password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = jwt.encode(
        {"sub": username, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    return {"access_token": access_token, "token_type": "bearer"}

