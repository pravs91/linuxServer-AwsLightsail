from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base
from user import User
from department import Department

# Use cascade property for data integrity (i.e. delete courses if dept is
# deleted) --> http://docs.sqlalchemy.org/en/latest/orm/cascades.html
# Also use relationship("Department", back_populates="courses") so Department
# has all courses -->
# http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html


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
    img_url = Column(String(400))

    @property
    def serialize(self):
        """Return course information in JSON format"""
        return {
            'name': self.name,
            'id': self.id,
            'department': self.department.name,
            'professor': self.professor,
            'credits': self.credits,
            'max_capacity': self.max_capacity,
            'description': self.description,
            'user_id': self.user_id,
            'img_url': self.img_url
        }
