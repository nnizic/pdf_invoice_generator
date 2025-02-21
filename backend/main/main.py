from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import create_tables
from auth import router as auth_router
from crud import router as crud_router

app = FastAPI()

# Omogućavanje CORS-a za frontend Flask aplikaciju
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Kreiranje tablica u DynamoDB
create_tables()

# Učitavanje ruta
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(crud_router, prefix="/invoice", tags=["invoice"])

