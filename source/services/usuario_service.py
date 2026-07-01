from flask import flash

from models.usuario import Usuario
from models.endereco import Endereco

from repositories.usuario_repository import UsuarioRepository
from repositories.endereco_repository import EnderecoRepository

from tools import cpf_valido


class UsuarioService:

    @staticmethod
    def cadastrar(form):

        senha = form["senha"]
        confirmar = form["confirmar-senha"]
        cpf = form["cpf"]
        email = form["email"]
        cep = form["cep"]

        if not cpf_valido(cpf):
            return "CPF inválido!"

        if UsuarioRepository.buscar_por_cpf(cpf):
            return "Este CPF já está cadastrado!"

        if senha != confirmar:
            return "As senhas não coincidem!"

        if len(email) > 150:
            return "O e-mail não pode ultrapassar 150 caracteres!"

        if len(cep) > 9:
            return "O CEP não pode ultrapassar 9 caracteres!"

        usuario = Usuario(
            nome=form["nome"],
            cpf=cpf,
            email=email,
            senha=senha,
            telefone=form["telefone"],
            data_nascimento=form["data-nascimento"],
            tipo_usuario="comum"
        )

        endereco = Endereco(
            usuario=usuario,
            cep=cep,
            rua=form["rua"],
            numero=form["numero"],
            bairro=form["bairro"],
            cidade=form["cidade"],
            estado=form["estado"],
        )

        UsuarioRepository.salvar(usuario)
        EnderecoRepository.salvar(endereco)

        UsuarioRepository.commit()

        return None