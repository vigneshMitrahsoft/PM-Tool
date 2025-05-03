from flask import Flask
from config import base, engine
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class timesheet(base):
    __tablename__ = "timesheet"
    
    id = Column(Integer, primary_key = True)
    task = Column(String)
    title = Column(String)
    description = Column(String)
    hours = Column(DateTime, nullable = True)
    status = Column(String)
    created_at = Column(DateTime, nullable = True, default = datetime.now())
    created_by = Column(Integer, nullable = True)
    updated_at = Column(DateTime, nullable = True, default = datetime.now, onupdate = datetime.now())
    updated_by = Column(Integer, nullable = True)
 
base.metadata.create_all(engine)