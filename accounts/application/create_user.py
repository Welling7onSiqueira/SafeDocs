from domain.auth.email import Email
from domain.auth.password import Password
from domain.auth.interfaces import IUserRepository
from domain.auth.user_entity import UserEntity
from domain.utils.comparator import Comparator

class CreateUser:

    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def execute(self, email: str, password: str, confirm_password: str):
        email_obj = Email(email)
        password_obj = Password(password)
        confirm_password_obj = Password(confirm_password)

        if not Comparator.compare(password_obj, confirm_password_obj):
            raise "Senhas Diferentes"

        user_entity = UserEntity(
            email=email_obj,
            password=password_obj
        )

        created_user = self.repository.create(user_entity)
        return created_user