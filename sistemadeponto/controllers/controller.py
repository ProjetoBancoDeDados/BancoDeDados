from datetime import datetime
from utils.interface import Interface
from models.registro_ponto import RegistroPonto
from reports.relatorios import Relatorios
from models.funcionario import Funcionario
class SistemaController:
    def __init__(self, db_connection):
        self.db = db_connection
        self.interface = Interface()
        self.funcionario = Funcionario(db_connection)
        self.registro_ponto = RegistroPonto(db_connection)
        self.relatorios = Relatorios(db_connection)

    def executar(self):
        Interface.exibir_splash_screen(self.db)
        self.interface.exibir_splash_screen(self.db)
        self.exibir_menu_principal()

    def exibir_menu_principal(self):
        while True:
            Interface.limpar_tela()
            print("\n=== Menu Principal ===")
            print("1. Relatórios")
            print("2. Inserir Registros")
            print("3. Remover Registros")
            print("4. Atualizar Registros")
            print("5. Sair")
            
            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                self.menu_relatorios()
            elif opcao == '2':
                self.menu_inserir_registros()
            elif opcao == '3':
                self.menu_remover_registros()
            elif opcao == '4':
                self.menu_atualizar_registros()
            elif opcao == '5':
                print("\nSaindo do sistema...")
                break
            else:
                input("\nOpção inválida! Pressione Enter para continuar...")

    def menu_relatorios(self):
        while True:
            Interface.limpar_tela()
            print("\n=== Menu de Relatórios ===")
            print("1. Relatório de Horas Trabalhadas por Funcionário")
            print("2. Relatório de Registros de Ponto")
            print("3. Voltar ao Menu Principal")
            
            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                self.exibir_relatorio_horas_trabalhadas()
            elif opcao == '2':
                self.exibir_relatorio_registros_ponto()
            elif opcao == '3':
                break
            else:
                input("\nOpção inválida! Pressione Enter para continuar...")

    def exibir_relatorio_horas_trabalhadas(self):
        try:
            resultados = self.relatorios.horas_trabalhadas()
            
            Interface.limpar_tela()
            print("\n=== Relatório de Horas Trabalhadas por Funcionário ===\n")
            
            if not resultados:
                print("Nenhum registro encontrado.")
            else:
                print(f"{'ID':^5} | {'Nome':<30} | {'Total Registros':^15} | {'Horas Trabalhadas':^20}")
                print("-" * 75)
                for linha in resultados:
                    print(f"{linha[0]:^5} | {linha[1]:<30} | {linha[2]:^15} | {linha[3]:^20.2f}")
        except Exception as error:
            print(f"\nErro ao gerar relatório: {error}")
        finally:
            input("\nPressione Enter para continuar...")

    def exibir_relatorio_registros_ponto(self):
        try:
            resultados = self.relatorios.registros_ponto()
            
            Interface.limpar_tela()
            print("\n=== Relatório de Registros de Ponto ===\n")
            
            if not resultados:
                print("Nenhum registro encontrado.")
            else:
                print(f"{'ID':^5} | {'Nome':<30} | {'Data':^12} | {'Entrada':^8} | {'Saída':^8} | {'Horas':^8}")
                print("-" * 80)
                for linha in resultados:
                    print(f"{linha[0]:^5} | {linha[1]:<30} | {linha[2]} | {linha[3]} | {linha[4]} | {linha[5]:^8.2f}")
        except Exception as error:
            print(f"\nErro ao gerar relatório: {error}")
        finally:
            input("\nPressione Enter para continuar...")

    def menu_inserir_registros(self):
        while True:
            Interface.limpar_tela()
            print("\n=== Inserir Registros ===")
            print("1. Inserir Funcionário")
            print("2. Inserir Registro de Ponto")
            print("3. Voltar ao Menu Principal")
            
            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                self.inserir_funcionario()
            elif opcao == '2':
                self.inserir_registro_ponto()
            elif opcao == '3':
                break
            else:
                input("\nOpção inválida! Pressione Enter para continuar...")

    def inserir_funcionario(self):
        Interface.limpar_tela()
        print("\n=== Inserir Novo Funcionário ===")

        try:
            nome = input("\nNome do funcionário: ")
            cargo = input("Cargo: ")
            
            ano = input("Ano de contratação (AAAA): ")
            mes = input("Mês de contratação (MM): ")
            dia = input("Dia de contratação (DD): ")
            
            if not nome or not cargo or not ano or not mes or not dia:
                print("\nTodos os campos são obrigatórios!")
                return

            try:
                data_contratacao = datetime.strptime(f"{ano}-{mes}-{dia}", "%Y-%m-%d").date()
            except ValueError:
                print("\nData inválida! Verifique os valores informados.")
                return

            novo_id = self.funcionario.inserir(nome, cargo, data_contratacao)
            print(f"\nFuncionário inserido com sucesso! ID: {novo_id}")

        except Exception as error:
            print(f"\nErro ao inserir funcionário: {error}")
        finally:
            input("\nPressione Enter para continuar...")

    def inserir_registro_ponto(self):
        Interface.limpar_tela()
        print("\n=== Inserir Registro de Ponto ===")

        try:
            funcionarios = self.funcionario.listar_todos()

            if not funcionarios:
                print("\nNão há funcionários cadastrados!")
                return

            print("\nFuncionários disponíveis:")
            for func in funcionarios:
                print(f"ID: {func[0]} - Nome: {func[1]}")

            funcionario_id = input("\nID do funcionário: ")

            data = self._obter_data_valida("Data do registro")
            if not data:
                return

            hora_entrada = self._obter_horario_valido("entrada")
            if not hora_entrada:
                return

            hora_saida = self._obter_horario_valido("saída")
            if not hora_saida:
                return

            novo_id = self.registro_ponto.inserir(funcionario_id, data, hora_entrada, hora_saida)
            print(f"\nRegistro de ponto inserido com sucesso! ID: {novo_id}")

        except Exception as error:
            print(f"\nErro ao inserir registro de ponto: {error}")
        finally:
            input("\nPressione Enter para continuar...")

    def _obter_data_valida(self, descricao):
        dia = input(f"Dia do {descricao} (DD): ")
        mes = input(f"Mês do {descricao} (MM): ")
        ano = input(f"Ano do {descricao} (AAAA): ")
        
        try:
            return datetime.strptime(f"{ano}-{mes}-{dia}", "%Y-%m-%d").date()
        except ValueError:
            print("\nData inválida! Verifique o formato e tente novamente.")
            return None

    def _obter_horario_valido(self, tipo):
       hora = input(f"Hora de {tipo} (HH): ")
       minuto = input(f"Minuto de {tipo} (MM): ")
        
       try:
           horario = f"{hora}:{minuto}:00"
           datetime.strptime(horario, "%H:%M:%S")
           return horario
       except ValueError:
           print("\nHorário inválido! Verifique o formato e tente novamente.")
           return None

    def menu_remover_registros(self):
       while True:
           Interface.limpar_tela()
           print("\n=== Remover Registros ===")
           print("1. Remover Funcionário")
           print("2. Remover Registro de Ponto")
           print("3. Voltar ao Menu Principal")
           
           opcao = input("\nEscolha uma opção: ")

           if opcao == '1':
               self.remover_funcionario()
           elif opcao == '2':
               self.remover_registro_ponto()
           elif opcao == '3':
               break
           else:
               input("\nOpção inválida! Pressione Enter para continuar...")

    def remover_funcionario(self):
       Interface.limpar_tela()
       print("\n=== Remover Funcionário ===")

       try:
           funcionarios = self.funcionario.listar_todos()

           if not funcionarios:
               print("\nNão há funcionários cadastrados!")
               return

           print("\nFuncionários disponíveis:")
           for func in funcionarios:
               print(f"ID: {func[0]} - Nome: {func[1]}")

           funcionario_id = input("\nID do funcionário a ser removido: ")
           
           confirma = input("Confirma a remoção do funcionário? (S/N): ").upper()
           if confirma == 'S':
               self.funcionario.remover(funcionario_id)
               print("\nFuncionário removido com sucesso!")
           else:
               print("\nOperação cancelada!")

       except Exception as error:
           print(f"\nErro ao remover funcionário: {error}")
       finally:
           input("\nPressione Enter para continuar...")

    def remover_registro_ponto(self):
       Interface.limpar_tela()
       print("\n=== Remover Registro de Ponto ===")

       try:
           registros = self.registro_ponto.listar_todos()

           if not registros:
               print("\nNão há registros de ponto cadastrados!")
               return

           print("\nRegistros disponíveis:")
           for registro in registros:
               print(f"ID: {registro[0]} - Funcionário: {registro[1]} - Data: {registro[2]}")

           registro_id = input("\nID do registro a ser removido: ")
           
           confirma = input("Confirma a remoção do registro? (S/N): ").upper()
           if confirma == 'S':
               self.registro_ponto.remover(registro_id)
               print("\nRegistro removido com sucesso!")
           else:
               print("\nOperação cancelada!")

       except Exception as error:
           print(f"\nErro ao remover registro de ponto: {error}")
       finally:
           input("\nPressione Enter para continuar...")

    def menu_atualizar_registros(self):
       while True:
           Interface.limpar_tela()
           print("\n=== Atualizar Registros ===")
           print("1. Atualizar Funcionário")
           print("2. Atualizar Registro de Ponto")
           print("3. Voltar ao Menu Principal")
           
           opcao = input("\nEscolha uma opção: ")

           if opcao == '1':
               self.atualizar_funcionario()
           elif opcao == '2':
               self.atualizar_registro_ponto()
           elif opcao == '3':
               break
           else:
               input("\nOpção inválida! Pressione Enter para continuar...")

    def atualizar_funcionario(self):
       Interface.limpar_tela()
       print("\n=== Atualizar Funcionário ===")

       try:
          funcionarios = self.funcionario.listar_todos()

          if not funcionarios:
              print("\nNão há funcionários cadastrados!")
              return

          print("\nFuncionários disponíveis:")
          for func in funcionarios:
              print(f"ID: {func[0]} - Nome: {func[1]}")

          funcionario_id = input("\nID do funcionário a ser atualizado: ")
          
          # Novos dados
          nome = input("Novo nome (deixe em branco para manter o atual): ").strip()
          cargo = input("Novo cargo (deixe em branco para manter o atual): ").strip()

          # Verifica se pelo menos um campo foi preenchido
          if not nome and not cargo:
              print("\nNenhum dado foi alterado!")
              return
              
          # Se um campo estiver vazio, mantém o valor atual
          self.funcionario.atualizar(
              funcionario_id=funcionario_id,
              nome=nome if nome else None,
              cargo=cargo if cargo else None
          )
          print("\nFuncionário atualizado com sucesso!")

       except Exception as error:
          print(f"\nErro ao atualizar funcionário: {error}")
       finally:
          input("\nPressione Enter para continuar...")

    def atualizar_registro_ponto(self):
      Interface.limpar_tela()
      print("\n=== Atualizar Registro de Ponto ===")

      try:
          registros = self.registro_ponto.listar_todos()

          if not registros:
              print("\nNão há registros de ponto cadastrados!")
              return

          print("\nRegistros disponíveis:")
          for registro in registros:
              print(f"ID: {registro[0]} - Funcionário: {registro[1]} - Data: {registro[2]} - "
                    f"Entrada: {registro[3]} - Saída: {registro[4]}")

          registro_id = input("\nID do registro a ser atualizado: ")
          
          # Novos dados
          nova_data = self._obter_data_valida("registro (deixe em branco para manter a atual)")
          nova_entrada = self._obter_horario_valido("entrada (deixe em branco para manter a atual)")
          nova_saida = self._obter_horario_valido("saída (deixe em branco para manter a atual)")

          # Atualiza o registro mantendo valores existentes quando não houver alteração
          self.registro_ponto.atualizar(
              registro_id=registro_id,
              data=nova_data,
              hora_entrada=nova_entrada,
              hora_saida=nova_saida
          )
          if nova_data or nova_entrada or nova_saida is not None :
              # Se algum dado foi alterado
             print ("\Registro atualizado com sucesso!")

      except Exception as error :
         # Mensagem amigável em caso de erro 
         mensagem_erro= _formatar_mensagem_erro(error)
         # Exibe mensagem 
         print(mensagem_erro)

      finally :
          input ("\Pressione Enter para continuar...") 

def _validar_horarios(self, hora_entrada, hora_saida):
   """Método auxiliar para validar a consistência entre horários de entrada e saída"""
   if not hora_entrada or not hora_saida :
      return True
      
   try :
      entrada= datetime.strptime(hora_entrada,"%H:%M:%S") 
      saida= datetime.strptime(hora_saida,"%H:%M:%S") 
      return saida > entrada 
   except ValueError :
      return False 

def _formatar_mensagem_erro(self, erro) :
   """Método auxiliar para formatar mensagens de erro de forma amigável"""
   if "foreign key" in str(erro).lower() :
      return "Registro relacionado não encontrado. Verifique os IDs informados."
   elif "not null" in str(erro).lower() :
      return "Todos os campos obrigatórios devem ser preenchidos."
   else :
      return str(erro)