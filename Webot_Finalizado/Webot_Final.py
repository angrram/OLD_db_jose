from selenium import webdriver 
from selenium.webdriver.firefox.options import Options 
import time
 
# the target website 
url = "http://www.swisstargetprediction.ch/?" 
 
 # the interface for turning on headless mode 
options = Options() 
options.add_argument("-headless") 

def entresacar(nombre_archivo="Resultados_Bot.txt"):
    # Lista para almacenar los SMILES extraídos
    smiles_extraidos = []

    # Abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Leer el contenido del archivo línea por línea
        for linea in archivo:
            # Extraer los SMILES después de los primeros 11 caracteres y agregarlos a la lista
            smile = linea[11:].strip()
            print("Copié el SMILES con exito!" + "\n")
            #chanchada(smile)
            with webdriver.Firefox(options=options) as driver:
                driver.get(url)
                com="document.forms[0].smiles.value='"
                caracter="'"
                driver.execute_script(com+smile+caracter)
                print(com+smile+caracter + "\n")
                driver.execute_script('document.getElementById("myForm").submit()')
                time.sleep(18)
                driver.execute_script('document.getElementsByClassName("buttons-csv")[0].click()')

            print(smile)
            print(" Este SMILE fue introducido " + "\n")
            smiles_extraidos.append(smile)

    # Retornar la lista de SMILES extraídos
    #return smiles_extraidos

# Llamar a la función entresacar() para obtener la lista de SMILES
entresacar()
print("Proceso terminado con exito! :)")
