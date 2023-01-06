import getpass

# Pergunta ao usuário qual é o seu nome de usuário
username = input("Nome de usuário: ")

# Se o nome de usuário for "admin", solicita a senha
if username == "admin":
    senha = getpass.getpass("Senha: ")

    # Se a senha estiver correta, exibe uma mensagem
    if senha == "SenhaAdmin":
        print("Acesso concedido")
    else:
        print("Senha incorreta")
else:
    print("Nome de usuário incorreto")
