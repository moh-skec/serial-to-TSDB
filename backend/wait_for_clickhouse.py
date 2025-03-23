import time
from clickhouse_driver import Client


def wait_for_db():
    print("Waiting for ClickHouse...")
    while True:
        try:
            client = Client(
                host='clickhouse',
                port=9000,  
                user='default',
                password='YnRjprs~PI2Gh',
                database='analytics_db'
            )
            version = client.execute('SELECT version()')
            print(f"✅ ClickHouse is ready! Version: {version[0][0]}")
            return
        except Exception as e:
            print(f"❌ ClickHouse unavailable, retrying in 5s... ({e})")
            time.sleep(5)


if __name__ == "__main__":
    wait_for_db()
