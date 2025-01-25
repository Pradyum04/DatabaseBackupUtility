import shutil
from datetime import datetime

def backup_sqlite(config):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"backups/sqlite_backup_{timestamp}.db"

    try:
        shutil.copy(config["database"], backup_file)
        print(f"SQLite backup successful: {backup_file}")
    except Exception as e:
        print(f"SQLite backup failed: {e}")
