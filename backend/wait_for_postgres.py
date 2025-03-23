import time
import psycopg2
from psycopg2 import OperationalError

def wait_for_db():
    print("Waiting for PostgreSQL database...")
    while True:
        try:
            connection = psycopg2.connect(
                dbname='postgres',
                user='postgres',
                password='New password',
                host='postgres',
                port='5432'
            )
            cursor = connection.cursor()
            cursor.execute('SELECT 1')
            cursor.close()
            connection.close()
            print("Database is ready! ✅")
            return
        except OperationalError as e:
            print(f"Database unavailable, waiting... ({e})")
            time.sleep(2)


if __name__ == "__main__":
    wait_for_db()