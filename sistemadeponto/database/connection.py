# database/db_connection.py
import pg8000

class DatabaseConnection:
    def __init__(self):
        # Configurações de conexão                     
        self.nome_banco = "labdatabase"
        self.usuario = "labdatabase"
        self.senha = "labDatabase2022"
        self.host = "Localhost"
        self.porta = 5432 
        self.conexao = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao = pg8000.connect(
                database=self.nome_banco,
                user=self.usuario,
                password=self.senha,
                host=self.host,
                port=self.porta
            )
            self.cursor = self.conexao.cursor()
            print("Conexão estabelecida com sucesso!")
        except pg8000.DatabaseError as error:
            print(f"Erro ao conectar ao banco de dados: {error}")
            raise

    def __enter__(self):
        self.conectar()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conexao:
            if exc_type is None:
                self.conexao.commit()
            else:
                self.conexao.rollback()
                print(f"Ocorreu um erro: {exc_val}")
            if self.cursor:
                self.cursor.close()
            self.conexao.close()
            print("Conexão fechada.")
