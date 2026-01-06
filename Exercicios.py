# Exercicio 6 - Listas
'''num1 = int(input('Num1\n'))
num2 = int(input('Num2\n'))
num3 = int(input('Num3\n'))

list = [num1, num2, num3]
print(list)
print(num1)
print(num1+num2+num3)'''

'''# Exercicio 7 - Tupla
city1 = input('City 01\n')
city2 = input('City 02\n')
city3 = input('City 03\n')
cidades = (city1,city2,city3)
print(cidades)
print(city3)
print(len(cidades))'''

# Exercicio 8 - Set
'''num1 = int(input('num1\n'))
num2 = int(input('num2\n'))
num3 = int(input('num3\n'))
num4 = int(input('num4\n'))
num5 = int(input('num5\n'))

numSets = {num1, num2, num3, num4, num5}
print(numSets)
print(len(numSets))
maiorNumero = max(numSets)
print(maiorNumero)'''

# Exercício 9 - Dicionário
'''prod1 = (input("Primeiro Produto\n"))
valor1 = float(input("Coloque o valor do seu produto 1\n"))
prod2 = (input("Segundo Produto\n"))
valor2 = float(input("Coloque o valor do seu produto 2\n"))
prod3 = (input("Terceiro Produto\n"))
valor3 = float(input("Coloque o valor do seu produto 3\n"))

listaProdutos = {
    prod1: valor1,
    prod2: valor2,
    prod3: valor3
}

# 1 - Dicionário completo
print(listaProdutos)

# 2 - O produto mais caro
prodMaisCaro = max(listaProdutos, key=listaProdutos.get)
print(prodMaisCaro)

# 3 - Tirar média dos produtos
mediaProd = (valor1 + valor2 + valor3) / 3
print(f"{mediaProd:.2f}")'''