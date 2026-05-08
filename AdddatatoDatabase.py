import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred ,{
    'databaseURL' : "https://face-recognition-attenda-13ff0-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "221702":
        {
            "name": "Adnan Pinjari",
            "branch": "CSE(AIML)",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-09-11 00:54:34"
        },


    "221723":
        {
            "name": "Salik Khan",
            "branch": "CSE(AIML)",
            "starting_year": 2022,
            "total_attendance": 9,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-09-11 00:54:34"
        },


    "325410":
        {
            "name": "Sufiyan Mirje",
            "branch": "EXTC",
            "starting_year": 2022,
            "total_attendance": 4,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-09-11 00:54:34"
        }
}
for key, value in data.items():
    ref.child(key).set(value)
