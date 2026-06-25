from main import app
from flask import render_template, request, flash, redirect, url_for
from models.database import db
from models.endereco import Endereco
from models.usuario import Usuario
from tools import cpf_valido


@app.route("/")
def home():
    return render_template("perfil.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html",)


@app.route("/dados-usuario", methods=["GET", "POST"])
def dados_usuario():
    # if request.method == "GET":
    #     return render_template("dados-usuario.html")
    senha = request.form["senha"]
    confirmar_senha = request.form["confirmar-senha"]
    cpf = request.form["cpf"]
    email = request.form["email"]
    cep = request.form["cep"]

    if not cpf_valido(cpf):
        flash("CPF inválido!", "erro")
        return redirect(url_for("cadastro"))
    cpf_existente = Usuario.query.filter_by(cpf=cpf).first()
    
    if cpf_existente:
        flash("Este CPF já está cadastrado!", "erro")
        return redirect(url_for("cadastro"))
    
    if senha != confirmar_senha:
        flash("As senhas não coincidem!", "erro")
        return redirect(url_for("cadastro"))

    if len(email) > 150:
        flash("O e-mail não pode ultrapassar 150 caracteres!", "erro")
        return redirect(url_for("cadastro"))

    if len(cep) > 9:
        flash("O CEP não pode ultrapassar 9 caracteres!", "erro")
        return redirect(url_for("cadastro"))

    # POST: formulário enviado
    usuario = Usuario(
        nome=request.form["nome"],
        cpf=cpf,
        email=request.form["email"],
        senha = senha,  
        telefone=request.form["telefone"],
        data_nascimento=request.form["data-nascimento"],
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
