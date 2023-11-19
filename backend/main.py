from datetime import datetime

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from enum import Enum

from auth.routes import authRouter
from auth.utils import get_current_active_user, get_password_hash
from auth.models import User
from db.connector import connection
import pymysql

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware to allow communication with the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authRouter)


class UserLogin(BaseModel):
    username: str
    password: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.post("/login")
# async def login(userlogin: UserLogin):

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
        with connection.cursor() as cursor:
            sql = (f"INSERT INTO users (FirstName, LastName, Email, username, password) VALUES "
                   f"('{signup.first_name}', '{signup.last_name}', '{signup.email}', '{signup.username}', '{get_password_hash(signup.password)}')")
            print(sql)
            cursor.execute(sql)
            connection.commit()
        return {"success": True}
    except pymysql.err.IntegrityError as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail="Duplicate username")


@app.get("/users/all")
def get_all_users(current_user: User = Depends(get_current_active_user)):
    with connection.cursor() as cursor:
        sql = f"SELECT * FROM users"
        cursor.execute(sql)
        users = cursor.fetchall()
        print(users)
        return users


class StatusEnum(Enum):
    PENDING = "PENDING"
    VERIFIED = "VERIFIED"
    SUCCESSFUL = "SUCCESSFUL"
    WARNING = "WARNING"


class BookingForm(BaseModel):
    roomID: int
    startTime: datetime
    endTime: datetime


@app.post("/booking")
def do_booking(form: BookingForm, current_user: User = Depends(get_current_active_user)):
    try:
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM bookings WHERE RoomID = {form.roomID}
                         AND (('{form.startTime}' < StartTime AND '{form.endTime}' > StartTime)
                          OR ('{form.startTime}' > StartTime AND '{form.endTime}' < EndTime)
                          OR ('{form.startTime}' BETWEEN StartTime AND EndTime))
                          AND status != 'CANCELED';"""
            cursor.execute(sql)
            res = cursor.fetchall()
            print(res)
            # if this returns that means there is an incompatible time
            if len(res) != 0:
                raise HTTPException(status_code=400, detail="Time Not available")

        with connection.cursor() as cursor:
            sql = (f"INSERT INTO bookings (UserID, RoomID, StartTime, EndTime) VALUES "
                   f"('{current_user.UserID}', '{form.roomID}', '{form.startTime}', '{form.endTime}')")
            cursor.execute(sql)
            connection.commit()
        return {"success": True}
    except pymysql.err.OperationalError as e:
        connection.rollback()
        print(e)
        raise HTTPException(status_code=500, detail=f"Something went wrong {e}")


class AdminEdit(BaseModel):
    bookingID: int
    status: str


@app.post("/edit/booking")
def edit_booking(booking: AdminEdit, current_user: User = Depends(get_current_active_user)):
    try:
        if current_user.role == 'admin':
            with connection.cursor() as cursor:
                sql = f"UPDATE bookings SET Status = '{booking.status}' WHERE BookingID = {booking.bookingID}"
                cursor.execute(sql)
                connection.commit()
            return {"success": True}

    except pymysql.OperationalError as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Something went Wrong {e}")


@app.delete("/booking/{booking_id}")
def delete_booking(booking_id: int, current_user: User = Depends(get_current_active_user)):
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM bookings WHERE BookingID= '{booking_id}'"
            cursor.execute(sql)
            res = cursor.fetchone()
        if current_user.role == 'admin' or int(res.get('UserID')) == current_user.UserID:
            with connection.cursor() as cursor:
                sql = f"UPDATE bookings SET Status = 'CANCELED' WHERE BookingID = {booking_id}"
                cursor.execute(sql)
                sql = f"INSERT INTO cancellations (BookingID) VALUES ({booking_id})"
                cursor.execute(sql)
                connection.commit()

    except pymysql.OperationalError as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Something Went Wrong {e}")


@app.get("/booking/history")
def get_booking_history(current_user: User = Depends(get_current_active_user)):
    if current_user.role == 'admin':
        sql = "SELECT * FROM bookings"
    else:
        sql = f"SELECT * FROM bookings WHERE UserID='{current_user.UserID}'"
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            data = cursor.fetchall()
        return data
    except pymysql.OperationalError as e:
        raise HTTPException(status_code=500, detail=f"Something Went Wrong {e}")