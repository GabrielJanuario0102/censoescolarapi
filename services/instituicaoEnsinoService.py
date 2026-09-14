from repositories.instituicoesEnsinoRepository import InstituicoesEnsinoRepository


class InstituicaoEnsinoService:

    def __init__(self, repository):
        self.repository = repository

    def getAll(self):
        lista = self.repository.findAll()

        return [
            item.to_dict()
            for item in lista
        ]

    def getByCoEntidade(self, co_entidade):
        instituicao = self.repository.findByCoEntidade(
            co_entidade
        )

        return instituicao.to_dict()

    def insertByCoEntidade(self, instituicao):
        lista = self.repository.insertByCoEntidade(
            instituicao
        )

        return [
            item.to_dict()
            for item in lista
        ]

    def updateByCoEntidade(self, co_entidade, instituicao):
        lista = self.repository.updateByCoEntidade(
            co_entidade,
            instituicao
        )

        return [
            item.to_dict()
            for item in lista
        ]

    def deleteByCoEntidade(self, co_entidade):
        lista = self.repository.deleteByCoEntidade(
            co_entidade
        )

        return [
            item.to_dict()
            for item in lista
        ]
