from main import app
from flask import render_template, request, redirect, url_for
from flask import request
from models.database import db
from models.endereco import Endereco
from models.usuario import Usuario

@app.route("/")
def home():
    return render_template("perfil.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html",)


@app.route("/dados-usuario", methods=["GET", "POST"])
def dados_usuario():
    if request.method == "GET":
        return render_template("dados-usuario.html")

    # POST: formulário enviado
    usuario = Usuario(
        nome=request.form["nome"],
        cpf=request.form["cpf"],
        email=request.form["email"],
        senha=request.form["senha"],  # idealmente usar hash
        telefone=request.form["telefone"],
        data_nascimento=request.form.get("data_nascimento"),
        tipo_usuario="comum"
    )
    endereco = Endereco(
        usuario=usuario,
        cep=request.form["cep"],
        rua=request.form["rua"],
        numero=request.form["numero"],
        bairro=request.form["bairro"],
        cidade=request.form["cidade"],
        estado=request.form["estado"],
        
    )

    db.session.add(usuario)
    db.session.add(endereco)
    db.session.commit()

    return f"{request.form["nome"]} foi cadastrado com sucesso!"
