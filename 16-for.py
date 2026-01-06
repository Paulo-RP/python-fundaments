# Lista de filmes
movieList = ["Interstellar", "Senhor dos Anéis", "Star Wars", "Vingadores"]

# 1 - Iterando valores de uma lista
for movie in movieList:
    print(movie)

line = "-"
print(line*50)

for movie in movieList: # Estrutura de repetição for
    if movie == "Star Wars": # Condição if
        break # Para, o laço até determinada o nome do filme da lista
    print(movie)

print(line*50)

for movie in movieList:
    if movie == "Interstellar":
        continue # Continue pula o que é determinado na condição
    print(movie)

print(line*50)

# 2 - Avaliação de filme

movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite a quantidade de avaliação você deseja fazer:\n"))

total = 0 # Essa variável é para controle
for i in range(movieRating):
    note = float(input("Digite a nota para o filme:\n"))
    total += note

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average}")