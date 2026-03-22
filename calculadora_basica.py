num1 = 0
num2 = 0
operacao = ""
resultado = 0
continuar = "s" #variável para controlar se o usuário deseja continuar realizando operações
#bloco 2: O programa realiza a operação escolhida e exibe o resultado
while continuar == "s":

   if continuar == "s":
       #bloco 1: O usuario escolhe a operação desejada e insere os números para a operação
    operacao = input("Digite a operação desejada (+, - , *, / , %  0 para sair):")
    if operacao == "0":
        
        break
    elif operacao in ["+", "-", "*", "/", "%"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if operacao == "+":
                resultado = num1 + num2
                print(f"O resultado da soma é: {resultado}")
        elif operacao == "-":
                resultado = num1 - num2
                print(f"O resultado da subtração é: {resultado}")
        elif operacao == "*":
                resultado = num1 * num2
                print(f"O resultado da multiplicação é: {resultado}")
            
        elif operacao == "/":
                if num2 == 0: #verifica se o segundo número é zero para evitar divisão por zero
                    print("Erro: Divisão por zero não é permitida.")
                else:
                    resultado = num1 / num2
                    print(f"O resultado da divisão é: {resultado}")
                    
        elif operacao == "%":
                resultado = num1 % num2
                print(f"O resultado do resto da divisão é: {resultado}")
    else:
            print("Operação inválida. Por favor, escolha uma operação válida.")
            
print("Obrigado por usar a calculadora básica!")

