from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time

# Inicia el navegador
driver = webdriver.Chrome()

try:
    # Abre la página local
    driver.get('localhost:8000')

    # Espera un momento para asegurarte de que la página ha cargado completamente
    time.sleep(2)

    # Ejecuta el JavaScript para hacer scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Espera un momento para ver el resultado
    time.sleep(5)

except WebDriverException as e:
    print(f"Se produjo un error al intentar cargar la página: {e}")

finally:
    # Cierra el navegador
    driver.quit()
