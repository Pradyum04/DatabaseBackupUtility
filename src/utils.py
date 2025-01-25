import json
import mysql.connector
import psycopg2
import pymongo

def load_config(db_type):
    with open("config/config.json", "r") as f:
        config = json.load(f)
    if db_type in config:
        return config[db_type]
    raise ValueError(f"Unsupported database type: {db_type}")

def test_connection(config, db_type):
    try:
        if db_type == "mysql":
            connection = mysql.connector.connect(
                host=config["host"],
                port=config["port"],
                user=config["username"],
                password=config["password"],
                database=config["database"]
            )
            return connection.is_connected()
        elif db_type == "postgresql":
            connection = psycopg2.connect(
                host=config["host"],
                port=config["port"],
                user=config["username"],
                password=config["password"],
                database=config["database"]
            )
            return True
        elif db_type == "mongodb":
            client = pymongo.MongoClient(
                host=config["host"],
                port=config["port"],
                username=config["username"],
                password=config["password"]
            )
            client.server_info()  # Test the connection
            return True
        elif db_type == "sqlite":
            # SQLite uses file-based connection
            import sqlite3
            connection = sqlite3.connect(config["database"])
            connection.close()
            return True
        else:
            print(f"Unsupported database type: {db_type}")
            return False
    except Exception as e:
        print(f"Connection failed: {e}")
        return False
