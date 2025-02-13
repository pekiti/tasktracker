"""
Flask application factory and initialization.

This module initializes the Flask application using the factory pattern.
It configures:
- Template directory location
- Database initialization
- Email service setup
- Security headers
- Blueprint registration

Functions:
    create_app(config_class): Creates and configures Flask application instance
"""
from flask import Flask
from app.config import Config
from app.database import init_db, close_db
from app.email_service import mail
import os

def create_app(config_class=Config):
    app = Flask(__name__, 
                template_folder=os.path.abspath('templates'))
    app.config.from_object(config_class)
    
    # Initialize extensions
    mail.init_app(app)
    
    # Initialize database
    init_db(app)
    app.teardown_appcontext(close_db)
    
    # Configure security headers
    @app.after_request
    def add_security_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app

# Create the app instance
app = create_app() 