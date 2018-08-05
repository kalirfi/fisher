from sqlalchemy.orm import relationship

from app.models.base import Base
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False, unique=True)
    launched = Column(Boolean, default=False)

