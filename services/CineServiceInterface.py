from abc import ABC


class CineServiceInterface(ABC):
    def get_sessions(self):
        pass

    def buy_ticket(self):
        pass

    def return_ticket(self):
        pass
    