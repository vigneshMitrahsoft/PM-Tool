from models.techstackmodels import TechStack, TechstackArea
from models.projectmodels import Project
from models.projecttechstackmodels import ProjectTechStack
from config import engine, Base

Base.metadata.create_all(engine)