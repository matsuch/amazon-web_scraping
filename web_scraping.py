# bibliotecas
from oauth2client.service_account import ServiceAccountCredentials
from urllib.parse import urlparse
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd

import requests
import gspread
import time
import json
import re

start = time.time()

# acessa um arquivo csv com os links desejados
links_df = pd.read_csv("links.csv")
links_list = links_df['Links'].tolist()

# cria uma tabela vazia com as colunas desejadas
df = pd.DataFrame(columns=['Link', 'Produto', 'Preco', 'Avaliacao', 'Disponibilidade', 'Hora Pesquisa'])

# abre o arquivo JSON com os parametros da URL
with open('./url_parameters.json') as file:
    data = json.load(file)

# extrair os objetos "cookies", "headers" e "queries"
cookies = data.get('cookies', {})
headers = data.get('headers', {})
params = data.get('queries', {})

# percorre todos os links da lista e busca as informacoes desejadas
for link in links_list:

    URLs = requests.get(
        link,
        params=params,
        cookies=cookies,
        headers=headers,
    )
    
    # solicita request para a URL
    #URLs = requests.get(link, headers=HEADERS)
    soup = BeautifulSoup(URLs.content, "lxml")
      
    # extrair o link
    parsed_url = urlparse(link)
    link = parsed_url.netloc + parsed_url.path
    
    # Extrai os dados desejados
    title = soup.find("span", attrs={"id":'productTitle'}).string.strip()
    price = re.sub(r'[^0-9,]', '', soup.find("span", class_="a-offscreen").string.strip())
    availability = soup.find("div", attrs={"id":'availability'})
    availability = availability.find("span").string.strip()
    review = soup.find("span", class_="a-icon-alt").string
    
    # Para cada link, adiciona uma linha ao dataframe criado
    df = pd.concat([df, pd.DataFrame({'Link': [link],
                                      'Produto': [title],
                                      'Preco': [price],
                                      'Avaliacao': [review],
                                      'Disponibilidade': [availability],
                                      'Hora Pesquisa': datetime.now()
                                      })],
                   ignore_index=True)

# converte a coluna 'data_hora' para o formato desejado
df['Hora Pesquisa'] = df['Hora Pesquisa'].dt.strftime('%d/%m/%Y %H:%M:%S')

#### Integracao com Google Sheets ####

# escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

# dados de autenticação do gsheet
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credenciais.json', scope)

# autentica o gs
gc = gspread.authorize(credentials)

# abre a planilha
wks = gc.open_by_key('ID-DO-SEU-SHEET') # insira aqui o ID do seu sheet

# seleciona a primeira página da planilha
worksheet = wks.get_worksheet(0)

# converte os valores do df em uma lista
#data = [df.columns.tolist()] + df.values.tolist()
data = df.values.tolist()

# salva os dados na tabela do Google Sheets
#worksheet.clear()  # Limpe a tabela existente
worksheet.append_rows(data)  # Adicione os dados do DataFrame

end = time.time()

print('Codigo finalizado em', end-start, 'segundos')
