from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base
from user import User
from department import Department


class Course(Base):
    __tablename__ = 'course'
    id = Column(String(6), primary_key=True)  # course code
    name = Column(String(250), nullable=False)
    department = relationship(Department)
    department_id = Column(Integer, ForeignKey('department.id'))
    professor = Column(String(70))
    credits = Column(Integer)
    max_capacity = Column(Integer)
    description = Column(String())
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))

    @property
    def serialize(self):
        """Return course information in JSON format"""
        return {
            'name': self.name,
            'id': self.id,
            'department_id': self.department_id,
            'professor': self.professor,
            'credits': self.credits,
            'max_capacity': self.max_capacity,
            'description': self.description,
            'user_id': self.user_id
        }
