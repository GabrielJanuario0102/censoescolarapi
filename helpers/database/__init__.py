import sqlite3

DATABASE = 'censoescolar.db'

def get_db_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        
        print("conectou")
    except Exception as e:
        print(f"Erro ao conectar no DATABASE: {e}")
        return None
    finally:
            return conn