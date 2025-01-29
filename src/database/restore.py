import subprocess
import shutil
import os

def restore_database(config, db_type, backup_file):
    """
    Restores a database from a backup file.

    Args:
        config (dict): Configuration dictionary containing database connection details.
        db_type (str): Type of the database (e.g., mysql, postgresql, mongodb, sqlite).
        backup_file (str): Path to the backup file to restore from.
    """
    try:
        if db_type == "mysql":
            restore_mysql(config, backup_file)
        elif db_type == "postgresql":
            restore_postgresql(config, backup_file)
        elif db_type == "mongodb":
            restore_mongodb(config, backup_file)
        elif db_type == "sqlite":
            restore_sqlite(config, backup_file)
        else:
            print(f"⚠️ Unsupported database type: {db_type}")
    except Exception as e:
        print(f"❌ Restore failed for {db_type}: {e}")

def restore_mysql(config, backup_file):
    """
    Restores a MySQL database from a backup file.

    Args:
        config (dict): Configuration dictionary for MySQL.
        backup_file (str): Path to the backup file.
    """
    try:
        cmd = [
            "mysql",
            f"--host={config['host']}",
            f"--port={config['port']}",
            f"--user={config['username']}",
            f"--password={config['password']}",
            config["database"]
        ]

        with open(backup_file, "r") as file:
            subprocess.run(cmd, stdin=file, stderr=subprocess.PIPE, check=True)

        print(f"✅ MySQL restore successful from {backup_file}")

    except subprocess.CalledProcessError as e:
        print(f"❌ MySQL restore failed. Error: {e.stderr.decode()}")

def restore_postgresql(config, backup_file):
    """
    Restores a PostgreSQL database from a backup file.

    Args:
        config (dict): Configuration dictionary for PostgreSQL.
        backup_file (str): Path to the backup file.
    """
    try:
        cmd = [
            "psql",
            f"--host={config['host']}",
            f"--port={config['port']}",
            f"--username={config['username']}",
            f"--dbname={config['database']}"
        ]

        with open(backup_file, "r") as file:
            subprocess.run(cmd, stdin=file, stderr=subprocess.PIPE, check=True)

        print(f"✅ PostgreSQL restore successful from {backup_file}")

    except subprocess.CalledProcessError as e:
        print(f"❌ PostgreSQL restore failed. Error: {e.stderr.decode()}")

def restore_mongodb(config, backup_file):
    """
    Restores a MongoDB database from a backup directory.

    Args:
        config (dict): Configuration dictionary for MongoDB.
        backup_file (str): Path to the backup directory.
    """
    try:
        cmd = [
            "mongorestore",
            f"--host={config['host']}",
            f"--port={config['port']}",
            f"--username={config['username']}",
            f"--password={config['password']}",
            f"--db={config['database']}",
            backup_file
        ]

        subprocess.run(cmd, stderr=subprocess.PIPE, check=True)
        print(f"✅ MongoDB restore successful from {backup_file}")

    except subprocess.CalledProcessError as e:
        print(f"❌ MongoDB restore failed. Error: {e.stderr.decode()}")

def restore_sqlite(config, backup_file):
    """
    Restores an SQLite database from a backup file.

    Args:
        config (dict): Configuration dictionary for SQLite.
        backup_file (str): Path to the backup file.
    """
    try:
        shutil.copy(backup_file, config["database"])
        print(f"✅ SQLite restore successful from {backup_file}")
    except Exception as e:
        print(f"❌ SQLite restore failed: {e}")
