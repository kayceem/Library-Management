from pydantic import BaseSettings

# Create a pydantic BaseSettings class to store the environment variables
class Settings(BaseSettings):
    db_hostname:str
    db_password:str
    db_username:str
    db_name:str
    db_port:str
    secret_key:str
    algorithm:str
    
    class Config:
        env_file = ".env"
        
# Create an instance of Settings class
settings=Settings()