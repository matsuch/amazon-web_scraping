# Amazon Web Scrapping

### Sumario

1. [Resumo](#brief)
2. [Requisitos](#requirements)
3. [Instruções de instalação](#installation)
4. [Descrição dos arquivos](#files)

## Resumo do projeto<a name="brief"></a>

Este projeto tem como objetivo realizar a extração de alguns dados do site amazon.com e enviá-los para o google sheets. Dados extraidos:
  - Link do produto
  - Nome do produto
  - Valor
  - Avaliação (nota)
  - Disponibilidade (Em estoque)

![amazon_webscraping](https://github.com/matsuch/web_scrapping/assets/77889112/4e6311b5-bf33-43d7-bc5b-c46a98538ced)

## Requisitos <a name="requirements"></a>

O código deve ser executado sem problemas usando Python versões 3 com as seguintes bibliotecas: 
  - Web Scrapping: BeautifulSoup
  - Google Integrations: Oauth2client, gspread

## Instruções de instalação <a name="installation"></a>

1. Crie um projeto na sua conta do Google Drive.

    - Habilite as APIs do Google Drive e Google Sheets.
    - Crie as credenciais de acesso e gere o arquivo JSON, salve como "credenciais.json"
    - Tutorial: https://pt.linkedin.com/pulse/manipulando-planilhas-do-google-usando-python-renan-pessoa

2. Faça login na sua conta amazon e na página inicial acesse o inspetor do navegador (F12)

    - Procure por Rede, no primeiro link que aparecer clique com o botão direito do mouse e vá em Copiar valor > Copiar como cURL

![baixar_ccurl](https://github.com/matsuch/web_scrapping/assets/77889112/b907de81-de7c-414a-9ee7-2b419f616b70)

    - Acesse o site: https://curlconverter.com/ copie o cCurl e converta em JSON.
    - Acesse o site: https://jsoneditoronline.org/#left=local.pelema e salve como "url_parameters.json"

3. Abra o arquivo "links.csv" e informe todas as URLs que você deseja buscar, cada URL em uma linha (mantenha o cabecalho)

## Descrição dos arquivos <a name="files"></a>

- **Dados**
  - links.csv - *tabela com a lista de links que voce deseja buscar*
  - requirements.txt - *lista das bibliotecas necessarias para rodar o codigo*
  - web_scrapping.py - *Código em python para fazer o web scraping*

**ATENÇÃO**: Não se esqueça de criar os arquivos JSON descritos na etapa **Instruções de instalação**
