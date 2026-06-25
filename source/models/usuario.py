from models.database import db

class Usuario(db.Model):
    __tablename__ = "usuario"

    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=False)
    senha = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(20))
    data_nascimento = db.Column(db.Date)
    data_cadastro = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp()
    )
    tipo_usuario = db.Column(db.String(50))

    enderecos = db.relationship(
        "Endereco",
        back_populates="usuario",
        cascade="all, delete-orphan"
    )