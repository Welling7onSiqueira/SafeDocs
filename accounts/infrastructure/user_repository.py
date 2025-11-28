from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User as UserModel
from domain.auth.email import Email
from domain.auth.interfaces import IUserRepository
from domain.auth.user_entity import UserEntity


class DjangoUserRepository(IUserRepository):
    
    def create(self, entity: UserEntity):
        obj = UserModel.objects.create_user(
            username=entity.email.value,
            email=entity.email.value,
            password=entity.password.value,
        )
        return obj

    def get_by_email(self, email: Email):
        try:
            return UserModel.objects.get(email=email.value)
        except UserModel.DoesNotExist:
            return None
        
    def get_by_id(self, user_id: int):
        try:
            return UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return None
        
    def list(self):
        return UserModel.objects.all()
    
    def update(self, entity: UserEntity):
        user = UserModel.objects.get(id=entity.id)
        user.email = entity.email.value
        user.password = entity.password.value
        user.save()
        return user
    
    def delete(self, user_id: int):
        user = UserModel.objects.get(id=user_id)
        user.delete()        