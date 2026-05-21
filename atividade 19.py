# Programa simples de Web Scraping

# Importa as bibliotecas
import requests
from bs4 import BeautifulSoup

# URL do site
url = "https://example.com"

# Faz a requisição para o site
resposta = requests.get(url)

# Verifica se a requisição funcionou
if resposta.status_code == 200:

    # Analisa o conteúdo HTML
    site = BeautifulSoup(resposta.text, "html.parser")

    # Captura o título da página
    titulo = site.title.string

    # Exibe o título
    print("Título da página:")
    print(titulo)

else:
    print("Erro ao acessar o site.")