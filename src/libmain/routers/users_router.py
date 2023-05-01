from fastapi import APIRouter
from libmain.services.users_service import User
from libmain.models.users_model import UserModel


router = APIRouter(prefix="/api/v1/users")


@router.post("/", tags=["Users"])
def create_user(user: UserModel):
    return User().create(user)

@router.get("/", tags=["Users"])
def get_users():
    return User().get_all()

@router.get("/{id}", tags=["Users"])
def get_user(id: int):
    return User().get(id)
