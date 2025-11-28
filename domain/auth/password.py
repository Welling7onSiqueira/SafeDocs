import re

class Password:

    def __init__(self, password):

        self.__validate(password)
        self._password = password

    def __validate(self, password):
        
        if not isinstance(password, str):
            raise ValueError("A senha deve ser uma string.")

        if " " in password:
            raise ValueError("A senha não pode conter espaços.")

        if len(password) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")

        if not re.search(r"[A-Z]", password):
            raise ValueError("A senha deve conter ao menos uma letra maiúscula.")

        if not re.search(r"[a-z]", password):
            raise ValueError("A senha deve conter ao menos uma letra minúscula.")

        if not re.search(r"\d", password):
            raise ValueError("A senha deve conter ao menos um número.")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\\[\]]", password):
            raise ValueError("A senha deve conter ao menos um caractere especial.")
        
    def __eq__(self, value):
        if not isinstance(value, Password):
            return NotImplemented
        return self._password == value.value

    def __str__(self):
        return self._password
    
    @property
    def value(self):
        return self._password