from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa a biblioteca para permitir requisições de diferentes origens (CORS)
import db_mongo  # Importa o módulo de banco de dados MongoDB
import json

# Inicializa a aplicação Flask
app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas da API

@app.route('/')
def home():
    """
    Rota principal da API.
    Retorna uma mensagem simples para indicar que a API está funcionando.
    """
    return 'API Licitações'

@app.route('/lista_final')
def lista_final():
    """
    Retorna a lista de registros finais da base de dados MongoDB.
    """
    consulta = db_mongo.seleciona_registros_finais()  # Consulta os registros finais no banco
    return app.response_class(
        response=json.dumps(consulta, ensure_ascii=False),  # Converte para JSON mantendo caracteres especiais
        mimetype='application/json'
    )

@app.route('/atualizar_interesse', methods=['POST'])
def atualizar_interesse():
    """
    Atualiza o campo 'interesse' de um registro no banco de dados com base no link fornecido.
    """
    try:
        data = request.json  # Obtém os dados enviados na requisição
        link = data.get("link")  # Obtém o link do registro
        interesse = data.get("interesse")  # Obtém o novo valor para 'interesse'

        if not link or interesse is None:
            return jsonify({"erro": "Campos 'link' e 'interesse' são obrigatórios"}), 400  # Retorna erro se campos estiverem ausentes

        db_mongo.atualizar_interesse(link, interesse)  # Atualiza o registro no banco
        return jsonify({"mensagem": "Interesse atualizado com sucesso!"}), 200  # Retorna sucesso
    except Exception as e:
        return jsonify({"erro": str(e)}), 500  # Retorna erro em caso de falha

@app.route('/atualizar_anotacao', methods=['POST'])
def atualizar_anotacao():
    """
    Atualiza o campo 'anotacao' de um registro no banco de dados com base no link fornecido.
    """
    try:
        data = request.json  # Obtém os dados da requisição
        link = data.get("link")  # Obtém o link do registro
        anotacao = data.get("anotacao")  # Obtém o novo valor para 'anotacao'

        if not link or anotacao is None:
            return jsonify({"erro": "Campos 'link' e 'anotacao' são obrigatórios"}), 400  # Retorna erro se campos estiverem ausentes

        db_mongo.atualizar_anotacao(link, anotacao)  # Atualiza o registro no banco
        return jsonify({"mensagem": "Anotação atualizada com sucesso!"}), 200  # Retorna sucesso
    except Exception as e:
        return jsonify({"erro": str(e)}), 500  # Retorna erro em caso de falha

if __name__ == '__main__':
    # Inicia o servidor Flask, tornando a API acessível em todas as interfaces na porta 5000
    app.run(host='0.0.0.0', port=5000)