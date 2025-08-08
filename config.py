import os
DB_CONFIG = {
    "host": "localhost",
    "user": "root",          # MySQL username
    "password": "aakash",  # MySQL password
    "database": "court_data" # Database name
}

SQLALCHEMY_DATABASE_URI = (
    f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
)

COURT_URL = "https://delhihighcourt.nic.in/app/get-case-type-status"


DEBUG = True           
SECRET_KEY = "secret!" 
