from model.db import BaseEntityInterface

class UserMongo(BaseEntityInterface):
    def __init__(self ,connexion):
        self.connexion = connexion

    def get(self, data):
        database =  self.connexion.get_database("Scraping")
        users = database.get_collection("User")
        res = users.find_one(data)
        return res

    def get_by_id(self, id):
        database =  self.connexion.get_database("Scraping")
        users = database.get_collection("User")
        users.find_one({"_id" : id})
        return "get by id mongo"

    def getall(self):
        return "get all mongo"

    def update(self, data, id):
        database =  self.connexion.get_database("Scraping")
        users = database.get_collection("User")
        rec = users.update_one({"_id" : id}, data)
        return "update mongo"

    def delete(self, id):
        database =  self.connexion.get_database("Scraping")
        users = database.get_collection("User")
        rec = users.delete({"_id" : id}, data)
        return "delete mongo"
