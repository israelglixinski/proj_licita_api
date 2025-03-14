# proj_licita_api

## Descrição
O **proj_licita_api** é uma API desenvolvida em **Flask** para fornecer acesso a informações sobre licitações extraídas do **Portal Nacional de Contratações Públicas (PNCP)** e armazenadas em um banco de dados **MongoDB**.

## Objetivo
O objetivo principal deste projeto é disponibilizar endpoints que permitam a consulta e atualização de registros de licitações, facilitando o acesso e a análise dos dados.

## Funcionalidades
- **Listar licitações filtradas**
- **Atualizar interesse em uma licitação**
- **Atualizar anotações sobre uma licitação**

## Estrutura do Projeto
O projeto contém os seguintes arquivos principais:

### `app.py`
Arquivo principal da API, desenvolvido com **Flask**. Contém os seguintes endpoints:
- **`/`** → Retorna uma mensagem indicando que a API está ativa.
- **`/lista_final`** → Retorna os registros filtrados das licitações armazenadas no banco de dados.
- **`/atualizar_interesse`** (POST) → Atualiza o campo `interesse` de um registro com base no link.
- **`/atualizar_anotacao`** (POST) → Atualiza o campo `anotacao` de um registro com base no link.

### `db_mongo.py`
Arquivo responsável pela conexão com o banco **MongoDB** e manipulação dos registros. Contém funções para:
- Consultar registros finais filtrados.
- Atualizar o campo `interesse`.
- Atualizar o campo `anotacao`.

### `Procfile`
Arquivo de configuração para deploy em plataformas como o **Heroku**, especificando o comando para iniciar a API.

## Requisitos
Para utilizar o projeto, é necessário ter instalado:
- **Python 3.8+**
- **MongoDB** (local ou MongoDB Atlas)
- Pacotes Python:
  - `flask`
  - `flask-cors`
  - `pymongo`
  - `python-dotenv`

## Configuração
1. Criar um arquivo `.env` na raiz do projeto e adicionar a variável `MONGO_PASS` com a senha do banco:
   ```ini
   MONGO_PASS=sua_senha_aqui
   ```
2. Modificar o código no arquivo `db_mongo.py` para apontar para o seu banco **MongoDB**, caso utilize um servidor diferente.

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute a API:
   ```bash
   python app.py
   ```
3. Acesse os endpoints via **Postman** ou navegador:
   - `http://localhost:5000/`
   - `http://localhost:5000/lista_final`

## Contribuição
Caso queira utilizar este projeto para seu próprio propósito, basta modificar as variáveis necessárias para apontar para seu banco **MongoDB**.

Sugestões e melhorias são bem-vindas!
