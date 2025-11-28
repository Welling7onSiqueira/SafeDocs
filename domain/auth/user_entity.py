from dataclasses import dataclass
from typing import Optional
from .email import Email
from .password import Password


@dataclass
class UserEntity:
    email: Email
    password: Password