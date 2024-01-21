from abc import ABC


class UserServiceInterface(ABC):
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get_tickets(self):
        pass
