from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app/sql_app.db"
SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='password', server='127.0.0.1', database='fastapi')
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@127.0.0.1/fastapi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()