from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class DataInterface():
    def __init__(self, config):
        self.config = config
        pass
    def connect(self):
        pass
    def getModel(self, model):
        pass

    def getTables(self):
        pass
  
class BaseEntityInterface():
    def __init__(self):
        pass

    def get(self, data):
        pass

    def get_by_id(self, id):
        pass

    def getall(self):
        pass

    def insert(self, data ):
        pass

    def insertMany(self , data ):
        pass

    def update(self, id, data):
        pass

    def delete(self, id):
        pass


    
    



    
#factory <DataFactory>




db = SQLAlchemy(model_class=Base)


