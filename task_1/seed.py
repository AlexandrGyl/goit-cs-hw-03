import psycopg2
from faker import Faker
import random


fake = Faker()


db_params = {
    "dbname": "task_1_db",
    "user": "user",
    "password": "workcentre",
    "host": "localhost", 
    "port": "5432"
}

# Функція для підключення до PostgreSQL
def connect_db():
    conn = psycopg2.connect(**db_params)
    return conn


def seed_users(cursor, num_records=100):
    for _ in range(num_records):
        fullname = fake.name()
        email = fake.unique.email()
        cursor.execute("""
            INSERT INTO users (fullname, email) 
            VALUES (%s, %s);
        """, (fullname, email)) 


def seed_status(cursor):
    statuses = ['new', 'in progress', 'completed']
    for status in statuses:
        cursor.execute("""
            INSERT INTO status (name) 
            VALUES (%s)
        """, (status,))


def seed_tasks(cursor, num_records=50):
    cursor.execute("SELECT id FROM users;")
    user_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("SELECT id FROM status;")
    status_ids = [row[0] for row in cursor.fetchall()]
    
    for _ in range(num_records):
        title = fake.sentence(nb_words=5)
        description = fake.text()
        user_id = random.choice(user_ids)
        status_id = random.choice(status_ids)
        cursor.execute("""
            INSERT INTO tasks (title, description, status_id, user_id) 
            VALUES (%s, %s, %s, %s);
        """, (title, description, status_id, user_id))


def main():
    conn = connect_db()
    cursor = conn.cursor()
    
   
    print("Заповнюємо таблицю status...")
    seed_status(cursor)
    
    print("Заповнюємо таблицю users...")
    seed_users(cursor, num_records=100)
    
    print("Заповнюємо таблицю tasks...")
    seed_tasks(cursor, num_records=200)
    
    
    conn.commit()
    
   
    cursor.close()
    conn.close()

    print("Дані успішно заповнено!")

if __name__ == "__main__":
    main()