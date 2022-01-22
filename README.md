# condo-backend-fastapi
API developed in Python using FastAPI.

## Autor: 
Alonso Ehlert

## Linguagem de programação utilizada: 
* Python (Versão 3.8.10 64-bit) (Disponível em: https://www.python.org/downloads/release/python-3810/)

## Gerenciador de pacotes de instalação Python:
* pip (v.20.0.2 ou superior). (Disponível em: https://pip.pypa.io/en/stable/installation/)

## Arquitetura de referência mais utilizada: 
* Clean Architecture

## Framework web para construção da API:
* FastAPI (v.0.68.1) - Abrir um terminal e instalar via pip com o comando: `pip install fastapi`

## Banco de Dados utilizado: 
* SQLite 3 (v.3.31.1) (Referências de instalação em Linux: https://linuxhint.com/install-sqlite-ubuntu-linux-mint/)

## Aplicativo para visualizar o banco de dados SQLite
* DB Browser for SQLite 3.11.2 

## ORM utilizado para manipulação do Banco de Dados: 
* SQLAlchemy (v.1.4.29) - Abrir um terminal e instalar via pip com o comando: `pip install sqlalchemy`

## Ferramenta de migrações de banco de dados:
* Alembic (v.1.1.0) - Abrir um terminal e instalar via pip com o comando: `pip install alembic` 
* Observação: É necessário alterar o diretório contido no arquivo env.py (localizado em `condo-backend/alembic/`) 
para o diretório raiz onde o projeto está salvo na máquina. 

## Ferramenta para subir o servidor da aplicação:
* uvicorn (v.0.13.4) - Abrir um terminal e instalar via pip com o comando: `pip install uvicorn`


## Modelagem do banco de dados:
* A modelagem pode ser visualizada no diretório do projeto `condo-backend/src/infra/sqlalchemy/models` .
No arquivo `models.py` estão declaradas 3 classes distintas: `Unit` (que define as Unidades), 
`Tenant` (que define os inquilinos) e `UnitExpenses` (que define as despesas das unidades).

Foi criado um relacionamento com cardinalidade "n para n" entre as classes `Tenant` e `Unit`, o que 
gera uma tabela de associação (chamada de `association_table_1`).
Foi ainda criado um relacionamento com cardinalidade "1 para n" entre as classes `Unit` e `UnitExpenses`.

A modelagem dos relacionamentos entre classes no Banco de Dados seguiu a documentação do ORM 
SQLAlchemy, disponível em: https://docs.sqlalchemy.org/en/14/orm/relationships.html 

## Considerações adicionais:
* A camada `schemas` (`condo-backend/src/schemas`) é uma camada de abstração entre o usuário e os endpoints da aplicação.
* As camadas `models` (`condo-backend/src/infra/sqlalchemy/models`) e `repositories` (`condo-backend/src/infra/sqlalchemy/repositories`) estão diretamente ligadas ao banco de dados, sendo que os arquivos contidos na pasta `repositories` definem as operações CRUD (Create, Read, Update, Delete) a serem realizadas. 

# Instruções para executar a aplicação

* Instalar Python e todos os pacotes/ferramentas/framework/ORM mencionados no arquivo `requirements.txt`. A instalação pode ser feita via terminal, na pasta raiz do projeto, através do comando `pip install -r requirements.txt`. 
* Baixar e abrir o projeto em um editor de código fonte (VS Code, por exemplo).
* Em um terminal, navegar até a pasta raiz do projeto (por exemplo: `/home/user/Documentos/condo-backend`).
* Copiar e inserir o diretório da pasta raiz do projeto na linha 3 do arquivo `env.py`, que está contido na pasta `condo-backend/alembic` do projeto. Esta etapa será útil para o caso de futuras migrações relacionadas ao banco de dados.
* Ainda no mesmo terminal da pasta raiz do projeto, digitar o comando `uvicorn src.server:app --reload --reload-dir=src`.
* Após receber a mensagem "Application startup complete." no terminal, abra um browser qualquer e acesse 
http://localhost:8000/docs (Interface do usuário que corresponde à documentação da API).
* A interface possui 8 rotas implementadas e com suas funções descritas em inglês.

# Acessando rotas do projeto:

## 1 - Rota GET /tenants Get All Tenants
* Clique sobre esta rota e em seguida clique em `Try it out`.
* Em seguida clique em `Execute`. (Deverão aparecer cadastros de inquilinos que já estão cadastrados no banco de dados)

## 2 - Rota POST /tenants Create Tenants
* Clique sobre a rota e em seguida clique em `Try it out`.
* Em seguida, dentro do corpo de requisição (Request Body), digite valores para os atributos `name` (tipo string), `age` (tipo inteiro), `gender` (tipo string), `phone` (tipo inteiro) e `email` (tipo string). Todos os valores do tipo string devem ser
digitados entre aspas duplas.  
* Na sequência, clique em `Execute` e verifique se a resposta foi bem sucedida logo abaixo de `Execute`.
* Caso a resposta não seja bem-sucedida, é necessário analisar o tipo de erro cometido na digitação e retomar todos os 
passos para reexecutar esta rota. 

## 3 - Rota GET /units Get All Units
* Clique sobre a rota e em seguida clique em `Try it out`.
* Em seguida clique em `Execute`. (Deverão aparecer cadastros de unidades que já estão cadastradas no banco de dados)

## 4 - Rota POST /units Create Units
* Clique sobre a rota e em seguida clique em `Try it out`.
* Em seguida preenha o corpo de requisições com valores para cada um dos campos requeridos. 
Para esta rota todos os campos podem ser preenchidos com strings quaisquer (sempre entre aspas duplas.) 
* Na sequência, clique em `Execute` e verifique se a resposta foi bem sucedida logo abaixo de `Execute`.
* Caso a resposta não seja bem-sucedida, é necessário analisar o tipo de erro cometido na digitação e retomar todos os 
passos para reexecutar esta rota. 

## 5 - Rota POST /unitexpenses Create Unit Expense
* Clique sobre a rota e em seguida clique em `Try it out`.
* Em seguida preenha o corpo de requisições com valores para cada um dos campos requeridos. 
* Para esta rota, o valor do campo opcional "id" pode ter preenchido com um número inteiro (sem aspas), os valores dos campos 
"description", "type_expense" e "payment_status" devem ser preenchidos com string (entre aspas duplas), o valor do campo
"amount" deve ser preenchido com número do tipo float, o valor do campo "due_date" deve ser preenchido com um tipo datetime (entre
aspas duplas e conforme o exemplo pré-preenchido) e o valor do campo "unit_id" deve ser preenchido com um número inteiro (sem aspas).
* Na sequência, clique em `Execute` e verifique se a resposta foi bem sucedida logo abaixo de `Execute`.
* Caso a resposta não seja bem-sucedida, é necessário analisar o tipo de erro cometido na digitação e retomar todos os 
passos para reexecutar esta rota. 


## 6- Rota PUT /unitexpenses/{id} Edit Unit Expense
* Clique sobre a rota e em seguida clique em `Try it out`.
* Na sequência, digite um número inteiro escolhido para o parâmetro "id" afim de editar a despesa da unidade correspondente.
* Em seguida, edite os valores do corpo de requisição logo abaixo, seguindo exatamente os mesmos passos da rota POST anterior, com excessão do campo "id", que deve ser preenchido com um número inteiro.
* Por fim, clique em `Execute` e verifique se a resposta foi bem sucedida logo abaixo de `Execute`.
* Caso a resposta não seja bem-sucedida, é necessário analisar o tipo de erro cometido na digitação e retomar todos os 
passos para reexecutar esta rota. 

## 7 - Rota GET /unitexpenses/{unit_id} Expense per Unit
* Clique sobre a rota e em seguida clique em `Try it out`.
* Na sequência, digite um número inteiro escolhido para o parâmetro "unit_id" afim de visualizar uma despesa de uma determinada unidade. No banco de dados os valores 2, 5, 9 e 10 estão cadastrados e podem ser consultados. 
* Finalmente clique em `Execute` e verifique a resposta obtida.

## 8 - Rota GET /unitexpenses/overdue Get Overdue Expenses
* Clique sobre a rota e em seguida clique em `Try it out`.
* Na sequência clique em `Execute` para obter os resultados filtrados por `Overdue` no status de pagamento para visualizar despesas com fatura vencida.







