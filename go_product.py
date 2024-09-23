from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

import time
 
def config_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=500,500', '--incognito'] #,'--headless'
    for argument in arguments:
        chrome_options.add_argument(argument)
        # inicializando o webdriver
    chrome_options.add_experimental_option('prefs', {
    # Desabilitar notificações
    'profile.default_content_setting_values.notifications': 2
    })
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def go_product(link):    
    try:
        driver = config_driver()
        driver.maximize_window()
        driver.get(link)
        time.sleep(240) 
    except Exception as e:
        return f"Erro na busca dos dados: {e}"
    
def formatar_moeda(Valor_result):
    return locale.currency(Valor_result, grouping=True)


