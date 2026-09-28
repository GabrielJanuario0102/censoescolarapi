class Usuario:

    def __init__(
        self,
        id: int | None,
        nome: str,
        email: str,
        cpf: str,
        nascimento: str
    ):
        self.id = id
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.nascimento = nascimento

    def __str__(self):
        return (
            "<Usuario>"
            "========================================\n"
            f"ID:                   {self.id}\n"
            f"Nome:                 {self.nome}\n"
            f"Email:                {self.email}\n"
            f"CPF:                  {self.cpf}\n"
            f"Nascimento:           {self.nascimento}\n"
            "========================================"
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "nascimento": self.nascimento
        }

    @classmethod
    def from_dict(cls, dados: dict) -> "Usuario":
        return cls(
            id=dados.get("id"),
            nome=dados.get("nome"),
            email=dados.get("email"),
            cpf=dados.get("cpf"),
            nascimento=dados.get("nascimento")
        )

    @classmethod
    def from_tuple(cls, dados: tuple) -> "Usuario":
        return cls(
            id=dados[0],
            nome=dados[1],
            email=dados[2],
            cpf=dados[3],
            nascimento=dados[4]
        )
