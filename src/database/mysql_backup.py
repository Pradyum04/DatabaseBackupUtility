import subprocess
from datetime import datetime
import os

def backup_mysql(config):
    """
    Performs a backup of a MySQL database using mysqldump.
    
    Args:
        config (dict): Configuration dictionary containing database connection details.
    """
    # Generate a timestamp for the backup file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)  # Ensure the backups directory exists
    backup_file = os.path.join(backup_dir, f"mysql_backup_{timestamp}.sql")

    try:
        # Construct the mysqldump command
        cmd = [
            "mysqldump",
            f"--host={config['host']}",
            f"--port={config['port']}",
            f"--user={config['username']}",
            f"--password={config['password']}",
            config["database"]
        ]

        # Redirect output to the backup file
        with open(backup_file, "w") as file:
            subprocess.run(cmd, stdout=file, stderr=subprocess.PIPE, check=True)

        print(f"✅ MySQL backup successful: {backup_file}")

    except subprocess.CalledProcessError as e:
        print(f"❌ MySQL backup failed. Error: {e.stderr.decode()}")

    except Exception as e:
        print(f"⚠️ Unexpected error during MySQL backup: {e}")
