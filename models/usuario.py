class Usuario:
    def __init__(self, nome, email, cpf, nascimento):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.nascimento = nascimento
        
    def __str__(self):
        return (
            "<Usuario>"
            f"- nome: {self.nome}\n"
            f"- email: {self.email}\n"
            f"- cpf: {self.cpf}\n"
            f"- nascimento: {self.nascimento}\n"
            )

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "nascimento": self.nascimento
            }