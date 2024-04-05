
import Coleta_contador 
import Abrir_json_impressoras as abrir_json
from datetime import datetime
from Organizar_arquivos_nas_pastas import Organizar_arquivos
impressoras_data = abrir_json.Abrir_json_impressoras()

mes_anterior = datetime.now().month - 1
ano_atual = datetime.now().year
for impressora_nome, impressora_info in impressoras_data.items():
    item = impressora_info.get("item")
    link = impressora_info.get("link")
    modelo = impressora_info.get("modelo")
    xpath = impressora_info.get("xpath")
    caminho = impressora_info.get("caminho")

    coletor = Coleta_contador.Coleta_contador(item, link, modelo, xpath)
    coletor.abrir_navegador()

    organizador = Organizar_arquivos(item, caminho, (datetime.now().month - 1), datetime.now().year)
    organizador.organizando_arquivos()