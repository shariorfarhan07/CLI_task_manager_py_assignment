from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    start_time = Column(DateTime, default=datetime.utcnow, nullable=True)
    end_time = Column(DateTime, default=datetime.utcnow, nullable=True)
    def __repr__(self):
       return f"<Task(id={self.id}, title={self.title}, completed={self.completed}, created_at={self.created_at})>"
