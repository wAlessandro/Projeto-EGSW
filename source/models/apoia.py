from models.database import db

class Apoia(db.Model):
    __tablename__ = "apoia"

    id_doacao = db.Column(
        db.Integer,
        db.ForeignKey("doacao.id_doacao"),
        primary_key=True
    )

    id_parceiro = db.Column(
        db.Integer,
        db.ForeignKey("parceiro.id_parceiro"),
        primary_key=True
    )