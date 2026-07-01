from models.database import db
from models.usuario import Usuario


class UsuarioRepository:

    @staticmethod
    def buscar_por_cpf(cpf):
        return Usuario.query.filter_by(cpf=cpf).first()

    @staticmethod
    def salvar(usuario):
        db.session.add(usuario)

    @staticmethod
    def commit():
        db.session.commit()