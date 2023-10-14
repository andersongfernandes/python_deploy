from dotenv import load_dotenv
from pprint import pprint
import requests
import os
from flask import Flask, render_template

app = Flask(__name__)

# cria pagina no site
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')

@app.route("/usuarios/<nome_usuario>")
def usuario(nome_usuario):
    return render_template('usuarios.html',nome_usuario=nome_usuario)

# coloca o site no ar
if __name__ == "__main__":
    app.run(debug=True)