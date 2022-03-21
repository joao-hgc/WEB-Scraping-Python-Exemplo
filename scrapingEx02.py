from bs4 import BeautifulSoup
from urllib.request import urlopen

#Pagina URL
url = "https://super.abril.com.br/mundo-estranho/quais-sa%CC%83o-os-principais-deuses-egipcios/"
#Abre URL
page = urlopen(url)
#Extrai a pagina e retorna uma sequencia de bytes
html_bytes = page.read()
#Decodifica os bytes para uma string usando ("utf-8")
html = html_bytes.decode("utf-8")
#Cria um BeautifulSoupObjeto e o atribui à SOUPvariavel com 2 argumentos 1º HTML analisado 2º String "html.parse" representao analisadorinterno doPython
soup = BeautifulSoup(html, "html.parser")
#Exibe conteudo HTML pagina
print(html)

#Exibe tag <title> conteudo </title> 
print(soup.title)

#Exibe somente texto sem tag da pagina
print(soup.get_text())

#Exibe em forma titulo pela propriedade title soup
print(soup.title.string)

#Pesquisa tipos específicos de tags do Beautifulsoup cuja os atributos correspondem a determinados valores ex: (passamos como parametros a tag HTML 'span' e a 'class'ou 'id' da tag )
print(soup.find('h1', class_='title').string)





