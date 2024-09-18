import json

from task_manager import Task


class Storage:


    def __init__(self):
        self._tasks =Storage.read_json('db.json')
        print(self._tasks)


    def save_task(self, task):
        self._tasks.append(task.__dict__)
        self.write_json(self._tasks)

    def update_task(self, updated_task):
        for i, task in enumerate(self._tasks):
            if task.title == updated_task.title:
                self._tasks[i] = updated_task
                break
        self.write_json(self._tasks)


    def get_task(self, title):
        for task in self._tasks:
            if task.title == title:
                return task
        return None

    def get_all_tasks(self):
        return list(self._tasks)


    def clear_all_tasks(self):
        self._tasks = []
        self.write_json()

    # methods to persist in the database
    @classmethod
    def read_json(cls,filename='db.json'):

        try:
            with open(filename, 'r') as f:
                temp = cls.json_to_tasks(f.readline())
                return temp
        except FileNotFoundError:
            create_file = open(filename, 'w')
            create_file.write('[]')
            create_file.close()
            return []

    @classmethod
    def write_json(cls,data, filename='db.json'):
        print(data,'write')
        with open(filename, 'w') as f:
            json.dump(cls.tasks_to_json(data), f, indent=4)

    def tasks_to_json(tasks):
        return json.dumps([task.to_dict() for task in tasks], indent=4)

    def json_to_tasks(json_data):
        print(json_data,'json to task')
        tasks_dict = json.loads(json_data)
        return [Task.from_dict(task_data) for task_data in tasks_dict]

