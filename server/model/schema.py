from sqlalchemy.orm import Mapped, mapped_column
from .db import db

class User(db.Model):
    __tablename__ ="users"
    id : Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username : Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    email : Mapped[str] = mapped_column(db.String)
    password : Mapped[str] = mapped_column(db.String)
    role : Mapped[str] = mapped_column(db.String)