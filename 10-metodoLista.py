animeList = ['Black Clover', 'Attack on Titans', 'Boku no Hero', 
             'Lord Of The Mysters', 'To Be Hero X']

# 1 -Tamanho da Lista
print(len(animeList))

# 2 -Recuperar um item da lista pelo nome
print(animeList.index('Black Clover'))

# 3- Adicionar item ao final da lista
animeList.append('The Lord of The Rings') # O metodo .append adiciona na lista mais filmes e etc...
print(animeList)

# 4- Ordenar lista
animeList.sort()
print(animeList)

# 5 - Copiar os itens da lista para outra
animeCopy = animeList.copy()
animeCopy.remove('The Lord of The Rings')
print(animeCopy)

# 6 - Remove todos os itens da lista
animeList.clear()
print(animeList)