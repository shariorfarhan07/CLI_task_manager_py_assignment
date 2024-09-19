from datetime import datetime, timedelta

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
        if data['start_time']:
            task.start_time = datetime.strptime(data['start_time'], '%Y-%m-%dT%H:%M:%S.%f').isoformat()
        else:
            task.start_time =None
        if data['end_time']:
            task.end_time = datetime.strptime(data['end_time'], '%Y-%m-%dT%H:%M:%S.%f').isoformat()
        else:
            task.end_time = None
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
            if task.end_time is not None:
                print("The task was already completed at {}".format(task.end_time))
                return
            if task.start_time is not None:
                task.completed = True
                task.end_time = datetime.now().isoformat()
                self.storage.update_task(task)
                print("Task has been completed")
            else:
                print("Please start the task first")


    def list_tasks(self, include_completed=False):
        tasks = self.storage.get_all_tasks()
        if include_completed:
            return tasks
        return [task for task in tasks if not task.completed]

    def generate_report(self):
        tasks = self.storage.get_all_tasks()
        total_tasks_count = len(tasks)
        completed_tasks = [task for task in tasks if task.completed]
        completed_tasks_time =[self.time_for_completing_task(task) for task in completed_tasks]
        completed_tasks_time_sum =timedelta()
        for task_time in completed_tasks_time:
            completed_tasks_time_sum +=task_time
        completed_tasks_count = len(completed_tasks)
        average_time = 0
        if completed_tasks != 0:
            average_time = completed_tasks_time_sum / completed_tasks_count

        report = {
            "total": total_tasks_count,
            "completed": completed_tasks_count,
            "pending": total_tasks_count - completed_tasks_count,
             "average_time": self.delta_to_str(average_time)
        }

        return report

    def time_for_completing_task(self,task):
        return datetime.fromisoformat(task.end_time) - datetime.fromisoformat(task.start_time)

    def start_task(self, title):
        tasks = self.storage.get_all_tasks()
        for task in tasks:
            if task.title == title:
                if task.start_time is None:
                    task.start_time = datetime.now().isoformat()
                    self.storage.persist()
                    print("task has been started")
                else:
                    print('The following task has been is running from', task.start_time)
                break
    def delta_to_str(self,delta):
        parts = []
        if delta.days > 0:
            parts.append(f"{delta.days} days")
        if delta.seconds // 3600 > 0:
            parts.append(f"{delta.seconds // 3600} hours")
        if (delta.seconds % 3600) // 60 > 0:
            parts.append(f"{(delta.seconds % 3600) // 60} minutes")
        if delta.seconds % 60 > 0:
            parts.append(f"{delta.seconds % 60} seconds")
        formatted_string = ", ".join(parts)

        return formatted_string