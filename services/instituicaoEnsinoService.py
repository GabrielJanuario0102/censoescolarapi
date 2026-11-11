from repositories.instituicoesEnsinoRepository import InstituicoesEnsinoRepository

from models.instituicaoEnsino import (
    InstituicaoEnsino,
    InstituicaoEnsinoSchema,
    InstituicaoEnsinoResponseSchema
)


class InstituicaoEnsinoService:

    def __init__(self):

        self.repository = InstituicoesEnsinoRepository()

        # Schema para entrada de uma instituição
        self.instituicaoEnsinoSchema = InstituicaoEnsinoSchema()

        # Schema para entrada de várias instituições
        self.instituicoesEnsinoSchema = InstituicaoEnsinoSchema(many=True)

        # Schema para resposta de uma instituição
        self.instituicaoEnsinoResponseSchema = InstituicaoEnsinoResponseSchema()

        # Schema para resposta de várias instituições
        self.instituicoesEnsinoSchemaResponse = InstituicaoEnsinoResponseSchema(many=True)

    def getAll(self, pagina=1, por_pagina=10):
        pagina = max(1, int(pagina))
        por_pagina = max(1, int(por_pagina))

        lista = self.repository.findAll(
            pagina=pagina,
            por_pagina=por_pagina
        )
        
        return {
            "dados": self.instituicoesEnsinoSchemaResponse.dump(lista),
            "paginacao": {
                "pagina": pagina,
                "por_pagina": por_pagina
            }
        }

    def getById(self, id):
        instituicao = self.repository.findByid(id)

        if instituicao is None:
            return None

        return self.instituicaoEnsinoResponseSchema.dump(instituicao)

    def insert(self, dados: dict):
        dados_validos = self.instituicaoEnsinoSchema.load(dados)

        instituicao = InstituicaoEnsino.from_dict(dados_validos)

        ie = self.repository.insert(instituicao)

        if ie is None:
            return None

        return self.instituicaoEnsinoResponseSchema.dump(ie)

    def update(self, id ,dados: dict):
        dados_validos = self.instituicaoEnsinoSchema.load(dados)

        instituicao = InstituicaoEnsino.from_dict(dados_validos)
        instituicao.id = id
        
        ie = self.repository.update(instituicao)

        if ie is None:
            return None

        return self.instituicaoEnsinoResponseSchema.dump(ie)

    def delete(self, id):
        ie = self.repository.findByid(id)
        
        if ie is None:
                return None
                
        self.repository.delete(id)
                
