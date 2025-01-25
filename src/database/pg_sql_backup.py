import subprocess
from datetime import datetime

def backup_postgresql(config):
    # Get the current date and time
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file=f"backups/pgsql_backup_{timestamp}.sql"

    try:
        cmd = [
            "pg_dump",
            f"--host={config['host']}",
            f"--port={config['port']}",
            f"--username={config['username']}",
            f"--dbname={config['database']}",
            f"--file={backup_file}"
        ]
        subprocess.run(" ".join(cmd), shell=True, check=True)
        print(f"PostgreSQL backup successful: {backup_file}")
    except Exception as e:
        print(f"PostgreSQL backup failed: {e}")