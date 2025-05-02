import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = "postgres"
password = "root@123"
host = "localhost"
database = "flaskAPI"
encode = urllib.parse.quote_plus(password)
connection_string = f"postgresql://{username}:{encode}@{host}/{database}"
engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)
session = Session()



base = declarative_base()