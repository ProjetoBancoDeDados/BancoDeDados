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
bash
pip install pg8000

Configure o Banco de Dados:
Certifique-se de que o PostgreSQL está em execução.
Crie um banco de dados chamado ponto-db e configure um usuário com as credenciais especificadas no código (usuario: postgres, senha: root).
Execute o Código:
bash
python nome_do_arquivo.py

Uso
Após a instalação, você poderá interagir com o sistema através do terminal. As opções disponíveis incluem:
Inserir novos funcionários e registros de ponto.
Remover funcionários e registros.
Atualizar informações existentes.
Gerar relatórios sobre horas trabalhadas.
Conclusão
Este sistema é uma solução prática para gerenciar registros de ponto em ambientes corporativos,
facilitando a administração do tempo dos funcionários e a geração de relatórios necessários para a gestão eficiente do trabalho.
