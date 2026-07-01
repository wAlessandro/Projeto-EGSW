from main import app

from flask import render_template, request, flash, redirect, url_for

from services.usuario_service import UsuarioService


@app.route("/")
def home():
    return render_template("perfil.html")


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/dados-usuario", methods=["POST"])
def dados_usuario():

    erro = UsuarioService.cadastrar(request.form)

    if erro:
        flash(erro, "erro")
        return redirect(url_for("cadastro"))

    return f"{request.form['nome']} foi cadastrado com sucesso!"