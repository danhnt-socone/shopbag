import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'devkey'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://mongo:27017/luxurybags'
