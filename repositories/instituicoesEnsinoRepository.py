from repositories.jsonReader import lerJson


class InstituicoesEnsinoRepository:

    def __init__(self):
        self.lista = lerJson()

    def findAll(self):
        return self.lista

    def findByCoEntidade(self, co_entidade):
        for e in self.lista:
            if int(e.co_entidade) == int(co_entidade):
                return e

        return None

    def insertByCoEntidade(self, instituicao):
        self.lista.append(instituicao)
        return self.lista

    def updateByCoEntidade(self, co_entidade, instituicao):
        for i, e in enumerate(self.lista):
            if int(e.co_entidade) == int(co_entidade):
                self.lista[i] = instituicao
                return self.lista

        return None

    def deleteByCoEntidade(self, co_entidade):
        self.lista = [
            e
            for e in self.lista
            if int(e.co_entidade) != int(co_entidade)
        ]

        return self.lista
