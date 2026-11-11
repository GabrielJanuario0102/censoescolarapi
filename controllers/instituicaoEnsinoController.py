from services.instituicaoEnsinoService import InstituicaoEnsinoService

from helpers.loggers import logger

from flask import request, Blueprint

instituicao_ensino_bp = Blueprint('instituicaoensino', __name__, url_prefix='/instituicoesEnsino')

@instituicao_ensino_bp.get("/")
def getAllInstituicoes():
    pagina = request.args.get("pagina", default=1, type=int)
    por_pagina = request.args.get("por_pagina", default=10, type=int)

    resultado = InstituicaoEnsinoService().getAll(
        pagina=pagina,
        por_pagina=por_pagina
    )

    logger.info("listando instituicoes: GET /instituicoesEnsino")
    return resultado, 200


@instituicao_ensino_bp.get("/<int:id>")
def getByCoEntidadeInstituicoes(id):

    instituicao = InstituicaoEnsinoService().getById(id)

    if instituicao is None:
        return {
            "erro": "Instituição de ensino não encontrada"
        }, 404

    logger.info(f"buscando instituicao: GET /instituicoesEnsino/{id}")
    return instituicao, 200


@instituicao_ensino_bp.post("")
def postInstituicoes():

    dados = request.get_json()

    instituicao = InstituicaoEnsinoService().insert(dados)

    if instituicao is None:
        return {
            "erro": "Não foi possível inserir a instituição"
        }, 400

    logger.info("adicionando instituicao: POST /instituicoesEnsino")
    return instituicao, 201


@instituicao_ensino_bp.put("/<int:id>")
def putInstituicoes(id):

    dados = request.get_json()

    instituicao = InstituicaoEnsinoService().update(id, dados)

    if instituicao is None:
        return {
            "erro": "Instituição de ensino não encontrada"
        }, 404

    logger.info(f"atualizando instituicao: PUT /instituicoesEnsino/{id}")
    return instituicao, 200


@instituicao_ensino_bp.delete("/<int:id>")
def deleteInstituicoes(id):

    InstituicaoEnsinoService().delete(id)
    logger.info(f"deletando instituicao: DELETE /instituicaoEnsino/{id}")
    return {"message": f"IE de id {id} deletada com sucesso"}, 200
