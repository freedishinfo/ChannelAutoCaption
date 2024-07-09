import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7218167291:AAGPEvK5-G3JYaRyJdWg1dHur34J5yZUDOY")
    API_ID = int(os.environ.get("API_ID", "1310650"))
    API_HASH = os.environ.get("API_HASH", "8b85f95e0e07d0aee4fa812ce9ea46f4")
    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://freedishinfo2022:BJYtDeJ8c8QBi9tW@xyzdata.bwhb1tl.mongodb.net/?retryWrites=true&w=majority&appName=xyzdata")
