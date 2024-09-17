from datetime import datetime, timedelta

from Utils.enums import Status
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
        saved = self.storage.save_task(task)
        if saved:
            return task
        return None

    def start_task(self,title):
        task = self.storage.start_task(title)

    def complete_task(self, title):
        task = self.storage.get_task(title)
        if task ==None:
            return False
        if task.start_time == None:
            return Status.NOT_STARTED
        if task:
            task.completed = True
            task.end_time = datetime.utcnow()
            self.storage.commit_updated_task(task)
            return Status.COMPLETE
        return Status.NOT_FOUND

    def list_tasks(self, include_completed=False):
        tasks = self.storage.get_all_tasks()
        if not include_completed:
            return [task for task in tasks if not task.completed]
        return tasks

    '''
         This method improves efficiency compared to the previous implementation.
         Instead of retrieving all tasks and then filtering out completed ones,
         it directly queries for incomplete tasks. This reduces the amount of data
         fetched from the database, saving time and bandwidth.
         By using self.storage.get_all_incomplete_tasks(), we avoid the overhead of
         loading unnecessary data and filtering it in-memory.

    '''
    def list_tasks_efficient_version(self, include_completed=False):
        if not include_completed:
            return self.storage.get_all_tasks()
        return self.storage.get_all_incomplete_task()

    def generate_report(self):
        tasks = self.storage.get_all_tasks()
        total_tasks = len(tasks)
        completed_tasks = len([task for task in tasks if task.completed])
        total_completed_task_time = [(task.end_time-task.start_time).total_seconds() for task in tasks
                                     if task.completed and (task.end_time != None or task.start_time !=None )]
        # if not total_completed_task_time:
        #     total_completed_task_time= []

        average_duration_seconds = sum(total_completed_task_time)/completed_tasks
        # Convert average duration back to timedelta
        average_duration = timedelta(seconds=average_duration_seconds)
        days = average_duration.days
        seconds = average_duration.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60
        formatted_time_delta=""
        if hours >0:
            formatted_time_delta +=f" {days}d"
        if minutes> 0:
            formatted_time_delta += f" {minutes}m"
        if remaining_seconds>0:
            formatted_time_delta += f" {remaining_seconds}s"
        report = {
            "total": total_tasks,
            "completed": completed_tasks,
            "pending": total_tasks - completed_tasks,
            "average_time":  formatted_time_delta
        }

        return report
