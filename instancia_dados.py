import pyexcel

class instancia_dados:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.dados_arquivo = []
        
    def coleta_dados(self):
        with pyexcel.iget_workbook(file_name=self.nome_arquivo, format="ods") as workbook:
            sheet = workbook.active
            for row in sheet.rows():
                if row:
                    self.dados_arquivo.append(row)

    def get_dados_arquivo(self):
        return self.dados_arquivo