from models.database import db

class Ong(db.Model):
    __tablename__ = "ong"

    id_ong = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(18), nullable=False, unique=True)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(150))
    endereco = db.Column(db.String(255))
    descricao = db.Column(db.Text)