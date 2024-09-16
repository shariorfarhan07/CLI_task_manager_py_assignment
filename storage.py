from sqlalchemy import create_engine

from models.task import Base,Task
from sqlalchemy.orm import sessionmaker
class Storage:

    DATABASE_URL = "sqlite:///tasks.db"

    def __init__(self):
        self.engine = create_engine(self.DATABASE_URL, echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def save_task(self, new_task):
        existing_task=self.session.query(Task).filter(Task.title == new_task.title).first()
        if existing_task is None:
            self.session.add(new_task)
            self.session.commit()
            return new_task
        return None




        # self.session.close()


    def update_task(self, updated_task):
        for i, task in enumerate(self.tasks):
            if task.title == updated_task.title:
                self.tasks[i] = updated_task
                break

    def get_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def get_all_tasks(self):
        return list(self.tasks)

    def clear_all_tasks(self):
        self.tasks = []
