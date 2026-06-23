from flask import Flask
# import mysql.connector
from models.database import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:SENHADACONEXAO@localhost/ong_animais" #usuario:senha da conexao
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Importa os models para registrá-los

from models.usuario import Usuario
from models.endereco import Endereco
from models.ong import Ong
from models.parceiro import Parceiro
from models.pet import Pet
from models.doacao import Doacao
from models.apoia import Apoia
from models.adocao import Adocao

with app.app_context():
    db.create_all()
    
from routes import *

if __name__ == "__main__":
    app.run(debug=True)
