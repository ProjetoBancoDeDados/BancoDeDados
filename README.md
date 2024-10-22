Sistema de Controle de Ponto
Este projeto é um sistema de controle de ponto desenvolvido em Python, utilizando a biblioteca pg8000 para conexão com um banco de dados PostgreSQL. O sistema permite gerenciar funcionários e seus registros de ponto, incluindo funcionalidades para inserir, remover e atualizar registros, além de gerar relatórios.
Estrutura do Código
O código é organizado em uma classe chamada SistemaControlePonto, que contém métodos para realizar as operações principais do sistema. Abaixo estão os principais componentes:
Conexão com o Banco de Dados: O sistema se conecta a um banco de dados PostgreSQL usando as credenciais definidas nas variáveis da classe.
Menus: O sistema possui menus interativos para gerenciar funcionários e registros de ponto.
Relatórios: Gera relatórios sobre horas trabalhadas e registros de ponto.
Requisitos
Antes de instalar o sistema, você precisa ter o seguinte:
Python 3.x instalado.
PostgreSQL instalado e em execução.
Biblioteca pg8000 instalada. Você pode instalá-la usando o seguinte comando:

pip install pg8000

Instalação
Para Linux ou macOS
Clone o repositório (ou baixe o arquivo .py):

git clone <URL_DO_REPOSITORIO>
cd <DIRETORIO_DO_REPOSITORIO>

Instale a biblioteca necessária:

pip install pg8000

Configure o Banco de Dados:
Certifique-se de que o PostgreSQL está em execução.
Crie um banco de dados chamado ponto-db e configure um usuário com as credenciais especificadas no código (usuario: postgres, senha: root).
Execute o Código:

python nome_do_arquivo.py

Para Windows
Clone o repositório (ou baixe o arquivo .py):
bash
git clone <URL_DO_REPOSITORIO>
cd <DIRETORIO_DO_REPOSITORIO>

Instale a biblioteca necessária:

pip install pg8000

Configure o Banco de Dados:
Certifique-se de que o PostgreSQL está em execução.
Crie um banco de dados chamado postgres e configure um usuário com as credenciais especificadas no código (usuario: labdatabase, senha: labDatabase2022).
E execute os scripts do arquivo criar-tabelas.sql.

Execute o Código:

python3 interface_usuario.py

Uso
Após a instalação, você poderá interagir com o sistema através do terminal. As opções disponíveis incluem:
Inserir novos funcionários e registros de ponto.
Remover funcionários e registros.
Atualizar informações existentes.
Gerar relatórios sobre horas trabalhadas.







# Sistema de Controle de Ponto

Este projeto é um **Sistema de Controle de Ponto** que permite o gerenciamento de funcionários e seus registros de ponto. Ele inclui funcionalidades como cadastro de funcionários, registro de entrada e saída, remoção e atualização de informações, além da geração de relatórios.

## Funcionalidades

1. **Cadastro de Funcionários**:
   - Permite o cadastro de novos funcionários com nome, cargo e data de contratação.
   
2. **Registro de Ponto**:
   - Permite o registro da hora de entrada e saída de um funcionário em um determinado dia.

3. **Relatórios**:
   - Geração de relatórios que mostram as horas trabalhadas pelos funcionários.
   - Relatório que une as tabelas de funcionários e registros de ponto para exibir todas as entradas e saídas dos funcionários.

4. **Atualização de Dados**:
   - Atualiza informações dos funcionários ou registros de ponto.

5. **Remoção de Dados**:
   - Remove registros de funcionários (com seus registros de ponto automaticamente) ou remove apenas os registros de ponto.

## Estrutura do Banco de Dados

O projeto utiliza duas tabelas principais:

### Tabela: `Funcionarios`
| Coluna           | Tipo           | Descrição                                |
|------------------|----------------|------------------------------------------|
| `funcionario_id`  | `SERIAL`       | Identificador único do funcionário.      |
| `nome`           | `VARCHAR(255)` | Nome do funcionário.                     |
| `cargo`          | `VARCHAR(255)` | Cargo do funcionário.                    |
| `data_contratacao`| `DATE`         | Data de contratação do funcionário.      |

