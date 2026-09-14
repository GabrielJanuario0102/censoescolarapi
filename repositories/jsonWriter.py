import json
from models.instituicaoEnsino import InstituicaoEnsino

def deleteInstituicaoEnsino(co_entidade):
    try:
        with open("./db/db.json", "r", encoding="utf-8") as arquivo:
         dados = json.load(arquivo)
         dados = [InstituicaoEnsino(**item) for item in dados if item["co_entidade"] != co_entidade]
         return dados
                 
    except FileNotFoundError:
            print("Arquivo não encontrado.")
            return None
    
    except json.JSONDecodeError:
            print("O arquivo JSON está inválido.")
            return None