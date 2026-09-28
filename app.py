from flask import Flask, request
from flask_cors import CORS

from models.instituicaoEnsino import InstituicaoEnsino
from services.instituicaoEnsinoService import InstituicaoEnsinoService

from models.usuario import Usuario
from services.usuarioService import UsuarioService


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


#====================================
#Instituicoes Ensino
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
