salario = float(input("Digite o salário do funcionário: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas por dia: "))
dias_trabalhados = int(input("Digite o número de dias trabalhados: "))
salario = salario * dias_trabalhados
salario_hora = salario / (horas_trabalhadas * dias_trabalhados)
print(f"O salário por hora do funcionário é: R$ {salario_hora:.2f}")
# O código acima calcula o salário por hora de um funcionário com base no salário total e nas horas trabalhadas. Ele solicita ao usuário que insira o salário e as horas trabalhadas, realiza a divisão para obter o salário por hora e exibe o resultado formatado com duas casas decimais.