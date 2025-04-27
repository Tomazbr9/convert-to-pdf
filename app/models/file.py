from app.models.base import BaseModel
from app import db

class FileModel(BaseModel):
    __tablename__ = 'file'  # Define o nome da tabela explicitamente

    filename = db.Column(db.String(255), nullable=False)  # Nome do arquivo
    filepath = db.Column(db.String(500), nullable=False)  # Caminho onde o arquivo está salvo
    filesize = db.Column(db.Integer, nullable=False)      # Tamanho do arquivo
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Relaciona o arquivo a um usuário
