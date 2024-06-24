from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Note(Base):
    """
    Модель для заметки.
    """
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)

    def __repr__(self):
        return f"<Note (id={self.id}, title={self.title})>"
