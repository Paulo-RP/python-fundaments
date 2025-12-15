animesSet = {'Black Clover', 'Attack on Titans', 'Boku no Hero', 
             'Lord Of The Mysters', 'To Be Hero X'}
print(type(animesSet))

# 1 - Buscar o tamanho do Set
print(len(animesSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {"To Be Hero X", True, 1, 8.7}
print(exampleSet)

# 3 - Adicionar item de outro set
animesSet.update(exampleSet)
print(animesSet)

# 4 - Remover item no set
animesSet.remove(True)
animesSet.remove(8.7)
print(animesSet)

# 5 - Definir o maior numero do set 

num1 = int(input('num1\n'))
num2 = int(input('num2\n'))
num3 = int(input('num3\n'))
num4 = int(input('num4\n'))
num5 = int(input('num5\n'))

numSets = {num1, num2, num3, num4, num5}
maiorNumero = max(numSets)
print(maiorNumero)