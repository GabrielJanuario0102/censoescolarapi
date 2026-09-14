from flask import Flask, request
from flask_cors import CORS

from models.instituicaoEnsino import InstituicaoEnsino
from repositories.instituicoesEnsinoRepository import InstituicoesEnsinoRepository
from services.instituicaoEnsinoService import InstituicaoEnsinoService


app = Flask(__name__)

CORS(app)

repository = InstituicoesEnsinoRepository()
service = InstituicaoEnsinoService(repository)


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
    return service.getAll(), 200


@app.get("/instituicoesEnsino/<int:co_entidade>")
def getByCoEntidadeInstituicoes(co_entidade):
    return service.getByCoEntidade(
        co_entidade
    ), 200


@app.post("/instituicoesEnsino")
def postInstituicoes():
    dados = request.json

    instituicao = InstituicaoEnsino(
        dados["no_entidade"],
        dados["co_entidade"],
        dados["no_uf"],
        dados["sg_uf"],
        dados["co_uf"],
        dados["no_municipio"],
        dados["co_municipio"],
        dados["no_mesorregiao"],
        dados["co_mesorregiao"],
        dados["no_microrregiao"],
        dados["co_microrregiao"],
        dados["nu_ano_censo"],
        dados["no_regiao"],
        dados["co_regiao"],
        dados["qt_mat_bas"],
        dados["qt_mat_inf"],
        dados["qt_mat_fund"],
        dados["qt_mat_med"],
        dados["qt_mat_prof"],
        dados["qt_mat_eja"],
        dados["qt_mat_esp"]
    )

    return service.insertByCoEntidade(
        instituicao
    ), 200


@app.put("/instituicoesEnsino/<int:co_entidade>")
def putInstituicoes(co_entidade):
    dados = request.json

    instituicao = InstituicaoEnsino(
        dados["no_entidade"],
        dados["co_entidade"],
        dados["no_uf"],
        dados["sg_uf"],
        dados["co_uf"],
        dados["no_municipio"],
        dados["co_municipio"],
        dados["no_mesorregiao"],
        dados["co_mesorregiao"],
        dados["no_microrregiao"],
        dados["co_microrregiao"],
        dados["nu_ano_censo"],
        dados["no_regiao"],
        dados["co_regiao"],
        dados["qt_mat_bas"],
        dados["qt_mat_inf"],
        dados["qt_mat_fund"],
        dados["qt_mat_med"],
        dados["qt_mat_prof"],
        dados["qt_mat_eja"],
        dados["qt_mat_esp"]
    )

    return service.updateByCoEntidade(
        co_entidade,
        instituicao
    ), 200


@app.delete("/instituicoesEnsino/<int:co_entidade>")
def deleteInstituicoes(co_entidade):
    return service.deleteByCoEntidade(
        co_entidade
    ), 200


def main(arg=[]):
    app.run(debug=True)
