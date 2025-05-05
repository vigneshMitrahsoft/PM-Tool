from config import base,engine
from sqlalchemy import Column, Integer, DateTime, DATE

class projectEmployee(base):
	__tablename__='projectEmployee'
	
	emp_id = Column(Integer, primary_key=True)
	project_id = Column(Integer)
	Created_at = Column(DateTime)
	update_at = Column(DateTime)
	Start_date= Column(DATE)
	End_date= Column(DATE)
	
base.metadata.create_all(engine)