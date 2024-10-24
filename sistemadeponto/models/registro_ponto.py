# models/registro_ponto.py
from datetime import datetime
import pg8000


class RegistroPonto:
    def __init__(self, db_connection):
        self.db = db_connection

    def inserir(self, funcionario_id, data, hora_entrada, hora_saida):
        if not all([funcionario_id, data, hora_entrada, hora_saida]):
            raise ValueError("Todos os campos são obrigatórios")
            
        if not self._validar_horarios(hora_entrada, hora_saida):
            raise ValueError("Hora de saída deve ser posterior à hora de entrada")
            
        try:
            self.db.cursor.execute("""
                INSERT INTO Registros_de_Ponto (
                    funcionario_id, data, hora_entrada, hora_saida
                )
                VALUES (%s, %s, %s, %s)
                RETURNING registro_id
            """, (funcionario_id, data, hora_entrada, hora_saida))
            return self.db.cursor.fetchone()[0]
        except pg8000.DatabaseError as error:
            raise Exception(f"Erro ao inserir registro de ponto: {error}")

    def atualizar(self, registro_id, data=None, hora_entrada=None, hora_saida=None):
        """
        Atualiza um registro de ponto, mantendo valores existentes quando não especificados
        
        Args:
            registro_id: ID do registro a ser atualizado
            data: Nova data (opcional)
            hora_entrada: Nova hora de entrada (opcional)
            hora_saida: Nova hora de saída (opcional)
        """
        try:
            # Obtém dados atuais do registro
            self.db.cursor.execute("""
                SELECT data, hora_entrada, hora_saida
                FROM Registros_de_Ponto
                WHERE registro_id = %s
            """, (registro_id,))
            
            resultado = self.db.cursor.fetchone()
            if not resultado:
                raise ValueError(f"Registro com ID {registro_id} não encontrado")
                
            data_atual, entrada_atual, saida_atual = resultado
            
            # Usa valores atuais se novos não forem fornecidos
            data_final = data if data is not None else data_atual
            entrada_final = hora_entrada if hora_entrada is not None else entrada_atual
            saida_final = hora_saida if hora_saida is not None else saida_atual
            
            # Valida horários
            if not self._validar_horarios(entrada_final, saida_final):
                raise ValueError("Hora de saída deve ser posterior à hora de entrada")
            
            # Realiza a atualização
            self.db.cursor.execute("""
                UPDATE Registros_de_Ponto
                SET data = %s,
                    hora_entrada = %s,
                    hora_saida = %s,
                    data_atualizacao = CURRENT_TIMESTAMP
                WHERE registro_id = %s
            """, (data_final, entrada_final, saida_final, registro_id))
            
            if self.db.cursor.rowcount == 0:
                raise ValueError(f"Registro com ID {registro_id} não encontrado")
                
        except pg8000.DatabaseError as error:
            raise Exception(f"Erro ao atualizar registro de ponto: {error}")

    def _validar_horarios(self, hora_entrada, hora_saida):
        """Valida se a hora de saída é posterior à hora de entrada"""
        try:
            entrada = datetime.strptime(hora_entrada, "%H:%M:%S")
            saida = datetime.strptime(hora_saida, "%H:%M:%S")
            return saida > entrada
        except ValueError:
            return False

    def remover(self, registro_id):
        try:
            # Verifica se o registro existe
            self.db.cursor.execute("""
                SELECT registro_id FROM Registros_de_Ponto 
                WHERE registro_id = %s
            """, (registro_id,))
            
            if not self.db.cursor.fetchone():
                raise ValueError(f"Registro com ID {registro_id} não encontrado")
            
            # Remove o registro
            self.db.cursor.execute("""
                DELETE FROM Registros_de_Ponto 
                WHERE registro_id = %s
            """, (registro_id,))
            
        except pg8000.DatabaseError as error:
            raise Exception(f"Erro ao remover registro de ponto: {error}")

    def listar_todos(self):
        try:
            self.db.cursor.execute("""
                SELECT 
                    r.registro_id,
                    f.nome,
                    r.data::date,
                    r.hora_entrada::time,
                    r.hora_saida::time,
                    r.data_atualizacao
                FROM Registros_de_Ponto r
                JOIN Funcionarios f ON r.funcionario_id = f.funcionario_id
                ORDER BY r.data DESC, f.nome
            """)
            return self.db.cursor.fetchall()
        except pg8000.DatabaseError as error:
            raise Exception(f"Erro ao listar registros de ponto: {error}")

    def buscar_por_id(self, registro_id):
        try:
            self.db.cursor.execute("""
                SELECT 
                    r.registro_id,
                    r.funcionario_id,
                    f.nome,
                    r.data::date,
                    r.hora_entrada::time,
                    r.hora_saida::time,
                    r.data_atualizacao
                FROM Registros_de_Ponto r
                JOIN Funcionarios f ON r.funcionario_id = f.funcionario_id
                WHERE r.registro_id = %s
            """, (registro_id,))
            return self.db.cursor.fetchone()
        except pg8000.DatabaseError as error:
            raise Exception(f"Erro ao buscar registro de ponto: {error}")