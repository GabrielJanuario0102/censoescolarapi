from helpers.database import get_db_connection
from models.instituicaoEnsino import InstituicaoEnsino

class InstituicoesEnsinoRepository:

    
    def findAll(self, pagina=1, por_pagina=10):
        lista = []
        conn = None

        try:
            pagina = max(1, int(pagina))
            por_pagina = max(1, int(por_pagina))

            offset = (pagina - 1) * por_pagina

            conn = get_db_connection()
            cursor = conn.cursor()

            sql = """
                SELECT *
                FROM tb_instituicao_ensino
                WHERE deleted_at IS NULL
                ORDER BY id
                LIMIT ? OFFSET ?
            """

            cursor.execute(sql, (por_pagina, offset))
            dataset = cursor.fetchall()

            lista = [
                InstituicaoEnsino.from_tuple(row)
                for row in dataset
            ]

        except Exception as e:
            print(f"Erro no findAll: {e}")

        finally:
            if conn is not None:
                conn.close()

        return lista


    def findByid(self, id):
        ie = None
        conn = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            sql = """
                SELECT *
                FROM tb_instituicao_ensino
                WHERE id = ?
                AND deleted_at IS NULL
            """

            cursor.execute(sql, (int(id),))
            data = cursor.fetchone()

            if data is not None:
                ie = InstituicaoEnsino.from_tuple(data)

        except Exception as e:
            print(f"Erro no findById: {e}")

        finally:
            if conn is not None:
                conn.close()

        return ie

    def insert(self, instituicao: InstituicaoEnsino):
        ie = None
        conn = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            sql = """
                INSERT INTO tb_instituicao_ensino (
                    no_entidade,
                    co_entidade,
                    no_uf,
                    sg_uf,
                    co_uf,
                    no_municipio,
                    co_municipio,
                    no_mesorregiao,
                    co_mesorregiao,
                    no_microrregiao,
                    co_microrregiao,
                    nu_ano_censo,
                    no_regiao,
                    co_regiao,
                    qt_mat_bas,
                    qt_mat_inf,
                    qt_mat_fund,
                    qt_mat_med,
                    qt_mat_prof,
                    qt_mat_eja,
                    qt_mat_esp
                )
                VALUES (
                    :no_entidade,
                    :co_entidade,
                    :no_uf,
                    :sg_uf,
                    :co_uf,
                    :no_municipio,
                    :co_municipio,
                    :no_mesorregiao,
                    :co_mesorregiao,
                    :no_microrregiao,
                    :co_microrregiao,
                    :nu_ano_censo,
                    :no_regiao,
                    :co_regiao,
                    :qt_mat_bas,
                    :qt_mat_inf,
                    :qt_mat_fund,
                    :qt_mat_med,
                    :qt_mat_prof,
                    :qt_mat_eja,
                    :qt_mat_esp
                )
                RETURNING *
            """

            cursor.execute(sql, instituicao.to_dict())

            dataset = cursor.fetchone()

            if dataset is not None:
                ie = InstituicaoEnsino.from_tuple(dataset)

            conn.commit()

        except Exception as e:
            print(f"Erro de insert: {e}")

        finally:
            if conn is not None:
                conn.close()

        return ie

    def update(self, instituicao: InstituicaoEnsino):
        ie = None
        conn = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            sql = """
                UPDATE tb_instituicao_ensino
                SET
                    no_entidade = :no_entidade,
                    co_entidade = :co_entidade,
                    no_uf = :no_uf,
                    sg_uf = :sg_uf,
                    co_uf = :co_uf,
                    no_municipio = :no_municipio,
                    co_municipio = :co_municipio,
                    no_mesorregiao = :no_mesorregiao,
                    co_mesorregiao = :co_mesorregiao,
                    no_microrregiao = :no_microrregiao,
                    co_microrregiao = :co_microrregiao,
                    nu_ano_censo = :nu_ano_censo,
                    no_regiao = :no_regiao,
                    co_regiao = :co_regiao,
                    qt_mat_bas = :qt_mat_bas,
                    qt_mat_inf = :qt_mat_inf,
                    qt_mat_fund = :qt_mat_fund,
                    qt_mat_med = :qt_mat_med,
                    qt_mat_prof = :qt_mat_prof,
                    qt_mat_eja = :qt_mat_eja,
                    qt_mat_esp = :qt_mat_esp
                WHERE id = :id
                AND deleted_at IS NULL
                RETURNING *
            """

            cursor.execute(sql, instituicao.to_dict())

            dataset = cursor.fetchone()

            if dataset is not None:
                ie = InstituicaoEnsino.from_tuple(dataset)

            conn.commit()

        except Exception as e:
            print(f"Erro no update de Instituicao: {e}")

        finally:
            if conn is not None:
                conn.close()

        return ie

    def delete(self, id: int):
        conn = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            sql = """
                UPDATE tb_instituicao_ensino
                SET deleted_at = CURRENT_TIMESTAMP
                WHERE id = :id
                AND deleted_at IS NULL
                RETURNING *
            """

            cursor.execute(sql, {"id": id})
            
            conn.commit()

        except Exception as e:
            print(f"Erro ao deletar: {e}")

        finally:
            if conn is not None:
                conn.close()

        return