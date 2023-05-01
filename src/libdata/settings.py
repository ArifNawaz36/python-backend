from pydantic import BaseSettings, Field
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DatabaseSettings(BaseSettings):
    database_url: str = Field(
        env="DATABASE_URL",
        default="postgresql://postgresUser:postgresPW@localhost:5432/postgresDB",
    )

    def get_engine(self):
        try:
            return create_engine(self.database_url)
        except AssertionError as error:
            print(error)
        return None

    def get_session(self):
        engine = self.get_engine()
        if engine is None:
            return None
        return scoped_session(sessionmaker(autoflush=False, bind=engine))

db_setting = DatabaseSettings()
