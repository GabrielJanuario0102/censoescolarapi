from datetime import datetime

from marshmallow import Schema, fields, validate



class InstituicaoEnsino:

    def __init__(
        self,
        id: int | None,
        no_entidade: str,
        co_entidade: int,
        no_uf: str,
        sg_uf: str,
        co_uf: int,
        no_municipio: str,
        co_municipio: int,
        no_mesorregiao: str | None,
        co_mesorregiao: int | None,
        no_microrregiao: str | None,
        co_microrregiao: int | None,
        nu_ano_censo: int,
        no_regiao: str | None,
        co_regiao: int | None,
        qt_mat_bas: int,
        qt_mat_inf: int,
        qt_mat_fund: int,
        qt_mat_med: int,
        qt_mat_prof: int,
        qt_mat_eja: int,
        qt_mat_esp: int,
        created_at: datetime | None,
        deleted_at: datetime | None
    ):
        self.id = id
        self.no_entidade = no_entidade
        self.co_entidade = co_entidade
        self.no_uf = no_uf
        self.sg_uf = sg_uf
        self.co_uf = co_uf
        self.no_municipio = no_municipio
        self.co_municipio = co_municipio
        self.no_mesorregiao = no_mesorregiao
        self.co_mesorregiao = co_mesorregiao
        self.no_microrregiao = no_microrregiao
        self.co_microrregiao = co_microrregiao
        self.nu_ano_censo = nu_ano_censo
        self.no_regiao = no_regiao
        self.co_regiao = co_regiao
        self.qt_mat_bas = qt_mat_bas
        self.qt_mat_inf = qt_mat_inf
        self.qt_mat_fund = qt_mat_fund
        self.qt_mat_med = qt_mat_med
        self.qt_mat_prof = qt_mat_prof
        self.qt_mat_eja = qt_mat_eja
        self.qt_mat_esp = qt_mat_esp
        self.created_at = created_at
        self.deleted_at = deleted_at

    def __str__(self):
        return (
            "<Instituicao Ensino>"
            "========================================\n"
            f"ID:                   {self.id}\n"
            f"Instituição:          {self.no_entidade}\n"
            f"Código da entidade:   {self.co_entidade}\n"
            f"UF:                   {self.no_uf}\n"
            f"Sigla UF:             {self.sg_uf}\n"
            f"Código UF:             {self.co_uf}\n"
            f"Município:             {self.no_municipio}\n"
            f"Código município:      {self.co_municipio}\n"
            f"Mesorregião:           {self.no_mesorregiao}\n"
            f"Código mesorregião:    {self.co_mesorregiao}\n"
            f"Microrregião:          {self.no_microrregiao}\n"
            f"Código microrregião:   {self.co_microrregiao}\n"
            f"Região:                {self.no_regiao}\n"
            f"Código região:         {self.co_regiao}\n"
            f"Ano do Censo:          {self.nu_ano_censo}\n"
            f"Criado em:             {self.created_at}\n"
            f"Deletado em:           {self.deleted_at}\n"
            "----------------------------------------\n"
            f"Matriculados Básico:   {self.qt_mat_bas}\n"
            f"  Educação Infantil:   {self.qt_mat_inf}\n"
            f"  Ensino Fundamental:  {self.qt_mat_fund}\n"
            f"  Ensino Médio:        {self.qt_mat_med}\n"
            f"  Ensino Profissional: {self.qt_mat_prof}\n"
            f"  EJA:                 {self.qt_mat_eja}\n"
            f"  Educação Especial:   {self.qt_mat_esp}\n"
            "========================================"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "no_entidade": self.no_entidade,
            "co_entidade": self.co_entidade,
            "no_uf": self.no_uf,
            "sg_uf": self.sg_uf,
            "co_uf": self.co_uf,
            "no_municipio": self.no_municipio,
            "co_municipio": self.co_municipio,
            "no_mesorregiao": self.no_mesorregiao,
            "co_mesorregiao": self.co_mesorregiao,
            "no_microrregiao": self.no_microrregiao,
            "co_microrregiao": self.co_microrregiao,
            "nu_ano_censo": self.nu_ano_censo,
            "no_regiao": self.no_regiao,
            "co_regiao": self.co_regiao,
            "qt_mat_bas": self.qt_mat_bas,
            "qt_mat_inf": self.qt_mat_inf,
            "qt_mat_fund": self.qt_mat_fund,
            "qt_mat_med": self.qt_mat_med,
            "qt_mat_prof": self.qt_mat_prof,
            "qt_mat_eja": self.qt_mat_eja,
            "qt_mat_esp": self.qt_mat_esp,
            "created_at": self.created_at,
            "deleted_at": self.deleted_at
        }

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(
            id=dados.get("id"),
            no_entidade=dados.get("no_entidade"),
            co_entidade=dados.get("co_entidade"),
            no_uf=dados.get("no_uf"),
            sg_uf=dados.get("sg_uf"),
            co_uf=dados.get("co_uf"),
            no_municipio=dados.get("no_municipio"),
            co_municipio=dados.get("co_municipio"),
            no_mesorregiao=dados.get("no_mesorregiao"),
            co_mesorregiao=dados.get("co_mesorregiao"),
            no_microrregiao=dados.get("no_microrregiao"),
            co_microrregiao=dados.get("co_microrregiao"),
            nu_ano_censo=dados.get("nu_ano_censo"),
            no_regiao=dados.get("no_regiao"),
            co_regiao=dados.get("co_regiao"),
            qt_mat_bas=dados.get("qt_mat_bas", 0),
            qt_mat_inf=dados.get("qt_mat_inf", 0),
            qt_mat_fund=dados.get("qt_mat_fund", 0),
            qt_mat_med=dados.get("qt_mat_med", 0),
            qt_mat_prof=dados.get("qt_mat_prof", 0),
            qt_mat_eja=dados.get("qt_mat_eja", 0),
            qt_mat_esp=dados.get("qt_mat_esp", 0),
            created_at=dados.get("created_at"),
            deleted_at=dados.get("deleted_at")
        )

    @classmethod
    def from_tuple(cls, dados: tuple):
        created_at = dados[22]
        deleted_at = dados[23]

        if isinstance(created_at, str):
            created_at = datetime.fromisoformat(created_at)

        if isinstance(deleted_at, str):
            deleted_at = datetime.fromisoformat(deleted_at) 

        return cls(
            id=dados[0],
            no_entidade=dados[1],
            co_entidade=dados[2],
            no_uf=dados[3],
            sg_uf=dados[4],
            co_uf=dados[5],
            no_municipio=dados[6],
            co_municipio=dados[7],
            no_mesorregiao=dados[8],
            co_mesorregiao=dados[9],
            no_microrregiao=dados[10],
            co_microrregiao=dados[11],
            nu_ano_censo=dados[12],
            no_regiao=dados[13],
            co_regiao=dados[14],
            qt_mat_bas=dados[15],
            qt_mat_inf=dados[16],
            qt_mat_fund=dados[17],
            qt_mat_med=dados[18],
            qt_mat_prof=dados[19],
            qt_mat_eja=dados[20],
            qt_mat_esp=dados[21],
            created_at=created_at,
            deleted_at=deleted_at
        )
        
