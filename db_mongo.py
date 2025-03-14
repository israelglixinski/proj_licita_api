from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

# Obtém a senha do MongoDB a partir da variável de ambiente
mongopass = os.getenv('MONGO_PASS')
if not mongopass:
    load_dotenv()  # Carrega variáveis de ambiente do arquivo .env se não estiverem definidas
    mongopass = os.getenv('MONGO_PASS')
    if not mongopass:
        raise ValueError("A variável de ambiente 'MONGO_PASS' não está definida!")

# Configuração da conexão com o banco MongoDB
client = MongoClient(f"mongodb+srv://israelglixinski:{mongopass}@cluster0.kzkzrs2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Seleciona o banco de dados e coleções utilizadas

# Banco de dados
db = client["licitacao"]

# Coleções
pncp_bruto = db["pncp_bruto"]
pncp_final = db["pncp_final"]

def seleciona_registros_finais():
    """
    Seleciona registros finais do banco MongoDB que ainda não tiveram seu prazo de encerramento expirado.
    Retorna um dicionário contendo o total de registros e uma lista de registros filtrados.
    """
    agora = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')  # Obtém a data e hora atuais no formato correto
    
    filtro = {
        "dataEncerramentoProposta": {"$gt": agora}  # Filtra registros cujo prazo ainda não expirou
    }
    
    # Define os campos a serem retornados
    chaves_selecionadas = {
        "valorTotalEstimado"        : 1,
        "dataEncerramentoProposta"  : 1,
        "objetoCompra"              : 1,
        "link"                      : 1,
        "interesse"                 : 1,
        "anotacao"                  : 1,
        "_id"                       : 0  # Oculta o ID do MongoDB
    }
    
    # Conta o total de registros filtrados
    total_registros = pncp_final.count_documents(filtro)
    
    # Executa a consulta no banco MongoDB
    consulta = pncp_final.find(filtro, chaves_selecionadas)
    
    # Monta a lista de registros retornados
    list_registros = [registro for registro in consulta]
    
    return {"total_registros": total_registros, "list_registros": list_registros}

def atualizar_interesse(link, interesse):
    """
    Atualiza o campo 'interesse' de um registro identificado pelo link.
    """
    pncp_final.update_one({"link": link}, {"$set": {"interesse": interesse}})

def atualizar_anotacao(link, anotacao):
    """
    Atualiza o campo 'anotacao' de um registro identificado pelo link.
    """
    pncp_final.update_one({"link": link}, {"$set": {"anotacao": anotacao}})

if __name__ == "__main__":
    # Executa a função para listar registros finais ao rodar o script
    consulta = seleciona_registros_finais()
    print(consulta)
