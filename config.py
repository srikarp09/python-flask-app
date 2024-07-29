import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Ensure to include the full scheme, user, password, host, port, and database name
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    ENV = 'Development'
