import json

from task_manager import Task


class Storage:

    def __init__(self):
        self._tasks = Storage.read_json('db.json')

    def save_task(self, task):
        for item in self._tasks:
            if task.title == item.title:
                return None
        self._tasks.append(task)
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
        return self._tasks

    def clear_all_tasks(self):
        self._tasks = []
        self.write_json()

    # methods to persist in the database
    @classmethod
    def read_json(cls, filename='db.json', json=None):

        try:
            with open(filename, 'r') as f:
                json_str = f.readline()
                temp = cls.json_to_task_list(json_str)
                return temp
        except FileNotFoundError:
            create_file = open(filename, 'w')
            create_file.write('[]')
            create_file.close()
            return []

    def write_json(cls, data, filename='db.json'):
        with open(filename, 'w') as f:
            temp = cls.instance_array_to_dic_array(data)
            json.dump(temp, f)

    def instance_array_to_dic_array(self,tasks):
        temp = [task.to_dict() for task in tasks]
        return temp

    @classmethod
    def json_to_task_list(cls, json_data):
        if len(json_data) == 0:
            return []
        tasks_dict = json.loads(json_data)
        return [Task.from_dict(task_data) for task_data in tasks_dict]

    def persist(self):
        self.write_json(self._tasks)
