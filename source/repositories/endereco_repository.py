from models.database import db
from models.endereco import Endereco


class EnderecoRepository:

    @staticmethod
    def salvar(endereco):
        db.session.add(endereco)

    @staticmethod
    def commit():
        db.session.commit()