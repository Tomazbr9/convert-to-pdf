from app import create_app

from app.auth.routes import auth_bp
from app.home.routes import home_bp

app = create_app()

app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)

if __name__ == '__main__':
    app.run(debug=True)