from config import base,engine
from sqlalchemy import Column, Integer, String

class Role(base):
	__tablename__='role'
	
	role_id = Column(Integer, primary_key=True)
	name = Column(String(100), nullable=False)
	description=Column(String(100))

	def __repr__(self):
		return self.name

base.metadata.create_all(engine)