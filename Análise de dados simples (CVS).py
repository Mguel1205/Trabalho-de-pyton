# Programa de análise simples de dados CSV

# Importa a biblioteca pandas
import pandas as pd

# Lê o arquivo CSV
dados = pd.read_csv("dados.csv")

# Exibe as primeiras linhas do arquivo
print("Primeiras linhas do arquivo:\n")
print(dados.head())

# Exibe informações gerais
print("\nInformações do arquivo:\n")
print(dados.info())

# Exibe estatísticas básicas
print("\nEstatísticas dos dados:\n")
print(dados.describe())
