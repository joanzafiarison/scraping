from model.db import DataInterface
from model.database.mongo.entities.user import UserMongo
from pymongo import MongoClient

class MongoInstanceDb(DataInterface):
    def __init__(self, config):
        self.config = config
        
    def connect(self):
        #mongodb+srv://joanzafdev:<password>@cluster0.klzoohx.mongodb.net/?retryWrites=true&w=majority
        self.connexion  = MongoClient(f"mongodb+srv://{self.config['username']}:{self.config['password']}@cluster0.klzoohx.mongodb.net/?retryWrites=true&w=majority") 

    def getModel(self, model):
        return MongoFactory(connexion = self.connexion).getModel(model)
    
    def getTables(self):
        return self.connexion.list_database_names()
       

class MongoFactory():
    def __init__(self, connexion):
        self.MODELS = {
            "user" : UserMongo(connexion = connexion) ,
            "struct" : "STRUCT",
            "job" : "JOB",
            'category' : "CATEGORY"
        } 
        

    def getModel(self, name):
        if name in self.MODELS.keys() :
            return self.MODELS[name]
        else :
            return "No model found"
  