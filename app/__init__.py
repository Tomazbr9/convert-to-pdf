from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Carrega configurações do objeto Config
    db.init_app(app)  # Inicializa a extensão SQLAlchemy com o app Flask

    with app.app_context():
        from app.models import UserModel, FileModel  # Importa os modelos dentro do contexto da aplicação
        db.create_all()  # Cria as tabelas no banco de dados se ainda não existirem
   
    # Registrando os routes no app
    from app.auth import auth_bp
    from app.home import home_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    
    return app 
