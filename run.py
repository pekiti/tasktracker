"""
Application entry point.

Imports and runs the Flask application.
Configures development server settings:
- Debug mode enabled
- Host set to localhost
- Port 5000
"""
from app import app

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000) 