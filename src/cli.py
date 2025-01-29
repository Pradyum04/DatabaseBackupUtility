import argparse
from utils import load_config, test_connection  # Utility functions
from database.mysql_backup import backup_mysql
from database.pgsql_backup import backup_postgresql
from database.mongo_backup import backup_mongodb
from database.sqlite_backup import backup_sqlite
from database.restore import restore_database  # Restore logic

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Database Backup Utility")
    parser.add_argument(
        "--db_type",
        required=True,
        choices=["mysql", "postgresql", "mongodb", "sqlite"],
        help="Type of database (mysql, postgresql, mongodb, sqlite)"
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Run a database backup"
    )
    parser.add_argument(
        "--restore",
        metavar="FILE",
        help="Restore a database from the specified backup file"
    )

    args = parser.parse_args()

    # Load configuration
    try:
        config = load_config(args.db_type)
    except ValueError as e:
        print(e)
        return

    # Test database connection
    if not test_connection(config, args.db_type):
        print(f"❌ Failed to connect to the {args.db_type} database. Check your configuration.")
        return

    # Perform backup
    if args.backup:
        print(f"🚀 Starting backup for {args.db_type}...")
        if args.db_type == "mysql":
            backup_mysql(config)
        elif args.db_type == "postgresql":
            backup_postgresql(config)
        elif args.db_type == "mongodb":
            backup_mongodb(config)
        elif args.db_type == "sqlite":
            backup_sqlite(config)
        else:
            print(f"⚠️ Backup not implemented for {args.db_type} yet.")

    # Perform restore
    elif args.restore:
        print(f"🔄 Restoring {args.db_type} database from {args.restore}...")
        restore_database(config, args.db_type, args.restore)

    else:
        print("⚠️ No operation specified. Use --help for usage details.")

if __name__ == "__main__":
    main()
