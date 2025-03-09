from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import conect

client = MongoClient(
    conect.MONGO_URI,
    server_api=ServerApi('1')
)

db = client.book

class CRUD:
    def __init__(self):
        """ Підключення до Atlas """
        try:
            self.connection = client
                    
        except Exception as e:
            print(" Помилка підключення до бази даних:", e)
    
    @staticmethod
    def db_create_cat(name, age, features):
        new_cat={"name":name , "age":age, "features":features}
        db.cats.insert_one(new_cat)
        print(f"Новий кіт {name} додано")
        
    @staticmethod
    def db_find():
        result = db.cats.find({}) 
        for el in result:
            print(el)
    @staticmethod
    def db_find_cat(name):
        result = db.cats.find_one({"name": name})
        if result:
            print(result)
        else:
            print(f"Кіт з імям {name} не знайдено")
    @staticmethod
    def db_update_age(name, new_age ):
        db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
        result = db.cats.find_one({"name": name})
        print(result)
    @staticmethod
    def db_update_features(name, features ):
        db.cats.update_one({"name": name}, {"$push": {"feature":features}})
        db.cats.find_one({"name": name})
        print(f"Характеристика {feature}кота {name} додано")

    @staticmethod
    def db_delete_cat(name):
        result = db.cats.delete_one({"name": name})
        if result.deleted_count:
            print(f"Кіт {name} видалений")
        else:
            print(f"Кіт {name} не знайдений")

    @staticmethod
    def db_delete_allcats():
        db.cats.delete_many({})
        print("Всі коти видалені")    
    
if __name__ == "__main__":
    crud = CRUD()
    while True:
        print("\n Виконайте команду:")
        print("1. Додати кота")
        print("2. Вивести всіх котів")
        print("3. Знайти кота за ім'ям")
        print("4. Оновити вік кота")
        print("5. Додати характеристику коту")
        print("6. Видалити кота за ім'ям")
        print("7. Видалити всіх котів")
        print("8. Вийти")
        
        choice = input("Введіть номер опції: ")
        
        if choice == "1":
            name = input("Введіть ім'я кота: ")
            age = int(input("Введіть вік кота: "))
            features = input("Введіть характеристики через кому: ").split(", ")
            crud.db_create_cat(name, age, features)
        elif choice == "2":
            crud.db_find()
        elif choice == "3":
            name = input("Введіть ім'я кота: ")
            crud.db_find_cat(name)
        elif choice == "4":
            name = input("Введіть ім'я кота: ")
            new_age = int(input("Введіть новий вік кота: "))
            crud.db_update_age(name, new_age)
        elif choice == "5":
            name = input("Введіть ім'я кота: ")
            feature = input("Введіть нову характеристику: ")
            crud.db_update_features(name, features)
        elif choice == "6":
            name = input("Введіть ім'я кота: ")
            crud.db_delete_cat(name)
        elif choice == "7":
            crud.db_delete_allcats()
        elif choice == "8":
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")