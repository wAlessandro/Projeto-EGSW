from models.database import db

class Endereco(db.Model):
    __tablename__ = "endereco"

    id_endereco = db.Column(db.Integer, primary_key=True)

    id_usuario = db.Column(
        db.Integer,
        db.ForeignKey("usuario.id_usuario", ondelete="CASCADE"),
        nullable=False
    )

    cep = db.Column(db.String(9), nullable=False)
    rua = db.Column(db.String(150), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)

    usuario = db.relationship(
        "Usuario",
        back_populates="enderecos"
    )