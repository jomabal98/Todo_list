from models.tasks import Task
from database.config import SessionLocal

def create_task(title, description):
    if not title:
        return 
    session = SessionLocal()
    new_task = Task(title=title, description=description)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    session.close()
    return new_task

def get_all_tasks():
    session = SessionLocal()
    tasks = session.query(Task).all()
    session.close()
    return tasks

def get_task_by_id(task_id):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    session.close()
    return task

def update_task(task_id, title=None, description=None, completed=None):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        if title:
            task.title = title
        if description:
            task.description = description
        if completed is not None:
            task.completed = completed
        session.commit()
        session.refresh(task)
    session.close()
    return task

def delete_task(task_id):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
    session.close()
    return task
