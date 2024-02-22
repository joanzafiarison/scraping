from model.db import BaseEntityInterface

class StructMongo(BaseEntityInterface):
    def __init__(self ,connexion):
        self.connexion = connexion

    def get(self, data):
        database =  self.connexion.get_database("Scraping")
        structs = database.get_collection("Structs")
        res = structs.find_one(data)
        return res

    def get_by_id(self, id):
        database =  self.connexion.get_database("Scraping")
        structs = database.get_collection("Structs")
        structs.find_one({"_id" : id})
        return "get by id mongo"

    def getall(self):
        return "get all mongo"

    def update(self, data, id):
        database =  self.connexion.get_database("Scraping")
        structs = database.get_collection("Users")
        rec = structs.update_one({"_id" : id}, data)
        return "update mongo"

    def delete(self, id):
        database =  self.connexion.get_database("Scraping")
        structs = database.get_collection("Structs")
        rec = structs.delete({"_id" : id})
        return "delete mongo"