from os import environ
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

class Config:
    DB_HOST = environ.get('DB_HOST')
    DB_USER = environ.get('DB_USER')
    DB_PASSWORD = environ.get('DB_PASSWORD')
    DB_NAME = environ.get('DB_NAME')
    DB_PORT = environ.get('DB_PORT', '3306')

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
