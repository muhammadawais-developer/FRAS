import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://fras-eeb4b-default-rtdb.asia-southeast1.firebasedatabase.app/",
                               'storageBucket': "fras-eeb4b.appspot.com"})

ref = db.reference('Students')


data = {
    "1": {
        "name": "Areeba",
        "major": "CS",
        "starting_year": random.randint(2015, 2023),
        "total_attendance": random.randint(1, 50),
        "standing": random.choice(["G", "B"]),
        "year": random.randint(1, 5),
        "last_attendance_time": "2022-12-11 00:54:34"
        # "last_attendance_time": "2022-12-11 00:54:34"
    },  "2": {
        "name": "Awais",
        "major": "SE",
        "starting_year": random.randint(2015, 2023),
        "total_attendance": random.randint(1, 50),
        "standing": random.choice(["G", "B"]),
        "year": random.randint(1, 5),
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "5": {
        "name": "Fawad",
        "major": "Chemistry",
        "starting_year": random.randint(2015, 2023),
        "total_attendance": random.randint(1, 50),
        "standing": random.choice(["G", "B"]),
        "year": random.randint(1, 5),
         "last_attendance_time": "2022-12-11 00:54:34"
    },
    "6": {
        "name": "Saeed",
        "major": "Mechanical",
        "starting_year": random.randint(2015, 2023),
        "total_attendance": random.randint(1, 50),
        "standing": random.choice(["G", "B"]),
        "year": random.randint(1, 5),
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "7": {
        "name": "Cruise",
        "major": "Astronomy",
        "starting_year": random.randint(2015, 2023),
        "total_attendance": random.randint(1, 50),
        "standing": random.choice(["G", "B"]),
        "year": random.randint(1, 5),
         "last_attendance_time": "2022-12-11 00:54:34"
    },
    "3": {
        "name": "Elon",
        "major": "Chemistry",
        "starting_year": random.randint(2015, 2023),
        "total_attendance": random.randint(1, 50),
        "standing": random.choice(["G", "B"]),
        "year": random.randint(1, 5),
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "4": {
        "name": "Emma",
        "major": "Biology",
        "starting_year": random.randint(2015, 2023),
        "total_attendance": random.randint(1, 50),
        "standing": random.choice(["G", "B"]),
        "year": random.randint(1, 5),
        "last_attendance_time": "2022-12-11 00:54:34"
    },   "8": {
        "name": "Sofiyan",
        "major": "English",
        "starting_year": random.randint(2015, 2023),
        "total_attendance": random.randint(1, 50),
        "standing": random.choice(["G", "B"]),
        "year": random.randint(1, 5),
        "last_attendance_time": "2022-12-11 00:54:34"
    },
}


for key, value in data.items():
    ref.child(key).set(value)