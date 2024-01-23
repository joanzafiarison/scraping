from model.db import db , DataInterface 
from model.database.sql.db import SqlDb 
from model.database.sql.entities.user import UserSQL
from model.database.mongo.db import  MongoInstanceDb
from flask import Flask
from model.schema import User , Struct , ResultJob, Job, Category

import os
from dotenv import load_dotenv

load_dotenv()

import pytest

mongoConfig = { 
        "username" :os.getenv('MONGO_USER'),
        "password" :os.getenv("MONGO_PASS")
}

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config["TESTING"] : True

    db.init_app(app)
    # other setup can go here
    with app.app_context():
        db.create_all()
    return app

app = create_app()

@pytest.fixture
def app_ctx(app):
    with app.app_context():
        yield

    # clean up / reset resources here
@pytest.mark.usefixtures("app_ctx")
def test_get_users():
    users =  db.session.execute(db.select(User)).scalars().all()
    assert users == []

@pytest.mark.usefixtures("app_ctx")
def test_get_categories():
    categories = db.session.execute(db.select(Category)).scalars().all()
    assert categories == []


def test_SqlDB_to_implement_DataInterface():
    assert issubclass(SqlDb, DataInterface) == True

def test_SQlDB_access_to_User():
    config = {}
    db = SqlDb(config=config)
    db.connect()
    userInstance = db.getModel("user")
    assert type(userInstance) == UserSQL()

def test_SQlDB_access_to_User():
    config = {
        "host":"localhost",
        "user" : "root",
        "password" :"hello" 
    }
    db = SqlDb(config=config)
    db.connect()
    userInstance = db.getModel("user")
    userResponse = userInstance.get()
    assert userResponse == "get user sql"

def test_MongoDB_access_to_User():
    data = {
        "email" : "joanzafdev@gmail.com"
    }
    expected = "joanzafdev@gmail.com"
       
    config = mongoConfig
    db = MongoInstanceDb(config=config)
    db.connect()
    userInstance = db.getModel("user")
    userResponse = userInstance.get(data)
    assert userResponse["email"] == expected

def test_MongoDB_get_table_list():
    config = mongoConfig
    db = MongoInstanceDb(config=config)
    db.connect()
    tables = db.getTables()
    assert tables == ["Scraping", "admin", "local"]

def test_MongoDB_get_collection_list():
    config = mongoConfig
    db = MongoInstanceDb(config=config)
    db.connect()
    database =  db.connexion.get_database("Scraping")
    tables = database.list_collection_names()
    assert "User" in tables





