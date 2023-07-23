from selenium import webdriver 
from selenium.webdriver.firefox.options import Options 
import time
 
# the target website 
url = "http://www.swisstargetprediction.ch/?" 
 
# the interface for turning on headless mode 
options = Options() 
options.add_argument("-headless") 
 
# using Firefox headless webdriver to secure connection to Firefox 
with webdriver.Firefox(options=options) as driver: 
	# opening the target website in the browser 
	driver.get(url) 
	com="document.forms[0].smiles.value='"
	smile="CCCCC/C=C/C=C/C(O)=NCC(C)C"
	mierda="'"
	driver.execute_script(com+smile+mierda)
	print(com+smile+mierda)
	driver.execute_script('document.getElementById("myForm").submit()')
	time.sleep(15)
	driver.execute_script('document.getElementsByClassName("buttons-csv")[0].click()')
