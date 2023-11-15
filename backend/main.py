from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import mysql.connector

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware to allow communication with the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MySQL database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Roomie",
)
cursor = db.cursor()

class User(BaseModel):
    FirstName: str
    LastName: str
    Email: str
    Username: str
    Password: str

@app.post("/signup")
def signup(user: User):
    try:
        # Insert user data into the MySQL database
        query = "INSERT INTO users (FirstName, LastName, Email, UserName, Password) VALUES (%s, %s, %s, %s, %s)"
        values = (user.FirstName, user.LastName, user.Email, user.Username, user.Password)
        cursor.execute(query, values)
        db.commit()
        return {"message": "User signed up successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


# Pydantic model for the login request
class UserLogin(BaseModel):
    Username: str
    Password: str

@app.post("/login")
def login(user: UserLogin):
    try:
        # Check if the user exists in the MySQL database
        query = "SELECT * FROM users WHERE Username = %s AND Password = %s"
        values = (user.Username, user.Password)
        cursor.execute(query, values)
        result = cursor.fetchall()
        if len(result) == 0:
            return HTTPException(status_code=401, detail="Invalid credentials")
        else:
            return {"message": "User logged in successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@app.get("/showuser")
def users():
    try:
        # Get all users from the MySQL database
        query = "SELECT * FROM users"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

# Pydantic model for the reservation request
class booking(BaseModel):
    day: int
    month: str
    year: int
    start_time: str
    end_time: str

@app.post("/reservation")
def reservation(reservation: Reservation):
    try:
        # Insert reservation data into the MySQL database
        query = "INSERT INTO reservations (day, month, year, start_time, end_time) VALUES (%s, %s, %s, %s, %s)"
        values = (reservation.day, reservation.month, reservation.year, reservation.start_time, reservation.end_time)
        cursor.execute(query, values)
        db.commit()
        return {"message": "Reservation created successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
    
@app.get("/showreservation")
def reservations():
    try:
        # Get all reservations from the MySQL database
        query = "SELECT * FROM reservations"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

# Pydantic model for the room request
class Room(BaseModel):
    name: str
    capacity: int
    area: int
    projector: bool
    tv: bool
    whiteboard: bool
    video_conference: bool
    description: str


@app.post("/room")
def room(room: Room):
    try:
        # Insert room data into the MySQL database
        query = "INSERT INTO rooms (name, capacity, area , projector, tv, whiteboard, video_conference, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (room.name, room.capacity, room.area, room.projector, room.tv, room.whiteboard, room.video_conference, room.description)
        cursor.execute(query, values)
        db.commit()
        return {"message": "New Room created successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
    
@app.get("/showroom")
def rooms():
    try:
        # Get all rooms from the MySQL database
        query = "SELECT * FROM rooms"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Hello World"}
