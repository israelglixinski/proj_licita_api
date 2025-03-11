from flask import Flask, jsonify, request
import db_mongo
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'API Licitações'

@app.route('/lista_final')
def lista_final():
    consulta = db_mongo.seleciona_registros_finais() 
    return app.response_class(
        response=json.dumps(consulta, ensure_ascii=False),
        mimetype='application/json'
    )

@app.route('/atualizar_interesse', methods=['POST'])
def atualizar_interesse():
    """ Atualiza o campo 'interesse' de um registro com base no link """
    try:
        data = request.json
        link = data.get("link")
        interesse = data.get("interesse")

        if not link or interesse is None:
            return jsonify({"erro": "Campos 'link' e 'interesse' são obrigatórios"}), 400

        db_mongo.atualizar_interesse(link, interesse)
        return jsonify({"mensagem": "Interesse atualizado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/atualizar_anotacao', methods=['POST'])
def atualizar_anotacao():
    """ Atualiza o campo 'anotacao' de um registro com base no link """
    try:
        data = request.json
        link = data.get("link")
        anotacao = data.get("anotacao")

        if not link or anotacao is None:
            return jsonify({"erro": "Campos 'link' e 'anotacao' são obrigatórios"}), 400

        db_mongo.atualizar_anotacao(link, anotacao)
        return jsonify({"mensagem": "Anotação atualizada com sucesso!"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

