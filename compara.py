# Lê os hashes do arquivo com login/senha/hash
senhas1 = {}
with open("usuarios.txt", "r") as f1:
    for linha in f1:
        login, senha, hash_senha = linha.strip().split(";")
        senhas1[hash_senha] = senha

# Lê os hashes do arquivo de senhas e verifica se há algum hash igual
with open("senhas.txt", "r") as f2:
    for linha in f2:
        senha, hash_senha = linha.strip().split(";")
        if hash_senha in senhas1:
            print("Senha: ", senhas1[hash_senha])
            print("Hash igual encontrado: ", hash_senha)
