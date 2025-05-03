from config import base,engine
from sqlalchemy import Column, Integer, String

class Employee(base):
	__tablename__='employee'
	
	emp_id = Column(Integer, primary_key=True)
	fname = Column(String(100), nullable=False)
	lname = Column(String(100))
	email = Column(String(100), unique=True)
	company_id = Column(Integer)
	project_id = Column(Integer)

	def __repr__(self):
		return self.fname

base.metadata.create_all(engine)