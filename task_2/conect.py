from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo

# Замість 'your_username' і 'your_password' вставте ваші реальні облікові дані
MONGO_URI = "mongodb+srv://hill:qazxsw23edc@cluster0.4wvmx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Підключення до MongoDB Atlas
client = MongoClient(MONGO_URI, server_api = pymongo.server_api.ServerApi(
 version="1", strict=True, deprecation_errors=True))
# Вибір бази даних (замініть 'mydatabase' на вашу реальну БД)
db = client.mydatabase

# Перевірка підключення
try:
    client.admin.command("ping")
    print("Успішне підключення до MongoDB Atlas!")
except Exception as e:
    print("Помилка підключення:", e)