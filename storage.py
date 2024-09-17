from datetime import datetime

from sqlalchemy import create_engine

from models.task import Base, Task
from sqlalchemy.orm import sessionmaker


class Storage:
    DATABASE_URL = "sqlite:///tasks.db"

    def __init__(self):
        self.engine = create_engine(self.DATABASE_URL, echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def save_task(self, new_task):
        existing_task = self.session.query(Task).filter(Task.title == new_task.title).first()
        if existing_task is None:
            self.session.add(new_task)
            self.session.commit()
            return new_task
        return None

        # self.session.close()

    def commit_updated_task(self, updated_task):
        self.session.commit()

    def get_task(self, title):
        return self.session.query(Task).filter(Task.title == str(title)).first()

    def start_task(self, title):
        task = self.session.query(Task).filter(Task.title == str(title)).first()
        task.start_time = datetime.utcnow()
        self.session.commit()

    def get_all_tasks(self):
        return self.session.query(Task).all()

    def get_all_incomplete_task(self):
        return self.session.query(Task).filter(Task.end_time == None).all()

    # Unused method
    def clear_all_tasks(self):
        self.tasks = []