class InstituicaoEnsinoSchema(Schema):

    no_entidade = fields.Str(
        required=True,
        validate=validate.Length(
            min=1,
            max=255
        )
    )

    co_entidade = fields.Int(
        required=True,
        validate=validate.Range(
            min=0
        )
    )

    no_uf = fields.Str(
        required=True,
        validate=validate.Length(
            min=1,
            max=255
        )
    )

    sg_uf = fields.Str(
        required=True,
        validate=validate.Length(
            min=2,
            max=2
        )
    )

    co_uf = fields.Int(
        required=True,
        validate=validate.Range(
            min=0
        )
    )

    no_municipio = fields.Str(
        required=True,
        validate=validate.Length(
            min=1,
            max=255
        )
    )

    co_municipio = fields.Int(
        required=True,
        validate=validate.Range(
            min=0
        )
    )

    no_mesorregiao = fields.Str(
        allow_none=True,
        validate=validate.Length(
            max=255
        )
    )

    co_mesorregiao = fields.Int(
        allow_none=True,
        validate=validate.Range(
            min=0
        )
    )

    no_microrregiao = fields.Str(
        allow_none=True,
        validate=validate.Length(
            max=255
        )
    )

    co_microrregiao = fields.Int(
        allow_none=True,
        validate=validate.Range(
            min=0
        )
    )

    nu_ano_censo = fields.Int(
        required=True,
        validate=validate.Range(
            min=0
        )
    )

    no_regiao = fields.Str(
        allow_none=True,
        validate=validate.Length(
            max=255
        )
    )

    co_regiao = fields.Int(
        allow_none=True,
        validate=validate.Range(
            min=0
        )
    )

    qt_mat_bas = fields.Int(
        load_default=0,
        validate=validate.Range(
            min=0
        )
    )

    qt_mat_inf = fields.Int(
        load_default=0,
        validate=validate.Range(
            min=0
        )
    )

    qt_mat_fund = fields.Int(
        load_default=0,
        validate=validate.Range(
            min=0
        )
    )

    qt_mat_med = fields.Int(
        load_default=0,
        validate=validate.Range(
            min=0
        )
    )

    qt_mat_prof = fields.Int(
        load_default=0,
        validate=validate.Range(
            min=0
        )
    )

    qt_mat_eja = fields.Int(
        load_default=0,
        validate=validate.Range(
            min=0
        )
    )

    qt_mat_esp = fields.Int(
        load_default=0,
        validate=validate.Range(
            min=0
        )
    )

class InstituicaoEnsinoResponseSchema(Schema):

    id = fields.Int()

    no_entidade = fields.Str()

    co_entidade = fields.Int()

    no_uf = fields.Str()

    sg_uf = fields.Str()

    co_uf = fields.Int()

    no_municipio = fields.Str()

    co_municipio = fields.Int()

    no_mesorregiao = fields.Str(
        allow_none=True
    )

    co_mesorregiao = fields.Int(
        allow_none=True
    )

    no_microrregiao = fields.Str(
        allow_none=True
    )

    co_microrregiao = fields.Int(
        allow_none=True
    )

    nu_ano_censo = fields.Int()

    no_regiao = fields.Str(
        allow_none=True
    )

    co_regiao = fields.Int(
        allow_none=True
    )

    qt_mat_bas = fields.Int()

    qt_mat_inf = fields.Int()

    qt_mat_fund = fields.Int()

    qt_mat_med = fields.Int()

    qt_mat_prof = fields.Int()

    qt_mat_eja = fields.Int()

    qt_mat_esp = fields.Int()

    created_at = fields.DateTime(
        allow_none=True
    )

    deleted_at = fields.DateTime(
        allow_none=True
    )