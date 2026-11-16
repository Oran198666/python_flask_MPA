from utils.app_config import AppConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Dal:

    # Session object works with the database:
    @staticmethod
    def create_session():

        # Create engine object which handles the connection:
        engine = create_engine(AppConfig.connection_string)

        # Create a session factory object (function for creating session objects):
        session_factory = sessionmaker(bind = engine)

        # Create the session object:
        session = session_factory()

        # Return the session object:
        return session
