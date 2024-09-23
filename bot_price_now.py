from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pathlib import Path
import os

import pandas as pd
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

from datetime import datetime
import time
 
def config_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=500,500', '--incognito','--headless'] #,'--headless'
    for argument in arguments:
        chrome_options.add_argument(argument)
        # inicializando o webdriver
    chrome_options.add_experimental_option('prefs', {
    # Desabilitar notificações
    'profile.default_content_setting_values.notifications': 2
    })
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def scrape_product_info(product):    
    try:
        sites = ['https://www.magazinevoce.com.br/magazineluizasitemega/busca/','https://lista.mercadolivre.com.br/']
        driver = config_driver()
        # Inicializa um DataFrame vazio
        df_produto = pd.DataFrame()
        for index, site in enumerate(sites):   
            
            if index == 0:
                #Magalu
                plataforma = "Magazine Luiza"
                path_url = product.split()
                path_url = "+".join(path_url)
                url = f"{site}{path_url}"
                driver.get(url)
                produto = driver.find_element(By.XPATH,'(//*[@class="sc-CCtys ddCamx"]/a)[1]/div[3]/h2').text 
                url_product = driver.find_element(By.XPATH,'(//*[@class="sc-CCtys ddCamx"]/a)[1]').get_attribute('href') 
                url_img = driver.find_element(By.XPATH,'(//*[@class="sc-CCtys ddCamx"]/a)[1]/div[2]/img').get_attribute('src') 
                valor = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/section[4]//p[contains(text(), 'R$') and not(@color='text.scratched')]").text  

            elif index ==1:
                #Mercado livre
                plataforma = "Mercado livre"
                path_url = produto.split()
                path_url = "-".join(path_url)
                url = f"{site}{path_url}"
                driver.get(url)
                time.sleep(1)
                produto = driver.find_element(By.XPATH,'(//li[contains(@class, "ui-search-layout__item")])[1]//div/div/div[2]//h2').text 
                url_product = driver.find_element(By.XPATH,'(//li[contains(@class, "ui-search-layout__item")])[1]/div/div/div[2]//a').get_attribute('href') 
                url_img = driver.find_element(By.XPATH,'(//li[contains(@class, "ui-search-layout__item")])[1]/div/div//img').get_attribute('src') 
                valor = driver.find_element(By.XPATH,'((//li[contains(@class, "ui-search-layout__item")])[1]//div//span/span[2])[1]').text

            # formatar valor
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            valor = valor.replace('R$ ', '').replace('.', '').replace(',', '.')
            valor = float(valor)
            
            #data e hora atuais
            data_hora_atual = datetime.now()
            # Formatar a data e hora
            data_hora_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")
            
            product_info = {
                'Produto': produto,
                'Valor': valor,
                'Plataforma': plataforma,
                'Data-hora_consulta': data_hora_formatada,            
                'Link_produto': url_product,
                'Url_img': url_img
            }
            if df_produto.empty:  # Se o DataFrame estiver vazio
                df_produto = pd.DataFrame([product_info])
            else:
                # Concatena o novo produto ao DataFrame existente
                df_produto = pd.concat([df_produto, pd.DataFrame([product_info])], ignore_index=True)
    except Exception as e:
        return f"Erro na busca dos dados: {e}"
    try: 
        driver.quit()
        # Ordenando pela coluna 'valor' do menor para o maior
        df_produto = df_produto.sort_values(by='Valor')
        file_path = export_excel_file(df_produto)
        product_inf = order_product(df_produto)
    except Exception as e:
        return f"Erro na busca dos dados: {e}"
    return product_inf,file_path

def export_excel_file(df_produto):
    try:
        #Definando pasta download
        home = str(Path.home())  
        downloads_path = os.path.join(home, 'Downloads')    
        #salvar um arquivo em xlsx
        file_name = "pesquisa_produto.xlsx"
        path_file = os.path.join(downloads_path, file_name)

        df_produto.to_excel(path_file, index=False)
        return path_file
    except Exception as e:
        return f"Erro na busca dos dados: {e}"
def order_product(df_produto):
    try:        
        idx_min = df_produto['Valor'].idxmin()
        df_filter = df_produto.loc[[idx_min]]

        produt_result = df_filter.iloc[0,0]
        Valor_result = df_filter.iloc[0,1]
        plataforma_result = df_filter.iloc[0,2]
        link_result = df_filter.iloc[0,4]
        valor_formatado = formatar_moeda(Valor_result)    

        return produt_result,valor_formatado,plataforma_result,link_result
    except Exception as e:
        return f"Erro na busca dos dados: {e}"
    
def formatar_moeda(Valor_result):
    return locale.currency(Valor_result, grouping=True)


