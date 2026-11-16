from dotenv import load_dotenv
from os import environ

load_dotenv()

class AppConfig:
    connection_string = str(environ.get("CONNECTION_STRING"))
