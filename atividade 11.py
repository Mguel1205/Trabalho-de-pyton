# Programa para ler um arquivo de texto

# Abre o arquivo no modo leitura
with open("texto.txt", "r", encoding="utf-8") as arquivo:
    
    # Lê o conteúdo do arquivo
    conteudo = arquivo.read()

# Exibe o conteúdo na tela
print("Conteúdo do arquivo:\n")
print(conteudo)