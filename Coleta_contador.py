from playwright.sync_api import sync_playwright
import time
import mapeamento_de_clique_impressora as mapeamento

class Coleta_contador:
    def __init__(self, item, link, modelo, xpath):
        self.item = item
        self.link = link
        self.modelo = modelo
        self.xpath = xpath

    def abrir_navegador(self):
        contador = 0
        with sync_playwright() as p:
            try:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context(ignore_https_errors=True)
                page = context.new_page()
                try:
                    page.set_default_navigation_timeout(10000)
                    page.goto(self.link)
                    time.sleep(5)
                except (TimeoutError) as e:
                    print(f"Erro: A impressora de item {self.item} ocorreu erro {e}") 

                contador = mapeamento.clique_impressora(self.modelo, page, self.xpath)
                nome_do_arquivo = ""
                ip_impressora = self.link.split("/")
                nome_do_arquivo = f"{self.item} - {ip_impressora[2]} - {contador}"
                page.screenshot(path=(r"imagens_contadores\\" + nome_do_arquivo + ".png")) 
                browser.close() 
            except Exception as e:
                print(f"Erro: Impressora de Item {self.item} teve um erro inesperado:  {e}")
        return contador
