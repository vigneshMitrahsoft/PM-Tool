from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer, ForeignKey, DateTime
from datetime import datetime
from config import Base

class ProjectTechStack(Base):

    __tablename__ = 'projecttechstack'

    id = Column(Integer, primary_key = True)
    project_id = Column(Integer, ForeignKey('project.project_id'))
    techstack_id = Column(Integer, ForeignKey('techstack.id'))
    created_at = Column(DateTime, default = datetime.now())
    created_by = Column(Integer)
    updated_at = Column(DateTime, default = datetime.now(), onupdate = datetime.now())
    updated_by = Column(Integer)

 

