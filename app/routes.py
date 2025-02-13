from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Task

"""
URL routes and view functions.

Implements all application routes using Flask Blueprint:
- Main page (task list)
- Add new task
- Complete task
- Delete task

Routes:
    /: Display all tasks
    /add_task: Create new task (POST)
    /complete_task/<task_id>: Mark task as complete
    /delete_task/<task_id>: Delete task
""" 
main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Task.get_all_tasks()
    return render_template('tasks/index.html', tasks=tasks)

@main.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    due_date = request.form['due_date']
    
    if title and due_date:
        Task.create_task(title, description, due_date)
        flash('Task added successfully!', 'success')
    else:
        flash('Title and due date are required!', 'error')
    
    return redirect(url_for('main.index'))

@main.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    Task.mark_completed(task_id)
    flash('Task marked as completed!', 'success')
    return redirect(url_for('main.index'))

@main.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    Task.delete_task(task_id)
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('main.index'))
