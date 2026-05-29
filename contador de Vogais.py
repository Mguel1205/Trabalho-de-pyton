# Programa para contar vogais em uma palavra ou frase

# Entrada de dados
texto = input("Digite uma palavra ou frase: ").lower()

# Variável para contar as vogais
contador = 0

# Verifica cada letra do texto
for letra in texto:
    if letra in "aeiou":
        contador += 1

# Exibe o resultado
print(f"\nQuantidade de vogais: {contador}")
