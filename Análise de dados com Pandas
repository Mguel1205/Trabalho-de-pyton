# Programa de análise de dados com pandas

# Importa a biblioteca pandas
import pandas as pd

# Lê o arquivo CSV
dados = pd.read_csv("dados.csv")

# Exibe os dados do arquivo
print("Dados do arquivo:\n")
print(dados)

# Exibe as 5 primeiras linhas
print("\nPrimeiras linhas:\n")
print(dados.head())

# Exibe informações das colunas
print("\nInformações gerais:\n")
print(dados.info())

# Exibe estatísticas numéricas
print("\nEstatísticas dos dados:\n")
print(dados.describe())

# Exibe valores nulos
print("\nValores nulos por coluna:\n")
print(dados.isnull().sum())

# Exemplo de filtro
print("\nFiltro de valores maiores que 50:\n")

# Verifica se existe a coluna "valor"
if "valor" in dados.columns:
    filtro = dados[dados["valor"] > 50]
    print(filtro)
else:
    print("A coluna 'valor' não foi encontrada.")
