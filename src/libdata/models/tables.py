import sqlalchemy as sa
from sqlalchemy import BIGINT, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, func
from libmain.settings import settings

Base = declarative_base()


def create_all():
    Base.metadata.create_all(bind=settings.get_engine())


def drop_all():
    Base.metadata.drop_all()


def recreate_all():
    drop_all()
    create_all()


class BaseModel(Base):
    __abstract__ = True

    created_at = sa.Column(types.TIMESTAMP, server_default="NOW")
    updated_at = sa.Column(
        types.TIMESTAMP, server_default="NOW", onupdate=func.current_timestamp()
    )


class UserTable(BaseModel):
    __tablename__ = "users"

    id = sa.Column(BIGINT, primary_key=True, autoincrement=True)
    name = sa.Column(String, nullable=False)
    email = sa.Column(String, nullable=False)
    gender = sa.Column(String, nullable=True)
    phone = sa.Column(String, nullable=True)
    age = sa.Column(sa.Integer, nullable=True)
    address = sa.Column(String, nullable=True)
    job = sa.Column(String, nullable=True)
    status = sa.Column(sa.Boolean, default=True)
