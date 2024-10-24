# reports/relatorios.py
import pg8000


class Relatorios:
    def __init__(self, db_connection):
        self.db = db_connection

    def horas_trabalhadas(self):
        try:
            self.db.cursor.execute("""
                SELECT 
                    f.funcionario_id,
                    f.nome,
                    COUNT(r.registro_id) AS total_registros,
                    COALESCE(SUM(
                        EXTRACT(EPOCH FROM (r.hora_saida - r.hora_entrada))/3600
                    ), 0) AS horas_trabalhadas
                FROM Funcionarios f
                LEFT JOIN Registros_de_Ponto r ON f.funcionario_id = r.funcionario_id
                GROUP BY f.funcionario_id, f.nome
                ORDER BY f.nome
            """)
            return self.db.cursor.fetchall()
        except pg8000.DatabaseError as error:
            raise Exception(f"Erro ao gerar relatório de horas trabalhadas: {error}")

    def registros_ponto(self):
        try:
            self.db.cursor.execute("""
                SELECT 
                    f.funcionario_id,
                    f.nome,
                    r.data::date,
                    r.hora_entrada,
                    r.hora_saida,
                    EXTRACT(EPOCH FROM (r.hora_saida - r.hora_entrada))/3600 AS horas_trabalhadas
                FROM Funcionarios f
                JOIN Registros_de_Ponto r ON f.funcionario_id = r.funcionario_id
                ORDER BY r.data DESC, f.nome
            """)
            return self.db.cursor.fetchall()
        except pg8000.DatabaseError as error:
            raise Exception(f"Erro ao gerar relatório de registros de ponto: {error}")
