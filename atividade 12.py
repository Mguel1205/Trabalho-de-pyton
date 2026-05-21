# Programa gerador de senhas aleatórias

# Importa a biblioteca random
import random
import string

# Define o tamanho da senha
tamanho = int(input("Digite o tamanho da senha: "))

# Junta letras, números e símbolos
caracteres = string.ascii_letters + string.digits + string.punctuation

# Gera a senha aleatória
senha = ""

for i in range(tamanho):
    senha += random.choice(caracteres)

# Exibe a senha gerada
print(f"\nSenha gerada: {senha}")