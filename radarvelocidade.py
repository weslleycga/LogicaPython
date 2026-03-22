print("Bem-vindo ao radar de velocidade!")
print("Digite a velocidade do veículo em km/h para verificar se está dentro do limite permitido.")
print("Para sair do programa, digite 999.")
vel = 0
while vel != 999: #condição para encerrar o programa, o usuário deve digitar 999 para sair
    vel = int(input("Digite a velocidade do veículo em km/h: "))
    if vel >= 40 and vel<= 60:
        print("Velocidade dentro do limite permitido.")
    elif vel < 40:
        print("Velocidade abaixo do minimo necessário! Dirija com cuidado.")
    elif vel > 60:
        print("Velocidade acima do limite permitido! Você foi multado.")     
print("Obrigado por usar o radar de velocidade!")