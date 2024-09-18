from datetime import datetime


class Task:

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now().isoformat()
    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }

    @classmethod
    def from_dict(data):
        task = Task(data['title'], data['description'])
        task.completed = data.get('completed', False)
        task.created_at = data.get('created_at', datetime.now().isoformat())
        return task

    def __str__(self):
        return (f"Task(title={self.title!r}, description={self.description!r}, "
                f"completed={self.completed}, created_at={self.created_at})")


class TaskManager:

    def __init__(self, storage):
        self.storage = storage

    def add_task(self, title, description):
        task = Task(title, description)
        self.storage.save_task(task)
        return task

    def complete_task(self, title):
        task = self.storage.get_task(title)
        if task:
            task.completed = True
            self.storage.update_task(task)
            return True
        return False

    def list_tasks(self, include_completed=False):
        tasks = self.storage.get_all_tasks()
        return tasks

    def generate_report(self):
        tasks = self.storage.get_all_tasks()
        total_tasks = len(tasks)
        completed_tasks = len([task for task in tasks if task.completed])

        report = {
            "total": total_tasks,
            "completed": completed_tasks,
            "pending": total_tasks - completed_tasks
        }

        return report
