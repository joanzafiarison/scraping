from sqlalchemy.orm import Mapped, mapped_column
from .db import db
import datetime

class User(db.Model):
    __tablename__ ="users"
    id : Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username : Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    email : Mapped[str] = mapped_column(db.String)
    password : Mapped[str] = mapped_column(db.String)
    role : Mapped[str] = mapped_column(db.String)

#Structures
class Struct(db.Model):
    __tablename__ ="structs"
    id : Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name : Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    filepath : Mapped[str] = mapped_column(db.String, unique=True)
    category : Mapped[int] = mapped_column(db.Integer)

class Category(db.Model):
    __tablename__ = "category"
    id : Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name : Mapped[str] = mapped_column(db.String)
    #filepath : Mapped[str] = mapped_column(db.String)


#JOB

class Job(db.Model):
    __tablename__ ="jobs"
    id : Mapped[int] = mapped_column(db.Integer, primary_key=True)
    #due_date : Mapped[datetime.datetime] = mapped_column(db.Datetime(timezone=True), server_default=func.now())
    filepath : Mapped[str] = mapped_column(db.String, unique=True)

class ResultJob(db.Model):
    __tablename__ ="result_jobs"
    id : Mapped[int] = mapped_column(db.Integer, primary_key = True)
    job_id : Mapped[int] = mapped_column(db.Integer)
    filepath : Mapped[str] = mapped_column(db.String)



''' => Modalisation de models avec Mongo
    'job_id': {
        'type': 'string',
        'minlength': 1,
        'required': True,
        'coerce': str.capitalize
    },
    'filepath': {
        'type': 'string',
        'minlength': 1,
        'required': True,
        'coerce': str.capitalize
    }
'''