import time
def clique_impressora(modelo_impressora, page, xpath):
    contador = 0
    if modelo_impressora in ["SP3510", "SP3710", "SP310", "SP377","M320", "SP5200", "M5360"]:
        contador = int(page.query_selector(xpath).inner_text())
    elif modelo_impressora == "M4070":
        page.click("xpath=/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button")
        time.sleep(5)
        page.click("xpath=/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/ul/div/li/ul/li[3]/div/a")
        time.sleep(5)
        contador = int(page.query_selector(xpath).inner_text())
    elif modelo_impressora == "MPC2003":
        #preto 
        contador_preto = (int(page.query_selector("xpath=/html/body/table/tbody/tr/td[3]/table[3]/tbody/tr/td[2]/table[3]/tbody/tr[1]/td[4]").inner_text()) +
                            int(page.query_selector("xpath=/html/body/table/tbody/tr/td[3]/table[3]/tbody/tr/td[2]/table[5]/tbody/tr[1]/td[4]").inner_text()))
        #colorido
        contador_colorido = (int(page.query_selector("xpath=/html/body/table/tbody/tr/td[3]/table[3]/tbody/tr/td[2]/table[3]/tbody/tr[2]/td[4]").inner_text()) +
                            int(page.query_selector("xpath=/html/body/table/tbody/tr/td[3]/table[3]/tbody/tr/td[2]/table[3]/tbody/tr[3]/td[4]").inner_text()) +
                            int(page.query_selector("xpath=/html/body/table/tbody/tr/td[3]/table[3]/tbody/tr/td[2]/table[3]/tbody/tr[4]/td[4]").inner_text()) + 
                            int(page.query_selector("xpath=/html/body/table/tbody/tr/td[3]/table[3]/tbody/tr/td[2]/table[5]/tbody/tr[2]/td[4]").inner_text()) + 
                            int(page.query_selector("xpath=/html/body/table/tbody/tr/td[3]/table[3]/tbody/tr/td[2]/table[5]/tbody/tr[3]/td[4]").inner_text()) + 
                            int(page.query_selector("xpath=/html/body/table/tbody/tr/td[3]/table[3]/tbody/tr/td[2]/table[5]/tbody/tr[4]/td[4]").inner_text())) 
        contadores = [contador_preto, contador_colorido]
        return contadores #retorna uma lista com os contadores b/w e colorido
    elif modelo_impressora == "HP_MFP432":
        time.sleep(10)
        page.click("xpath=/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[4]/div/div/div/table/tbody/tr/td[3]/table/tbody/tr/td[2]/em/button")
        time.sleep(10)
        page.click("xpath=/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/ul/div/li/ul/li[3]/div/a/span")
        time.sleep(3)
        contador = int(page.query_selector(xpath).inner_text())

    
    return contador