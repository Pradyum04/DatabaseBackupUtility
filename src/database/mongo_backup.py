import subprocess
from datetime import datetime

def backup_mongodb(config):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = f"backups/mongo_backup_{timestamp}"

    try:
        cmd = [
            "mongodump",
            f"--host={config['host']}",
            f"--port={config['port']}",
            f"--username={config['username']}",
            f"--password={config['password']}",
            f"--db={config['database']}",
            f"--out={backup_dir}"
        ]
        subprocess.run(" ".join(cmd), shell=True, check=True)
        print(f"MongoDB backup successfull: {backup_dir}")
    except Exception as e:
        print(f"MongoDB backup fialed: {e}")