import hashlib
import string
import random

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    # Recebe os dados do novo usuário
    nome = input("Informe o nome completo: ")
    usuario = input("Informe o nome de usuário: ")
    senha = input("Informe a senha (mínimo 6 caracteres, com pelo menos uma letra maiúscula, uma letra minúscula e um número): ")
    confirmacao_senha = input("Confirme a senha: ")

    # Verifica se a senha atende aos requisitos de segurança
    if len(senha) < 6 or not any(c.isupper() for c in senha) or not any(c.islower() for c in senha) or not any(c.isdigit() for c in senha):
        print("Senha inválida. A senha deve ter pelo menos 6 caracteres, com pelo menos uma letra maiúscula, uma letra minúscula e um número.")
        return

    # Verifica se a senha e a confirmação de senha são iguais
    if senha != confirmacao_senha:
        print("A senha e a confirmação de senha não correspondem.")
        return

    # Abre o arquivo de usuários em modo de leitura
    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()

    # Verifica se o nome de usuário já existe
    if usuario in [u.split(",")[0].strip() for u in usuarios]:
        print("O nome de usuário já existe. Escolha outro nome.")
        return

    # Gera o hash da senha
    senha_hash = hashlib.sha512(senha.encode()).hexdigest()

    # Adiciona o novo usuário no arquivo de usuários
    novo_usuario = f"{usuario},{senha_hash}\n"
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(novo_usuario)

    print("Usuário cadastrado com sucesso.")


# Função para realizar o login
def realizar_login():
    # Recebe o nome de usuário e a senha
    usuario = input("Informe o nome de usuário: ")
    senha = input("Informe a senha: ")

    # Abre o arquivo de usuários em modo de leitura
    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()

    # Verifica se o nome de usuário e a senha são válidos
    for u in usuarios:
        usuario_arq, senha_hash = u.strip().split(",")
        if usuario_arq == usuario:
            if hashlib.sha512(senha.encode()).hexdigest() == senha_hash:
                print(f"Bem-vindo, {usuario}!")
                return

    print("Usuário ou senha inválidos.")


# Função para gerar X usuários
def gerar_usuarios(qtd):
    for i in range(qtd):
        nome = f"Usuário{i+1}"
        usuario = f"usuario{i+1}"
        caracteres = string.ascii_letters + string.digits
        senha = "".join(random.choices(caracteres, k=6))
        senha_hash = hashlib.sha512(senha.encode()).hexdigest()
        novo_usuario = f"{usuario},{senha_hash}\n"
        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(novo_usuario)


# Função para gerar um usuario com senha fraca
def gerar_usuarios_fraco(qtd):
    for i in range(qtd):
        nome = f"Usuáriosenhafraca{i+1}"
        usuario = f"usuario{i+1}"
        caracteres = string.ascii_letters
        senha = "".join(random.choices(caracteres, k=2))
        senha_hash = hashlib.sha512(senha.encode()).hexdigest()
        novo_usuario = f"{usuario},{senha_hash}\n"
        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(novo_usuario)


while True:
    print("1. Cadastrar usuário")
    print("2. Realizar login")
    print("3. Gerar X usuários com senha padrão")
    print("4. Gerar usuários com senha fraca")
    print("0. Sair do programa")
    opcao = input("Escolha uma opção (1, 2, 3, 4 ou 0): ")
    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        realizar_login()
    elif opcao == "3":
        qtd = int(input("Informe a quantidade de usuários a serem gerados: "))
        gerar_usuarios(qtd)
    elif opcao == "4":
        qtd = int(input("Informe a quantidade de usuários a serem gerados: "))
        gerar_usuarios_fraco(qtd)
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")