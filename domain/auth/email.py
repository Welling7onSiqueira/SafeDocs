class Email:

    def __init__(self, email_address):

        self.__validate(email_address)
        self._email_address = email_address

    def __validate(self, email):
        
        if not isinstance(email, str):
            raise ValueError("O e-mail deve ser uma string.")

        if " " in email:
            raise ValueError("O e-mail não pode conter espaços.")

        if email.count("@") != 1:
            raise ValueError("E-mail inválido: deve conter um único '@'.")

        local, domain = email.split("@")

        if not local:
            raise ValueError("E-mail inválido: parte local vazia antes do '@'.")

        if not domain:
            raise ValueError("E-mail inválido: domínio vazio depois do '@'.")

        if "." not in domain:
            raise ValueError("Domínio inválido: deve conter pelo menos um '.'.")

        if domain.startswith(".") or domain.endswith("."):
            raise ValueError("Domínio inválido: não pode começar ou terminar com '.'.")
        
    def __eq__(self, value):
        if not isinstance(value, Email):
            return NotImplemented
        return self._email_address == value.value

    def __str__(self):
        return self._email_address
    
    @property
    def value(self):
        return self._email_address