from datetime import datetime
from models.task import Task


class TaskDto:

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
        self.time_to_complete = 0
        self.created_at = datetime.now().isoformat()


class TaskManager:

    def __init__(self, storage):
        self.storage = storage

    def add_task(self, title, description):
        task = Task(title=title, description=description)
        print(task,"task manager")
        return self.storage.save_task(task)



    def complete_task(self, title):
        task = self.storage.get_task(title)
        if task:
            task.completed = True
            self.storage.update_task(task)
            return True
        return False

    def list_tasks(self, include_completed=False):
        if include_completed:
            return self.storage.get_all_tasks()

        incomplete_task=[]
        tasks = self.storage.get_all_tasks()
        for task in tasks:
            if not task.completed:
                incomplete_task.append(task)

        return incomplete_task

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
