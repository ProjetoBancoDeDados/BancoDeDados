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
- **Instale a biblioteca necessária** : pip install pg8000
- **Banco de dados**: PostgreSQL (ou equivalente que suporte o tipo `SERIAL` e integridade referencial).
- **Ambiente de Desenvolvimento**: Python 3.x com as seguintes bibliotecas instaladas:
  - `pg8000` (ou similar para conexão com o banco de dados PostgreSQL)
  - `datetime` (para manipulação de datas e horários)

## Como Executar o Projeto

1.
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




