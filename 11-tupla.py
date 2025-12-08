animesTuple = ('Black Clover', 'Attack on Titans', 'Boku no Hero', 
             'Lord Of The Mysters', 'To Be Hero X')
print(type(animesTuple))

# 1 - Buscar os dois primeiros itens da tupla
print(animesTuple[:2])

# 2 - Buscar o último item da tupla
print(animesTuple[-1]) 

# 3 - Buscar animes até uma determinada position
print(animesTuple[:4])

# 4 - Buscar animes de uma posição em diante
print(animesTuple[3:])

# 5 - Recuperar um item da tuple pelo name
print(animesTuple.index('Boku no Hero'))