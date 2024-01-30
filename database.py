from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

# Construct the connection URI for the database
CONNECTION_URI = f"mysql+pymysql://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}"

# Create an engine that provides a source of connectivity to the database
engine = create_engine(CONNECTION_URI, echo=False)

# Create a configured "Session" class
# autocommit=False means the session will not commit unless explicitly told to
# autoflush=False means the session will not flush unless explicitly told to
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Dependency that will generate a new SessionLocal that will be used in each request,
# get closed when the request is finished, and then for every subsequent request a new SessionLocal will be generated
def get_db():
    session = SessionLocal()
    try:
        # yield the session to be used in the request
        yield session
    finally:
        # Close the session
        session.close()