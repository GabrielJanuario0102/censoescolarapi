from flask import Flask, request
from flask_cors import CORS

from models.instituicaoEnsino import InstituicaoEnsino
from services.instituicaoEnsinoService import InstituicaoEnsinoService


app = Flask(__name__)

CORS(app)


@app.route("/")
def index():
    return {
        "versao": "0.0.1"
    }, 200


@app.route("/health")
def health():
    return {
        "health": "ok"
    }, 200


@app.get("/instituicoesEnsino")
def getAllInstituicoes():
    return InstituicaoEnsinoService().getAll(), 200


@app.get("/instituicoesEnsino/<int:id>")
def getByCoEntidadeInstituicoes(id):
    return InstituicaoEnsinoService().getById(
        id
    ), 200


@app.post("/instituicoesEnsino")
def postInstituicoes():
    dados = request.json

    instituicao = InstituicaoEnsino(**dados)

    print(instituicao)
    
    instituicao_inserida_dict = InstituicaoEnsinoService().insert(instituicao)
    
    return (instituicao_inserida_dict, 201)


@app.put("/instituicoesEnsino")
def putInstituicoes():
    dados = request.json

    instituicao = InstituicaoEnsino(**dados)

    return (InstituicaoEnsinoService().update(instituicao), 200)


@app.delete("/instituicoesEnsino/")
def deleteInstituicoes():
    dados = request.json
    
    instituicao = InstituicaoEnsino(**dados)
    
    return (InstituicaoEnsinoService().delete(instituicao), 200)


def main(arg=[]):
    app.run(debug=True)
