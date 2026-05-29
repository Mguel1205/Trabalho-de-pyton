# Programa de dicionário de contatos com adição de novos números

# Cria um dicionário vazio
contatos = {}

# Pergunta quantos contatos o usuário deseja adicionar
quantidade = int(input("Quantos contatos deseja adicionar? "))

# Cadastro dos contatos
for i in range(quantidade):
    print(f"\nContato {i + 1}")

    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")

    # Adiciona o contato ao dicionário
    contatos[nome] = telefone

# Exibe os contatos cadastrados
print("\nLista de contatos:")

for nome, telefone in contatos.items():
    print(f"Nome: {nome} | Telefone: {telefone}")
