import os

class Config:
    # Chave secreta usada para segurança (ex.: sessões, CSRF protection)
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # URI de conexão com o banco de dados SQLite local
    SQLALCHEMY_DATABASE_URI = 'sqlite:///base.db'

    # Desativa o rastreamento de modificações para economizar recursos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
