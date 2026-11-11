from services.usuarioService import UsuarioService
from models.usuario import Usuario

from flask import request, Blueprint

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@usuarios_bp.get("/usuarios")
def getAllUsuarios():
    return UsuarioService().getAll(), 200


@usuarios_bp.get("/usuarios/<int:id>")
def getByIdUsuario(id):
    return UsuarioService().getById(
        id
    ), 200
 

@usuarios_bp.post("/usuarios")
def postUsuario():
    dados = request.json

    usuario = Usuario(**dados)

    print(usuario)

    usuario_inserido_dict = UsuarioService().insert(usuario)

    return (usuario_inserido_dict, 201)


@usuarios_bp.put("/usuarios")
def putUsuario():
    dados = request.json

    usuario = Usuario(**dados)

    return (UsuarioService().update(usuario), 200)


@usuarios_bp.delete("/usuarios/")
def deleteUsuario():
    dados = request.json

    usuario = Usuario(**dados)

    return (UsuarioService().delete(usuario), 200)
