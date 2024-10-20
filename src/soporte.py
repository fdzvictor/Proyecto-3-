
# Importamos las librerías que necesitamos

# Librerías de extracción de datos
# -----------------------------------------------------------------------

# Importaciones:
# Beautifulsoup
from bs4 import BeautifulSoup

# Requests
import requests

# Importar librerías para automatización de navegadores web con Selenium
# -----------------------------------------------------------------------
from selenium import webdriver  # Selenium es una herramienta para automatizar la interacción con navegadores web.
from webdriver_manager.chrome import ChromeDriverManager  # ChromeDriverManager gestiona la instalación del controlador de Chrome.
from selenium.webdriver.common.keys import Keys  # Keys es útil para simular eventos de teclado en Selenium.
from selenium.webdriver.support.ui import Select  # Select se utiliza para interactuar con elementos <select> en páginas web.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException # Excepciones comunes de selenium que nos podemos encontrar 


# Importar librerías para pausar la ejecución
# -----------------------------------------------------------------------
from time import sleep  # Sleep se utiliza para pausar la ejecución del programa por un número de segundos.


def sacar_info_h2(url):
        res_url = requests.get(url)

    # Verifica el código de estado
        print(res_url.status_code)

    # Si el código de estado es 200, procesa la respuesta
        if res_url.status_code == 200:
            sopa_actividades = BeautifulSoup(res_url.content, "html.parser")
            lista_actividades = sopa_actividades.findAll("h2")
            activ = []
            for actividad in lista_actividades:
                activ.append(actividad.getText(strip=True))

        else:
            print("Error al acceder a la página")

        return activ

def sacar_info(url, que_buscar):
    

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'es',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://www.getyourguide.es/'
 }

    res_url = requests.get(url, headers=headers)

    # Verifica el código de estado
    print(res_url.status_code)

    # Si el código de estado es 200, procesa la respuesta
    if res_url.status_code == 200:
        sopa_actividades = BeautifulSoup(res_url.content, "html.parser")
        lista_actividades = sopa_actividades.findAll(que_buscar)
        activ = []
        for actividad in lista_actividades:
            activ.append(actividad.getText(strip=True))

        print(activ)
    else:
        print("Error al acceder a la página")