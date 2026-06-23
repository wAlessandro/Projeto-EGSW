from models.database import db

class Pet(db.Model):
    __tablename__ = "pet"

    id_pet = db.Column(db.Integer, primary_key=True)

    id_ong = db.Column(
        db.Integer,
        db.ForeignKey("ong.id_ong", ondelete="CASCADE"),
        nullable=False
    )

    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50))
    raca = db.Column(db.String(100))
    sexo = db.Column(db.Enum("Macho", "Fêmea"))
    idade = db.Column(db.Integer)
    porte = db.Column(db.Enum("Pequeno", "Médio", "Grande"))
    descricao = db.Column(db.Text)
    status = db.Column(db.String(50))
    data_cadastro = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp()
    )