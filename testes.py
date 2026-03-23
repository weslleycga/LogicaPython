"""

 Declaração de Variáveis
x, y, z = "Orange", "Banana", "Cherry"
print(f"A variavel x é: {x}")
print(f"A variavel y é: {y}")
print(f"A variavel z é: {z}")

"""
"""
Atribuição de Variáveis

fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print(f"A variavel x é: {x}")
print(f"A variavel y é: {y}")
print(f"A variavel z é: {z}")


 ##### variáveis globais ############

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = b"Hello"
print(x)


 ##### dicionários ############
 
# Criar um dicionário
x = {"name" : "Weslley", "age" : 24}

# Acessar um valor
print(x["name"]) # Saída: weslley

# Adicionar ou alterar uma informação
x["city"] = "São Luís"
x["age"] = 37

# Remover uma informação
del x["name"]
"""
