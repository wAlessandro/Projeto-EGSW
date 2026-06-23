from models.database import db

class Adocao(db.Model):
    __tablename__ = "adocao"

    id_adocao = db.Column(db.Integer, primary_key=True)

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

    data_solicitacao = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp()
    )

    status = db.Column(db.String(50))
    data_conclusao = db.Column(db.DateTime)
    observacao = db.Column(db.Text)