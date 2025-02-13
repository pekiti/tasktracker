from flask_mail import Message, Mail
from flask import current_app

"""
Email notification service.

Handles email notifications for tasks using Flask-Mail.
Configures and sends emails through Gmail SMTP.

Functions:
    send_reminder_email(tasks): Send email notifications for due tasks
    create_email_body(tasks): Create email message body from task list
""" 

mail = Mail()

def send_reminder_email(tasks):
    with current_app.app_context():
        msg = Message(
            'Task Reminder',
            recipients=[current_app.config['MAIL_DEFAULT_SENDER']]
        )
        
        msg.body = create_email_body(tasks)
        mail.send(msg)

def create_email_body(tasks):
    email_body = "The following tasks are due:\n\n"
    for task in tasks:
        email_body += f"Title: {task.title}\n"
        email_body += f"Description: {task.description}\n"
        email_body += f"Due Date: {task.due_date}\n"
        email_body += "-" * 30 + "\n"
    return email_body
