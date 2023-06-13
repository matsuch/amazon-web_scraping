# Amazon Web Scraping

### Sumario

1. [Resumo](#brief)
2. [Requisitos](#requirements)
3. [Instruções de instalação](#installation)
4. [Descrição dos arquivos](#files)
5. [Resultado](#results)

## Resumo do projeto <a name="brief"></a>

Este projeto tem como objetivo realizar a extração de alguns dados do site amazon.com utilizando a biblioteca BeautifulSoup e enviá-los para o google sheets. Dados extraidos:
  - Link do produto
  - Nome do produto
  - Valor
  - Avaliação (nota)
  - Disponibilidade (Em estoque)

![amazon_webscraping](https://github.com/matsuch/amazon-web_scraping/assets/77889112/1e037e70-9351-46ab-b8ab-6b66185d8685)

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

    ![baixar_ccurl](https://github.com/matsuch/amazon-web_scraping/assets/77889112/86f86e1d-4599-4835-bf0d-d06dfc50cbb2)

    - Acesse o site: https://curlconverter.com/ copie o cCurl e converta em JSON.
    - Acesse o site: https://jsoneditoronline.org/#left=local.pelema e salve como "url_parameters.json"

3. Abra o arquivo "links.csv" e informe todas as URLs que você deseja buscar, cada URL em uma linha (mantenha o cabecalho)

4. Abra o arquivo "web_scraping.py" e na linha 83 informe o ID do seu Google Sheets.

![Captura de tela de 2023-06-12 22-30-06](https://github.com/matsuch/amazon-web_scraping/assets/77889112/97046eb7-4d73-46e0-ab88-5fbbb8607c45)

## Descrição dos arquivos <a name="files"></a>

- **Dados**
  - links.csv - *tabela com a lista de links que voce deseja buscar*
  - requirements.txt - *lista das bibliotecas necessarias para rodar o codigo*
  - web_scraping.py - *Código em python para fazer o web scraping*

## Resultados <a name="results"></a>

Toda vez que você rodar o código, serão adicionadas novas linhas com a data/hora que foi realizado a consulta.

![resultado_webscraping](https://github.com/matsuch/amazon-web_scraping/assets/77889112/1997445e-0464-4c45-a2f9-b245226ff5a2)

**ATENÇÃO**: Não se esqueça de criar os arquivos JSON descritos na etapa **Instruções de instalação**
