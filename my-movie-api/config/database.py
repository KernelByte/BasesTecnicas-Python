import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqllite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqllite_file_name)}"

# Representacion de la base de datos
engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

# Manipulacion de las tablas en la base de datos
Base = declarative_base()