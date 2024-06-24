from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Note


class Database:
    """
    Класс для управления базой данных SQLite.
    """

    def __init__(self, db_url='sqlite:///notes.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        """
        Возвращает новую сессию базы данных.
        """
        return self.Session()
