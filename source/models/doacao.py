from models.database import db

class Doacao(db.Model):
    __tablename__ = "doacao"

    id_doacao = db.Column(db.Integer, primary_key=True)

    id_usuario = db.Column(
        db.Integer,
        db.ForeignKey("usuario.id_usuario"),
        nullable=False
    )

    id_pet = db.Column(
        db.Integer,
        db.ForeignKey("pet.id_pet"),
        nullable=False
    )

    valor = db.Column(db.Numeric(10, 2), nullable=False)
    data_doacao = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp()
    )
    forma_pagamento = db.Column(db.String(50))
    observacao = db.Column(db.Text)