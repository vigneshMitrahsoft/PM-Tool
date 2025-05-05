from flask import Flask
from config import base, engine
from sqlalchemy import Column, Integer, String, DateTime, Date
from datetime import datetime

class milestone(base):
	__tablename__ = "milestone"
	
	milestone_id = Column(Integer, primary_key = True)
	project_name = Column(String)
	planned_startdate = Column(Date)
	planned_enddate = Column(Date)
	actual_startdate = Column(Date)
	actual_enddate = Column(Date)
	status = Column(String)
	description = Column(String)
	created_at = Column(DateTime, nullable = True, default = datetime.now())
	created_by = Column(Integer, nullable = True)
	updated_at = Column(DateTime, nullable = True, default = datetime.now(), onupdate = datetime.now())
	updated_by = Column(Integer)
 
base.metadata.create_all(engine)