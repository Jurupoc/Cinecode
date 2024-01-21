from services.UserServiceInterface import UserServiceInterface
from data_base.DataBaseInterface import DataBaseInterface


class UserOperations:
    def __init__(self, db: DataBaseInterface, user: UserServiceInterface):
        self.db = db
        self.user = user

    def normalizer_user(self):
        return self.user.__dict__

    def create_new_user(self):
        return self.normalizer_user()
