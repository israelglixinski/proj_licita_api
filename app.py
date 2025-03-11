from flask import Flask, jsonify
import db_mongo


app = Flask(__name__)

@app.route('/')
def home():
    return 'API Licitações'

@app.route('/lista_final')
def lista_final():
    return db_mongo.seleciona_registros_finais()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
