from app.models.base import BaseModel

from flask_login import UserMixin

from app import db

class UserModel(BaseModel, UserMixin):
    __tablename__ = 'user'  # Define explicitamente o nome da tabela

    username = db.Column(db.String(50), unique=True, nullable=False)  # Nome de usuário único
    password = db.Column(db.String(255), nullable=False)  # Senha do usuário (deve ser armazenada de forma segura)
    files = db.relationship('FileModel', backref='user', lazy=True)  # Relacionamento: um usuário pode ter vários arquivos
