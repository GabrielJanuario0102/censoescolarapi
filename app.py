from flask import Flask, request

from flask_cors import CORS

from services.instituicaoEnsinoService import InstituicaoEnsinoService

from services.usuarioService import UsuarioService

from models.usuario import Usuario

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


# ====================================
# Instituições de Ensino


@app.get("/instituicoesEnsino")
def getAllInstituicoes():
    pagina = request.args.get("pagina", default=1, type=int)
    por_pagina = request.args.get("por_pagina", default=10, type=int)

    resultado = InstituicaoEnsinoService().getAll(
        pagina=pagina,
        por_pagina=por_pagina
    )

    return resultado, 200


@app.get("/instituicoesEnsino/<int:id>")
def getByCoEntidadeInstituicoes(id):

    instituicao = InstituicaoEnsinoService().getById(id)

    if instituicao is None:
        return {
            "erro": "Instituição de ensino não encontrada"
        }, 404

    return instituicao, 200


@app.post("/instituicoesEnsino")
def postInstituicoes():

    dados = request.get_json()

    instituicao = InstituicaoEnsinoService().insert(dados)

    if instituicao is None:
        return {
            "erro": "Não foi possível inserir a instituição"
        }, 400

    return instituicao, 201


@app.put("/instituicoesEnsino")
def putInstituicoes():

    dados = request.get_json()

    instituicao = InstituicaoEnsinoService().update(dados)

    if instituicao is None:
        return {
            "erro": "Instituição de ensino não encontrada"
        }, 404

    return instituicao, 200


@app.delete("/instituicoesEnsino")
def deleteInstituicoes():

    dados = request.get_json()

    instituicao = InstituicaoEnsinoService().delete(dados)

    if instituicao is None:
        return {
            "erro": "Instituição de ensino não encontrada"
        }, 404

    return instituicao, 200

#======================================================================
#Usuario

@app.get("/usuarios")
def getAllUsuarios():
    return UsuarioService().getAll(), 200


@app.get("/usuarios/<int:id>")
def getByIdUsuario(id):
    return UsuarioService().getById(
        id
    ), 200


@app.post("/usuarios")
def postUsuario():
    dados = request.json

    usuario = Usuario(**dados)

    print(usuario)

    usuario_inserido_dict = UsuarioService().insert(usuario)

    return (usuario_inserido_dict, 201)


@app.put("/usuarios")
def putUsuario():
    dados = request.json

    usuario = Usuario(**dados)

    return (UsuarioService().update(usuario), 200)


@app.delete("/usuarios/")
def deleteUsuario():
    dados = request.json

    usuario = Usuario(**dados)

    return (UsuarioService().delete(usuario), 200)



def main(arg=[]):
    app.run(debug=True)
