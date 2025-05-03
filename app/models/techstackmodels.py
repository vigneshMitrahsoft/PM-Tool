from sqlalchemy.orm import relationship
from config import Base
from sqlalchemy import Column,Integer,String,ForeignKey, DateTime
from datetime import datetime

class TechstackArea(Base):
	__tablename__ = 'techstackarea'
	id = Column(Integer, primary_key = True)
	tech_stack_area_name = Column(String)
	techstack = relationship('TechStack', back_populates = 'tech', cascade="all,delete")

	def __str__(self):
		return f"{self.tech_stack_area_name}"
		
class TechStack(Base):
	__tablename__ = 'techstack'

	id = Column(Integer, primary_key = True)
	tech_name = Column(String)
	tech_area_id = Column(Integer, ForeignKey('techstackarea.id'))
	created_at = Column(DateTime, default = datetime.now())
	created_by = Column(Integer)
	updated_at = Column(DateTime, default = datetime.now(), onupdate = datetime.now())
	updated_by = Column(Integer)
	tech = relationship('TechstackArea', back_populates = 'techstack')

