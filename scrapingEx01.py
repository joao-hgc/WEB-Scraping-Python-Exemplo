from bs4 import BeautifulSoup
import requests

#Pagina URL
html = requests.get("https://www.tempo.com/ourinhos.htm").content

#Cria um BeautifulSoupObjeto e o atribui à SOUPvariavel com 2 argumentos 1º HTML analisado 2º String "html.parse" representao analisadorinterno doPython
soup = BeautifulSoup(html, "html.parser")

#Procura dentro do Objeto beautifulsoup valor atribuido ao elemento passando os parametros tag HTML ex: 'span' e a 'class'ou 'id' da tag 

cidade = soup.find('h1', class_='titulo').string
temperatura = soup.find('span', class_='dato-temperatura changeUnitT').string
vento_minino = soup.find('span', data="21|1").string
vento_maximo = soup.find('span', data="45|0").string
sensacao = soup.find('span', class_="sensacion changeUnitT").string

print("{} é de: {} e ventos de {}-{}".format(cidade,temperatura,vento_minino,vento_maximo))