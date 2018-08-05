from sqlalchemy.orm import relationship

from app.models.base import Base
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey

from app.spider.yushu_book import YuShuBook


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    isbn = Column(String(15), nullable=False, unique=True)
    launched = Column(Boolean, default=False)


    def is_yourself_gift(self, uid):
        if self.uid == uid:
            return True

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book


