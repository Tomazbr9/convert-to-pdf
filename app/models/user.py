from models.base import BaseModel

from app import db

class User(BaseModel):

    __tablename__ = 'user'

    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    files = db.relationship('File', backref='user', lazy=True)
    
