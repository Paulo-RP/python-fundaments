movieName = 'Demon Slayer'
movieDescription = '''Filme de ficção científica muito foda, com várias referências ao buraco de minhoca e teoria da relatividade'''

print(movieName.upper()) # Tudo em maiúsculo
print(movieName.lower()) # Tudo em minúsculo
print(movieName.capitalize()) # Primeira letra em maiúscula
print(movieName.title()) # Primeira letra em maiúsculo
print(movieName.center(24, '-'))
print(movieName.find("e"))
print(movieName.find("a"))
print(movieName.replace('Slayer', 'Abacate')) #Substituí palavras e etc
print(movieDescription.split(','))