#Vou criar um programa que leia um numero e mostre a sequencia ate um numero digitado (sem ajuda de bibliotecas)

n = int(input("Digite um numero:"))
n1 = int(input("Digite ate onde devemos contar:"))
contador = n
print(f"Contando de {n} até {n1}:")
while contador <= n1:
    print(contador)
    contador += 1
# O código acima solicita ao usuário que insira um número inicial e um número final, e então conta de 0 até o número final, exibindo cada número na sequência.
print("Contagem concluída.")