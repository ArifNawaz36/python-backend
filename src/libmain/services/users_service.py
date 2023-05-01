from pydantic import BaseModel
from libmain.settings import settings
from libmain.models.users_model import UserModel
from libdata.models.tables import UserTable

class User(BaseModel):
    def create(self, user: UserModel):
        try:
            session = settings.get_session()
            session.begin()
            new_user = UserTable(
                name=user.name,
                email=user.email,
                age=user.age,
                gender=user.gender,
                phone=user.phone,
                job=user.job,
                status=user.status,
            )
            session.add(new_user)

            session.commit()
            session.refresh(new_user)
            return new_user
        except Exception as error:
            session.rollback()
            raise error

    def get(self, user_id: int):
        try:
            session = settings.get_session()
            session.begin()
            user = session.query(UserTable).filter(UserTable.id == user_id).first()
            return user
        except Exception as error:
            session.rollback()
            raise error

    def get_all(self):
        try:
            session = settings.get_session()
            session.begin()
            users = session.query(UserTable).all()
            return users
        except Exception as error:
            session.rollback()
            raise error
