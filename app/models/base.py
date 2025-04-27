from app import db
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True  # Indica que esta classe não será criada como tabela, apenas herdada

    id = db.Column(db.Integer, primary_key=True)  # Identificador único para registros
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp de criação do registro

