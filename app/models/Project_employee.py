from config import base,engine
from sqlalchemy import Column, Integer, DATETIME, DATE

class Project_employee(base):
	__tablename__='Project_employee'
	
	emp_id = Column(Integer)
	project_id = Column(Integer)
	Created_at = Column(DATETIME)
	update_at = Column(DATETIME)
	Start_date= Column(DATE)
	End_date= Column(DATE)
	
base.metadata.create_all(engine)