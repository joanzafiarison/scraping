from model.db import DataInterface
from model.database.sql.entities.user import UserSQL
import mysql.connector

class SqlDb(DataInterface):
    def __init__(self, config):
        self.config = config
        
    def connect(self):
        self.connexion  = mysql.connector.connect(
            host = self.config["host"],#"localhost",
            user= self.config["user"], #"yourusername",
            password= self.config["password"] #"yourpassword"
        ) 
    
    def getModel(self, model):
        return SqlFactory(connexion = self.connexion).getModel(model)
    
    def getTables(self):
        return super().getTables()

class SqlFactory():
    def __init__(self, connexion):
        self.connexion = connexion
        self.MODELS = {
            "user" : UserSQL(connexion = self.connexion) ,
            "struct" : "STRUCT",
            "job" : "JOB",
            'category' : "CATEGORY"
        } 
        

    def getModel(self, name):
        if name in self.MODELS.keys() :
            return self.MODELS[name]
        else :
            return "No model found"