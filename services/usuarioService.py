from repositories.usuarioRepository import UsuarioRepository
from models.usuario import Usuario


class UsuarioService:

    def __init__(self):
        self.repository = UsuarioRepository()

    def getAll(self):
        lista = self.repository.findAll()

        return [item.to_dict() for item in lista]

    def getById(self, id):
        usuario = self.repository.findById(
            id
        )

        return usuario.to_dict()

    def insert(self, usuario: Usuario):
        user: Usuario = self.repository.insert(usuario)
        user_dict = user.to_dict()

        return user_dict

    def update(self, usuario: Usuario):
        user = self.repository.update(usuario)
        user_dict = user.to_dict()

        return user_dict

    def delete(self, usuario: Usuario):
        user = self.repository.delete(usuario)

        return {"DELETE": user.__str__()}
