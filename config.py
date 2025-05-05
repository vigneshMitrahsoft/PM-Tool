import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base 

username = "postgres"
password = "root@123"
host = "localhost"
database = "project_database"
encode = urllib.parse.quote_plus(password)
connection_string = f"postgresql://{username}:{encode}@{host}/{database}"
engine = create_engine(connection_string)

base = declarative_base()