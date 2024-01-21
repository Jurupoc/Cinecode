from abc import ABC


class DataBaseInterface:
    def create(self, data: dict):
        pass

    def read(self, data: dict):
        pass

    def update(self, data: dict):
        pass

    def delete(self, data: dict):
        pass
