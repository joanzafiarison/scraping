from model.db import BaseEntityInterface

class StructSQL(BaseEntityInterface):
    def __init__(self, connexion):
        self.connexion = connexion
        pass
    
    def get(self, data):
        pass

    def get_by_id(self, id):
        pass

    def getall(self):
        pass

    def insert(self, data):
        pass

    def insertMany(self, data):
        pass

    def delete(self, id):
        pass

    def update(self, data, id):
        pass