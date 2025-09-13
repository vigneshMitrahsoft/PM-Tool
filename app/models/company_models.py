from flask import Flask
from config import base, engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean

class company(base):
	__tablename__  = "company"
		
	company_id = Column(Integer, primary_key = True)
	company_name = Column(String)
	address = Column(String)
	phone_no = Column(String)
	email_id = Column(String, unique=True)
	is_active = Column(Boolean)
	created_on = Column(DateTime, nullable = True)
	updated_on = Column(DateTime, nullable = True)
	created_by = Column(Integer, nullable = True)
	updated_by = Column(Integer, nullable = True)

	def __str__(self):
		return self.company_name

base.metadata.create_all(engine)