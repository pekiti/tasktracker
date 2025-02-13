# Task Reminder

A simple web-based task reminder application built with Flask that sends email notifications for due tasks.

**Code and documentation was solely generated/written by cursor :)**

## Features

- Add, complete, and delete tasks
- Email notifications for due tasks
- Clean web interface
- SQLite database storage

## Installation

1. Clone the repository:

2. Create and activate a virtual environment:

On macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

## Configuration

1. Copy the example environment file:

```bash
cp .env.example .env
```

2. Edit `.env` file with your settings:

```
SECRET_KEY=your-secret-key-here
MAIL_USERNAME=your-gmail@gmail.com
MAIL_PASSWORD=your-gmail-app-password
MAIL_DEFAULT_SENDER=your-gmail@gmail.com
```

### Setting up Gmail for notifications

1. Go to your Google Account settings
2. Enable 2-Step Verification if not already enabled
3. Generate an App Password:
   - Go to Security → App passwords
   - Select "Mail" and your device
   - Click "Generate"
   - Use the generated 16-character password as your `MAIL_PASSWORD` in `.env`

## Project Structure

```plaintext
task_reminder/
│
├── app/                    # Application package
│   ├── __init__.py        # Flask app initialization
│   ├── config.py          # Configuration settings
│   ├── database.py        # Database operations
│   ├── email_service.py   # Email notification service
│   ├── models.py          # Data models
│   ├── routes.py          # URL routes and views
│   └── static/            # Static files (CSS, JS)
│
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   └── tasks/            
│       └── index.html    # Main task view
│
├── instance/             # Instance-specific files
├── tests/               # Test files
├── .env                 # Environment variables
├── .gitignore          # Git ignore rules
├── requirements.txt     # Project dependencies
└── run.py              # Application entry point
```

## Running the Application

1. Make sure your virtual environment is activated:

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

2. Start the development server:

```bash
python run.py
```

3. Open your web browser and navigate to:

```
http://localhost:5000
```

## Using the Application

### Adding a Task

1. Fill in the "Add New Task" form:
   - Title (required)
   - Description (optional)
   - Due Date (required)
2. Click "Add Task"

### Managing Tasks

- To mark a task as complete: Click the "Complete" button
- To delete a task: Click the "Delete" button
- Tasks are automatically sorted by due date
- Completed tasks are visually distinguished

### Email Notifications

- You will receive email notifications for tasks that are due
- Notifications include task title, description, and due date
- Emails are sent from the configured Gmail account

## Development

### Database

- SQLite database is used for storage
- Database file is created at `instance/tasks.db`
- Tables are automatically created on first run

### Templates

- Templates use Jinja2 templating engine
- Base template provides common structure
- Task template extends base template

### Static Files

- CSS styles are in `app/static/css/style.css`
- JavaScript files can be added in `app/static/js/`

## Troubleshooting

### Email Issues

- Verify Gmail app password is correct
- Ensure 2-Step Verification is enabled
- Check spam folder for notifications

### Database Issues

- If database errors occur, try deleting `instance/tasks.db`
- Restart application to recreate database

### Server Issues

- Check if port 5000 is available
- Ensure virtual environment is activated
- Verify all dependencies are installed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask framework and community
- Python community
- All contributors to this project
