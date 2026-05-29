# Jogo da Forca em Python

# Importa a biblioteca random
import random

# Lista de palavras
palavras = ["python", "computador", "programacao", "teclado", "internet"]

# Escolhe uma palavra aleatória
palavra = random.choice(palavras)

# Lista para armazenar letras descobertas
letras_descobertas = ["_"] * len(palavra)

# Número de tentativas
tentativas = 6

print("=== JOGO DA FORCA ===")

# Loop principal do jogo
while tentativas > 0 and "_" in letras_descobertas:

    # Exibe a palavra atual
    print("\nPalavra:", " ".join(letras_descobertas))
    print("Tentativas restantes:", tentativas)

    # Entrada do usuário
    letra = input("Digite uma letra: ").lower()

    # Verifica se a letra existe na palavra
    if letra in palavra:

        # Atualiza as letras descobertas
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra

        print("Letra correta!")

    else:
        tentativas -= 1
        print("Letra incorreta!")

# Verifica se o jogador venceu
if "_" not in letras_descobertas:
    print("\nParabéns! Você venceu!")
else:
    print("\nVocê perdeu!")

# Exibe a palavra correta
print("A palavra era:", palavra)
