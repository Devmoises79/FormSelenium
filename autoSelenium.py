from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

# Caminho absoluto do arquivo HTML
caminho_html = os.path.abspath("form.html")
url = "file://" + caminho_html

# Inicializa o navegador (Chrome)
service = Service()
driver = webdriver.Chrome(service=service)

try:
    driver.get(url)
    time.sleep(1)

    # Preenche os campos
    driver.find_element(By.ID, "nome").send_keys("Beltrano da Silva")
    driver.find_element(By.ID, "email").send_keys("beltrano@gmail.com")
    driver.find_element(By.ID, "mensagem").send_keys("Gostei do formulário!")

    time.sleep(2)

    # Envia o formulário
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)
finally:
    driver.quit()


print("Formulário enviado com sucesso!")