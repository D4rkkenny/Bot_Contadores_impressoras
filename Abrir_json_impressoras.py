import json
import os
caminho_arquivo = r"Json\\impressoras.json"

def Abrir_json_impressoras():
    try:
        diretorio_atual = os.path.dirname(__file__)
        caminho_completo = os.path.join(diretorio_atual, caminho_arquivo)
        with open(caminho_completo , 'r', encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados.get("impressoras")
    except(FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao ler o arquivo Json: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise