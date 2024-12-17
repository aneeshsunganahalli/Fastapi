from fastapi import FastAPI, status, HTTPException, Depends, Response
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from pydantic import BaseModel
from . import models,schemas,utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post,user,auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Karatekid2005', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(10)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


