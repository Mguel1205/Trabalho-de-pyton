# Programa de visualização de dados com matplotlib

# Importa as bibliotecas
import matplotlib.pyplot as plt

# Dados do gráfico
meses = ["Jan", "Fev", "Mar", "Abr", "Mai"]
vendas = [150, 200, 180, 250, 300]

# Cria o gráfico de linhas
plt.plot(meses, vendas)

# Adiciona título ao gráfico
plt.title("Vendas por Mês")

# Nome do eixo X
plt.xlabel("Meses")

# Nome do eixo Y
plt.ylabel("Quantidade de Vendas")

# Exibe o gráfico
plt.show()