# models/funcionario.py
import pg8000
from datetime import datetime

class Funcionario:
    def __init__(self, db_connection):
        self.db = db_connection

    def inserir(self, nome, cargo, data_contratacao):
        if not nome or not cargo or not data_contratacao:
            raise ValueError("Nome, cargo e data de contratação são obrigatórios")
            
        try:
            self.db.cursor.execute("""
                INSERT INTO Funcionarios (nome, cargo, data_contratacao)
                VALUES (%s, %s, %s)
                RETURNING funcionario_id
            """, (nome, cargo, data_contratacao))
            return self.db.cursor.fetchone()[0]
        except pg8000.DatabaseError as error:
            raise Exception(f"Erro ao inserir funcionário: {error}")

    def atualizar(self, funcionario_id, nome=None, cargo=None):
        """
        Atualiza os dados de um funcionário, mantendo valores existentes quando não especificados
        
        Args:
            funcionario_id: ID do funcionário a ser atualizado
            nome: Novo nome (opcional)
            cargo: Novo cargo (opcional)
        """
        try:
            # Primeiro, obtém os dados atuais do funcionário
            self.db.cursor.execute("""
                SELECT nome, cargo
                FROM Funcionarios
                WHERE funcionario_id = %s
            """, (funcionario_id,))
            
            resultado = self.db.cursor.fetchone()
            if not resultado:
                raise ValueError(f"Funcionário com ID {funcionario_id} não encontrado")
                
            nome_atual, cargo_atual = resultado
            
            # Usa os valores atuais se os novos não forem fornecidos
            nome_final = nome if nome is not None else nome_atual
            cargo_final = cargo if cargo is not None else cargo_atual
            
            # Realiza a atualização
            self.db.cursor.execute("""
                UPDATE Funcionarios
                SET nome = %s, 
                    cargo = %s,
                    data_atualizacao = CURRENT_TIMESTAMP
                WHERE funcionario_id = %s
            """, (nome_final, cargo_final, funcionario_id))
            
            if self.db.cursor.rowcount == 0:
                raise ValueError(f"Funcionário com ID {funcionario_id} não encontrado")
                
        except pg8000.DatabaseError as error:
            raise Exception(f"Erro ao atualizar funcionário: {error}")

    def remover(self, funcionario_id):
        try:
            # Verifica se o funcionário existe
            self.db.cursor.execute("""
                SELECT nome FROM Funcionarios WHERE funcionario_id = %s
            """, (funcionario_id,))
            
            if not self.db.cursor.fetchone():
                raise ValueError(f"Funcionário com ID {funcionario_id} não encontrado")
            
            # Remove registros de ponto relacionados
            self.db.cursor.execute("""
                DELETE FROM Registros_de_Ponto 
                WHERE funcionario_id = %s
            """, (funcionario_id,))
            
            # Remove o funcionário
            self.db.cursor.execute("""
                DELETE FROM Funcionarios 
                WHERE funcionario_id = %s
            """, (funcionario_id,))
            
        except pg8000.DatabaseError as error:
            raise Exception(f"Erro ao remover funcionário: {error}")

    def listar_todos(self):
        try:
            self.db.cursor.execute("""
                SELECT 
                    funcionario_id, 
                    nome,
                    cargo,
                    data_contratacao,
                    data_atualizacao
                FROM Funcionarios 
                ORDER BY nome
            """)
            return self.db.cursor.fetchall()
        except pg8000.DatabaseError as error:
            raise Exception(f"Erro ao listar funcionários: {error}")

    def buscar_por_id(self, funcionario_id):
        try:
            self.db.cursor.execute("""
                SELECT 
                    funcionario_id, 
                    nome,
                    cargo,
                    data_contratacao,
                    data_atualizacao
                FROM Funcionarios 
                WHERE funcionario_id = %s
            """, (funcionario_id,))
            return self.db.cursor.fetchone()
        except pg8000.DatabaseError as error:
            raise Exception(f"Erro ao buscar funcionário: {error}")