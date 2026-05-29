# Programa para calcular o fatorial de um número

# Entrada de dados
numero = int(input("Digite um número: "))

# Variável para armazenar o resultado
fatorial = 1

# Cálculo do fatorial
for i in range(1, numero + 1):
    fatorial *= i

# Exibe o resultado
print(f"\nO fatorial de {numero} é {fatorial}")
