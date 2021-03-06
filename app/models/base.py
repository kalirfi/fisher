from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer
from contextlib import contextmanager
from app.libs.utils import timestamp


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:  # content
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

db = SQLAlchemy()

class Base(db.Model):
    # 避免sqlalchemy自动尝试为该基类创建对应的表
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = timestamp()

    def set_attrs(self, attrs):
        for k, v in attrs.items():
            if hasattr(self, k) and k != id:
                setattr(self, k, v)

