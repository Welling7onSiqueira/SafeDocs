from abc import ABC, abstractmethod
from typing import Optional, List
from .user_entity import UserEntity
from .email import Email


class IUserRepository(ABC):

    @abstractmethod
    def create(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def get_by_email(self, email: Email) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def list(self) -> List[UserEntity]:
        pass

    @abstractmethod
    def update(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass