from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os


# Conexão com o Mongo
mongopass = os.getenv('MONGO_PASS')
if not mongopass:
    load_dotenv()
    mongopass = os.getenv('MONGO_PASS')
    if not mongopass:
        raise ValueError("A variável de ambiente 'MONGO_PASS' não está definida!")

client = MongoClient(f"mongodb+srv://israelglixinski:{mongopass}@cluster0.kzkzrs2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["licitacao"]
pncp_bruto = db["pncp_bruto"]
pncp_final = db["pncp_final"]


def seleciona_registros_finais():
    consulta = pncp_final.find()
    list_registros = []
    for registro in consulta:
        list_registros.append(registro)
        # print('\n')
        # print(registro)
        # print('\n')
    return list_registros


def atualizar_interesse(licitacao_id, novo_interesse):
    pncp_final.update_one({"id": licitacao_id}, {"$set": {"interesse": novo_interesse}})


if __name__ == "__main__":
    consulta = seleciona_registros_finais()
    for registro in consulta:
        print('\n')
        print(registro)
        print('\n')

    pass