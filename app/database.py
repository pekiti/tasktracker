import sqlite3
import os
from flask import g, current_app

"""
Database connection and initialization.

This module handles SQLite database operations including:
- Connection management using Flask's application context
- Database initialization with schema
- Connection cleanup

Functions:
    get_db(): Get database connection
    close_db(e=None): Close database connection
    init_db(app): Initialize database with schema
"""

def get_db():
    if 'db' not in g:
        # Ensure instance directory exists
        os.makedirs(current_app.instance_path, exist_ok=True)
        
        # Connect to database
        db_path = os.path.join(current_app.instance_path, 'tasks.db')
        g.db = sqlite3.connect(
            db_path,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    with app.app_context():
        db = get_db()
        
        # Create schema
        with app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8')) 