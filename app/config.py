from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine=create_engine("postgresql+psycopg2://postgres:root@localhost:5432/ProjectManagement")