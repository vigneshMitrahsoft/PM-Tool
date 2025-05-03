from config import base,engine
from sqlalchemy import Column, Integer, DATETIME

class Employee_role(base):
	__tablename__='employee_role'
	
	emp_id = Column(Integer, primary_key=True)
	role_id = Column(Integer)
	Created_at = Column(DATETIME)
	update_at = Column(DATETIME)

base.metadata.create_all(engine)