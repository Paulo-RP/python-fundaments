# 1 - Listando valores de 0 a 10 que sejam menores do que 4
listNumbers = [i for i in range(11) if i < 11]
print(listNumbers)

# Lista de filmes
movieList = ["Interstellar", "Senhor dos Anéis", "Star Wars", "Vingadores"]

# 2 - Filmes que possuem a letra "o" no título
movieWithO = [movie for movie in movieList if 'o' in movie.lower()]
print(movieWithO)

# 3 - Filmes que eu assisti
moviesWatched = [movie for movie in movieList if movie != "Vingadores"]
print(moviesWatched)

# 4 - Encontrando filme pelo nome
while True:
    searchName = input("Digite o nome do filme para buscar na lista (ou sair para encerrar):\n")
    if searchName.lower() == "sair":
        print("Programa Encerrado")
        break

    foundMovies = [movie for movie in movieList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme encontrado com o nome: {searchName}:")
        for foundMovie in foundMovies:
            print(foundMovie)
    else:
        print(f"Nenhum filme foi encontrado com o nome {searchName}. Tente novamente!")