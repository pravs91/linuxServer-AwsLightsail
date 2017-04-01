from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base
from user import User


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250))
    description = Column(String())
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))

    @property
    def serialize(self):
        """Return department object in JSON format"""
        return {
            'name': self.name,
            'id': self.id,
            'address': self.address,
            'description': self.description,
            'user_id': self.user_id
        }
