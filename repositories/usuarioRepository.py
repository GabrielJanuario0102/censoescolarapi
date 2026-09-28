from helpers.database import get_db_connection
from models.usuario import Usuario


class UsuarioRepository:

    def __init__(self):
        self

    def findAll(self):
        lista = []
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            sql = 'SELECT * FROM tb_usuario'
            cursor.execute(sql)

            dataset = cursor.fetchall()

            lista = [Usuario.from_tuple(row) for row in dataset]

        except Exception as e:
            print(f"Erro no findAll: {e}")

        finally:
            if conn is not None:
                conn.close()

        return lista

    def findById(self, id):
        usuario = None

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            sql = """
                SELECT * FROM tb_usuario
                WHERE id = ?
            """

            cursor.execute(sql, (int(id),))

            data = cursor.fetchone()

            if data is not None:
                usuario = Usuario.from_tuple(data)

        except Exception as e:
            print(f"Erro no findById: {e}")

        finally:
            if conn is not None:
                conn.close()

        return usuario

    def insert(self, usuario: Usuario):

        user: Usuario = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            sql = """
                INSERT INTO tb_usuario (
                    nome,
                    email,
                    cpf,
                    nascimento
                ) VALUES (
                    :nome,
                    :email,
                    :cpf,
                    :nascimento
                )
                RETURNING *
            """

            cursor.execute(sql, usuario.to_dict())

            dataset = cursor.fetchone()

            user: Usuario = Usuario.from_tuple(dataset)

            conn.commit()

        except Exception as e:
            print(f"Erro de insert: {e}")

        finally:
            if conn is not None:
                conn.close()

        return user

    def update(self, usuario: Usuario):

        user: Usuario = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            sql = """
                UPDATE tb_usuario
                SET
                    nome = :nome,
                    email = :email,
                    cpf = :cpf,
                    nascimento = :nascimento
                WHERE id = :id
                RETURNING *
            """

            cursor.execute(sql, usuario.to_dict())

            dataset = cursor.fetchone()

            user: Usuario = Usuario.from_tuple(dataset)

            conn.commit()

        except Exception as e:
            print(f"Erro no update de Usuario: {e}")

        finally:
            if conn is not None:
                conn.close()

        return user

    def delete(self, usuario: Usuario):

        user: Usuario = None

        try:

            conn = get_db_connection()
            cursor = conn.cursor()

            user = usuario

            sql = """
                DELETE FROM tb_usuario
                WHERE id = :id
            """

            cursor.execute(sql, user.to_dict())

            conn.commit()

        except Exception as e:
            print(f"Erro ao deletar Usuario: {e}")

        finally:
            if conn is not None:
                conn.close()

        return user
