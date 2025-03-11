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

    agora = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    filtro = {
        "dataEncerramentoProposta": { 
            "$gt": agora
        }
    }
    
    chaves_selecionadas = {
        "valorTotalEstimado"        : 1
        ,"dataEncerramentoProposta" : 1
        ,"objetoCompra"             : 1
        ,"link"                     : 1
        ,"interesse"                : 1
        ,"anotacao"                 : 1
        ,"_id"                      : 0 
    }
    

    total_registros = pncp_final.count_documents(filtro)
    consulta = pncp_final.find(filtro,chaves_selecionadas)

    list_registros = []
    for registro in consulta:
        list_registros.append(registro)

    return {"total_registros":total_registros,"list_registros":list_registros}


def atualizar_interesse(link, interesse):
    pncp_final.update_one({"link": link}, {"$set": {"interesse": interesse}})

def atualizar_anotacao(link, anotacao):
    pncp_final.update_one({"link": link}, {"$set": {"anotacao": anotacao}})


if __name__ == "__main__":
    consulta = seleciona_registros_finais()
    print(consulta)

    pass