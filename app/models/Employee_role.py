from config import base,engine
from sqlalchemy import Column, Integer, DateTime

class employeeRole(base):
	__tablename__='employee_role'
	
	emp_id = Column(Integer, primary_key=True)
	role_id = Column(Integer)
	Created_at = Column(DateTime)
	update_at = Column(DateTime)

base.metadata.create_all(engine)