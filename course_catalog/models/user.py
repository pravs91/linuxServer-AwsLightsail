from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100))
    picture = Column(String(250))

    @property
    def serialize(self):
        """Return user object in JSON format"""
        return {
            'name': self.name,
            'id': self.id,
            'email': self.email,
            'picture': self.picture,
        }
