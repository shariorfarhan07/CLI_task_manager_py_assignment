from datetime import datetime

import storage


class Task:

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now().isoformat()
        self.start_time = None
        self.end_time = None

    def __str__(self):
        return (f"Task(title='{self.title}', "
                f"description='{self.description}', "
                f"completed={self.completed}, "
                f"created_at='{self.created_at}', "
                f"start_time={self.start_time}, "
                f"end_time={self.end_time})")

    def to_dict(self):
        return {
            'title' : self.title,
            'description': self.description,
            'completed' : self.completed,
            'created_at' : self.created_at,
            'start_time' : self.start_time,
            'end_time' : self.end_time
        }

    @classmethod
    def from_dict(cls, data):
        task = Task(data['title'], data['description'])
        task.completed = data['completed']
        task.created_at = datetime.strptime(data['created_at'], '%Y-%m-%dT%H:%M:%S.%f').isoformat()
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
        if include_completed:
            return tasks
        return [task for task in tasks if not task.completed]

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

    def start_task(self, title):
        tasks = self.storage.get_all_tasks()
        for task in tasks:
            if task.title == title:

                if task.start_time is None:
                    task.start_time = datetime.now().isoformat()
                    self.storage.persist()
                else:
                    print('The following task has been is running from', task.start_time)
                break
