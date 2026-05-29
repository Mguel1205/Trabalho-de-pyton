# Programa de tabuada

# Entrada de dados
numero = int(input("Digite um número para ver a tabuada: "))

# Exibe a tabuada de 1 até 10
print(f"\nTabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
