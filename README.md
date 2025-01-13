# Database Backup Utility

## Overview
The Database Backup Utility is a command-line tool designed for backing up and restoring databases on a local machine. The tool supports various database management systems (DBMS) such as MySQL, PostgreSQL, MongoDB, and SQLite. It provides features like automated backup scheduling, compression, and robust logging for monitoring activities.

## Features
- Full, incremental, and differential backups
- Support for multiple databases:
  - MySQL
  - PostgreSQL
  - MongoDB
  - SQLite
- Compressed backups for efficient storage
- Scheduling for automatic backups
- Detailed logging of backup and restore operations

## Setting up the virtual environment
1. Create virtual environment:
    ```bash
    python -m venv venv

2. Activate the virtual environment:
On windows: 
    venv\Scripts\activate

On macOS/Linux
    source venv/bin/activate

3. Install dependencies
    pip install -r requirements.txt

4. How to check the installed dependencies and its version
    pip list

5. Deactivate the environment when done
    deactivate



## Project Structure
