from model.db import BaseEntityInterface
#from model.database.sql.db import SqlDb

class UserSQL(BaseEntityInterface):
    def __init__(self, connexion):
        self.connexion = connexion

    def get(self, data):
        return "get user sql"

    def get_by_id(self, id):
        return "get user by id sql"

    def getall(self):
        return "get all users sql"

    def update(self, data, id):
        return "update user sql"

    def delete(self, id):
        return "delete sql"