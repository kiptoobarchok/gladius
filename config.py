import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "a93c5fa9d1fc2ad39ab8aa6a0402d747")  # Change this!
    SQLALCHEMY_DATABASE_URI = 'sqlite:///gladius.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
