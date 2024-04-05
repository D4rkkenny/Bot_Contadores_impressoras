import shutil
import os
import Meses

class Organizar_arquivos:
    def __init__(self, item, caminho_impressora, mes, ano):
        self.item = item
        self.caminho_impressora = caminho_impressora
        self.mes = mes
        self.ano = ano
        self.caminho_pasta = "imagens_contadores"

    def organizando_arquivos(self):
        arquivos = os.listdir(self.caminho_pasta)
        try:
            for arquivo in arquivos:
                item_arquivo = arquivo.split(" ")
                if(item_arquivo[0] == self.item):
                    caminho_local = f"{self.caminho_pasta}\\{arquivo}".replace("\\\\", "\\")
                    caminho_destino =  f"{self.caminho_impressora}\\{self.ano}\\{self.mes} - {Meses.meses(self.mes)}".replace("\\\\", "\\")
                    shutil.copy(caminho_local, caminho_destino)
        except Exception as e:
            print(f"Impressora de item {self.item}: Erro Inesperado: {e}")