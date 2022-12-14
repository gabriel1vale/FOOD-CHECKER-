#Tauste - Arroz
#Ignorar os 5 últimos valores: são valores usados nos filtros de preço.

import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://tauste.com.br/marilia/mercearia/alimentos-basicos.html?cat=499")
soup = BeautifulSoup(page.text, 'html.parser')

with open("arroz_tauste.csv", "w", newline="") as arquivo:
  final = csv.writer(arquivo, delimiter=";")
    
  for produto in soup.find_all(class_="product-item-name"):
    produto = str(produto.text).strip()
    final.writerow([produto])
    print(produto)
  for valor in soup.find_all(class_="price"):
    valor = (valor.text).replace(",",".").strip()
    final.writerow([valor])
    print(valor)

#Amigão - Arroz

import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://marilia.amigaoonline.com.br/alimentos-basicos/arroz.html")
soup = BeautifulSoup(page.content, "html.parser")


with open("arroz-amigao.csv", "w", newline="") as arquivo:
  final = csv.writer(arquivo, delimiter=";")
  final.writerow(["Produto"])

  for produto in soup.find_all(class_="product-name"):
    produto = str(produto.text).strip()
    final.writerow([produto])
    print(produto)   
  for valor in soup.find_all(class_=["regular-price","special-price"]):
    valor = str(valor.text).replace("Por:","").replace(",",".").strip()
    final.writerow([valor])
    print(valor)

#Tauste - Feijão
#Ignorar os 3 últimos valores: são valores usados nos filtros de preço.

import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://tauste.com.br/marilia/mercearia/alimentos-basicos.html?cat=502")
soup = BeautifulSoup(page.text, 'html.parser')

with open("feijao_tauste.csv", "w", newline="") as arquivo:
  final = csv.writer(arquivo, delimiter=";")
    
  for produto in soup.find_all(class_="product-item-name"):
    produto = str(produto.text).strip()
    final.writerow([produto])
    print(produto)
  for valor in soup.find_all(class_="price"):
    valor = (valor.text).replace(",",".").strip()
    final.writerow([valor])
    print(valor)

#Amigão - Feijão

import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://marilia.amigaoonline.com.br/alimentos-basicos/feijao.html")
soup = BeautifulSoup(page.content, "html.parser")


with open("feijao-amigao.csv", "w", newline="") as arquivo:
  final = csv.writer(arquivo, delimiter=";")
  final.writerow(["Produto"])

  for produto in soup.find_all(class_="product-name"):
    produto = str(produto.text).strip()
    final.writerow([produto])
    print(produto)   
  for valor in soup.find_all(class_=["regular-price","special-price"]):
    valor = str(valor.text).replace("Por:","").replace(",",".").strip()
    final.writerow([valor])
    print(valor)

#Tauste - Açúcar
#Ignorar os 11 últimos valores: são valores usados nos filtros de preço.

import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://tauste.com.br/marilia/mercearia/alimentos-basicos.html?cat=508&p=2")
soup = BeautifulSoup(page.text, 'html.parser')

with open("açucar_tauste.csv", "w", newline="") as arquivo:
  final = csv.writer(arquivo, delimiter=";")
    
  for produto in soup.find_all(class_="product-item-name"):
    produto = str(produto.text).strip()
    final.writerow([produto])
    print(produto)
  for valor in soup.find_all(class_="price"):
    valor = (valor.text).replace(",",".").strip()
    final.writerow([valor])
    print(valor)

#Amigão - Açúcar

import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://marilia.amigaoonline.com.br/alimentos-basicos/acucar.html")
soup = BeautifulSoup(page.content, "html.parser")


with open("açucar-amigao.csv", "w", newline="") as arquivo:
  final = csv.writer(arquivo, delimiter=";")
  final.writerow(["Produto"])

  for produto in soup.find_all(class_="product-name"):
    produto = str(produto.text).strip()
    final.writerow([produto])
    print(produto)   
  for valor in soup.find_all(class_=["regular-price","special-price"]):
    valor = str(valor.text).replace("Por:","").replace(",",".").strip()
    final.writerow([valor])
    print(valor)

#Tauste - Óleo
#Ignorar os 3 últimos valores: são valores usados nos filtros de preço.

import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://tauste.com.br/marilia/mercearia/alimentos-basicos.html?cat=505")
soup = BeautifulSoup(page.text, 'html.parser')

with open("oleo_tauste.csv", "w", newline="") as arquivo:
  final = csv.writer(arquivo, delimiter=";")
    
  for produto in soup.find_all(class_="product-item-name"):
    produto = str(produto.text).strip()
    final.writerow([produto])
    print(produto)
  for valor in soup.find_all(class_="price"):
    valor = (valor.text).replace(",",".").strip()
    final.writerow([valor])
    print(valor)

#Amigão - Óleo

import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://marilia.amigaoonline.com.br/alimentos-basicos/oleo.html")
soup = BeautifulSoup(page.content, "html.parser")


with open("oleo-amigao.csv", "w", newline="") as arquivo:
  final = csv.writer(arquivo, delimiter=";")
  final.writerow(["Produto"])

  for produto in soup.find_all(class_="product-name"):
    produto = str(produto.text).strip()
    final.writerow([produto])
    print(produto)   
  for valor in soup.find_all(class_=["regular-price","special-price"]):
    valor = str(valor.text).replace("Por:","").replace(",",".").strip()
    final.writerow([valor])
    print(valor)

#Tauste - Farinha
#Ignorar os 3 últimos valores: são valores usados nos filtros de preço.

import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://tauste.com.br/marilia/mercearia/alimentos-basicos.html?cat=511")
soup = BeautifulSoup(page.text, 'html.parser')

with open("farinha_tauste.csv", "w", newline="") as arquivo:
  final = csv.writer(arquivo, delimiter=";")
    
  for produto in soup.find_all(class_="product-item-name"):
    produto = str(produto.text).strip()
    final.writerow([produto])
    print(produto)
  for valor in soup.find_all(class_="price"):
    valor = (valor.text).replace(",",".").strip()
    final.writerow([valor])
    print(valor)

#Amigão - Farinha

import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://marilia.amigaoonline.com.br/alimentos-basicos.html?cat=363")
soup = BeautifulSoup(page.content, "html.parser")


with open("farinha-amigao.csv", "w", newline="") as arquivo:
  final = csv.writer(arquivo, delimiter=";")
  final.writerow(["Produto"])

  for produto in soup.find_all(class_="product-name"):
    produto = str(produto.text).strip()
    final.writerow([produto])
    print(produto)   
  for valor in soup.find_all(class_=["regular-price","special-price"]):
    valor = str(valor.text).replace("Por:","").replace(",",".").strip()
    final.writerow([valor])
    print(valor)