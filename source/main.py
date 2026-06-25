from flask import Flask
from models.database import db
from create_db import *

app = Flask(__name__)
app.secret_key = "chave_secreta"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:%40bost4fedid4%24@localhost/ong_animais"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

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