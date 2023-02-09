#Web Scraping
#Coletar informações de um site de forma automatizada:
#pode ser contra politica de sites
#podem ver mecanismos de proteção.
#Normalmente não é uma tarefa simples:
#complexidade das paginas 
#conteúdo dinâmico
#mudanças frequentes
#mecanismos de preveção de consultas automatizadas.

import pandas as pd #
import urllib3 # fazer requisiçõa de uma pagina(site todo)
from bs4 import BeautifulSoup # ler por partes (fzer um parse)
def faz_requiscao(site):
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
  manager = urllib3.PoolManager()
  return manager.request('GET', site, headers={'User-Agent': 'Mozilla/5.0'})

def le_site(site):
  response = faz_requiscao(site)
  return BeautifulSoup(response.data, 'html.parser')

bs = le_site('https://www.horariodebrasilia.org/')
tag_hora = bs.find('p', id='relogio')
print(tag_hora.text)

bs = le_site('https://www.horariodebrasilia.org/')
tag_hora = bs.find('h3', id='dia-topo')
print(tag_hora.text)

