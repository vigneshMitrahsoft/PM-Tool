from sqlalchemy.orm import relationship,declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,Date, DateTime
from datetime import datetime
from config import engine

Base = declarative_base()

class Project(Base):
	__tablename__ = 'project'

	project_id = Column(Integer, primary_key=True)
	project_name = Column(String)
	budget = Column(Integer)
	startdate = Column(Date)
	duedate = Column(Date)
	created_at = Column(DateTime, default = datetime.now())
	created_by = Column(Integer)
	updated_at = Column(DateTime, default = datetime.now(), onupdate = datetime.now())
	updated_by = Column(Integer)

Base.metadata.create_all(engine)