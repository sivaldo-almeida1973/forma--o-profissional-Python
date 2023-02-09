#Buscando uma Tabela de Wikipedia e Transformando em Data Frame(ler uma tabela)
import pandas as pd #
import urllib3 # fazer requisiçõa de uma pagina(site todo)
from bs4 import BeautifulSoup 
def faz_requiscao(site):
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
  manager = urllib3.PoolManager()
  return manager.request('GET', site, headers={'User-Agent': 'Mozilla/5.0'})

def le_site(site):
  response = faz_requiscao(site)
  return BeautifulSoup(response.data, 'html.parser')

def func_le_paises():
  bs = le_site('https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_riqueza_total')
  table = bs.find('table', style='text-align: reight')
  if (table == None):
   raise Exception('Table não encontrada')
  
  corpo = table.find('tbody')
  if(corpo == None):
   raise Exception('corpo da tabela não encontrado')
  
  items = corpo.find_all('tr')

  paises = []
  for item in items:
    dados = item.find_all('td')
    item_pais = []
    for dado in dados:
      item_pais.append(dado.text.replace('\n',''))
    
    if len(item_pais) > 0:
      paises.append(item_pais)
  return paises


print(func_le_paises())