### Tabela: `Registros_de_Ponto`
| Coluna           | Tipo     | Descrição                                      |
|------------------|----------|------------------------------------------------|
| `registro_id`     | `SERIAL` | Identificador único do registro de ponto.      |
| `funcionario_id`  | `INTEGER`| Referência ao ID do funcionário.               |
| `data`            | `DATE`   | Data do registro de ponto.                     |
| `hora_entrada`    | `TIME`   | Hora de entrada do funcionário.                |
| `hora_saida`      | `TIME`   | Hora de saída do funcionário.                  |

### Relacionamento

- A tabela **Registros_de_Ponto** possui uma **chave estrangeira** que referencia a tabela **Funcionarios**.
- Caso um funcionário seja removido, todos os seus registros de ponto são excluídos automaticamente, garantindo a integridade referencial do banco de dados.

## Diagrama Relacional

O projeto segue o modelo de relacionamento 1:N, onde:

- **Um funcionário** pode ter **vários registros de ponto**.
- A tabela **Registros_de_Ponto** possui uma chave estrangeira que referencia a tabela **Funcionarios**.

## Requisitos para Execução

- **Banco de dados**: PostgreSQL (ou equivalente que suporte o tipo `SERIAL` e integridade referencial).
- **Ambiente de Desenvolvimento**: Python 3.x com as seguintes bibliotecas instaladas:
  - `psycopg2` (ou similar para conexão com o banco de dados PostgreSQL)
  - `sqlalchemy` (opcional, se preferir abstrair as consultas SQL)
  - `datetime` (para manipulação de datas e horários)

## Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
Crie as tabelas no seu banco de dados PostgreSQL:

sql
Copiar código
-- Criação da tabela Funcionarios
CREATE TABLE IF NOT EXISTS Funcionarios (
    funcionario_id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cargo VARCHAR(255) NOT NULL,
    data_contratacao DATE NOT NULL
);

-- Criação da tabela Registros_de_Ponto
CREATE TABLE IF NOT EXISTS Registros_de_Ponto (
    registro_id SERIAL PRIMARY KEY,
    funcionario_id INTEGER NOT NULL,
    data DATE NOT NULL,
    hora_entrada TIME,
    hora_saida TIME,
    FOREIGN KEY (funcionario_id) REFERENCES Funcionarios(funcionario_id) ON DELETE CASCADE
);
Execute o sistema para utilizar as funcionalidades de cadastro, registros e geração de relatórios.

Funcionalidades do Menu
Ao executar o sistema, você terá acesso às seguintes opções no menu:

Cadastrar Funcionário:

Insira o nome, cargo e data de contratação do funcionário.
Registrar Ponto:

Insira a data, hora de entrada e saída de um funcionário.
Atualizar Dados:

Atualize as informações de um funcionário ou de um registro de ponto.
Remover Registro:

Remova um funcionário (e seus registros de ponto) ou remova um registro de ponto específico.
Gerar Relatórios:

Relatório de horas trabalhadas por funcionário.
Relatório detalhado com todas as entradas e saídas de funcionários.
Relatórios
Relatório de Horas Trabalhadas por Funcionário
Este relatório calcula a diferença entre a hora de entrada e a hora de saída de cada funcionário e exibe o total de horas trabalhadas.

Relatório de Registros de Ponto
Este relatório exibe todos os registros de ponto dos funcionários com base no relacionamento entre as tabelas.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

Licença
Este projeto está licenciado sob a MIT License.

yaml
Copiar código

---

### Notas:
1. **GitHub Link**: Lembre-se de substituir o link do repositório no comando `git clone` pelo link real do seu projeto.
2. **Licença**: Se você desejar utilizar uma licença específica, lembre-se de alterar ou adicionar um arquivo `LICENSE` no repositório.
3. **Bibliotecas e Dependências**: Se você utilizar 




