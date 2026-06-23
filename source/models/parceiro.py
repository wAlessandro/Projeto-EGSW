from models.database import db

class Parceiro(db.Model):
    __tablename__ = "parceiro"

    id_parceiro = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50))
    cnpj = db.Column(db.String(18), unique=True)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(150))
    descricao = db.Column(db.Text)