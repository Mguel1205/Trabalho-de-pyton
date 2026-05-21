# Programa de registro de logs

# Importa a biblioteca datetime
from datetime import datetime

# Mensagem que será registrada
mensagem = input("Digite uma mensagem para o log: ")

# Obtém a data e hora atual
agora = datetime.now()

# Formata a data e hora
data_hora = agora.strftime("%d/%m/%Y %H:%M:%S")

# Abre o arquivo de log no modo adicionar
with open("log.txt", "a", encoding="utf-8") as arquivo:
    
    # Escreve a mensagem no arquivo
    arquivo.write(f"[{data_hora}] {mensagem}\n")

# Exibe mensagem de confirmação
print("\nLog registrado com sucesso!")