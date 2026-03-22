senha = input("Digite sua senha:")
confirmacao = input("Confirme sua senha:")

if senha == confirmacao:
    print("Senha confirmada com sucesso!")
    if len(senha) >= 6:
        print("A senha tem pelo menos 6 caracteres.")
    else:
        print("A senha deve ter pelo menos 6 caracteres.")
else:
    print("As senhas não coincidem. Tente novamente.")
# O código acima solicita ao usuário que insira uma senha e a confirme, e então verifica se as duas entradas são iguais, informando o resultado ao usuário.