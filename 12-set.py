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