from flask import Flask

from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy

from app.config.config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Carrega configurações do objeto Config
    db.init_app(app)  # Inicializa a extensão SQLAlchemy com o app Flask

    with app.app_context():
        from app.models import UserModel, FileModel  # Importa os modelos dentro do contexto da aplicação
        db.create_all()  # Cria as tabelas no banco de dados se ainda não existirem
    
    # Configura o gerenciamento de login no Flask
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' # type:ignore

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import UserModel
        return UserModel.query.get(int(user_id))
   
    # Registrando os routes no app
    from app.auth import auth_bp
    from app.home import home_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    
    return app 
