# Lista de filmes
movieList = ["Interstellar", "Senhor dos Anéis", "Star Wars", "Vingadores"]

line = "*"

# 1 - Iterando valores de uma lista com while
index = 0
while index < len(movieList):
    print(movieList[index])
    index += 1
print(line*50)

# 2 - Quando a condição for atendida encerra o loop
index = 0
while index < len(movieList):
    if movieList[index] == "Vingadores":
        break
    print(movieList[index])
    index += 1
print(line*50)

# 3 - Quando a condição for atendida, loop vai para próxima iteração
index = 0
while index < len(movieList):
    if movieList[index] == "Star Wars":
        index += 1
        continue
    print(movieList[index])
    index +=1

# 4 - Avaliação de Filme
movieName = input("Digite o nome do filme:\n")
movieRating = float(input("Digite quantas avaliaçãoes deseja fazer:\n"))
total = 0
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filme:\n"))
    total += note
    count += 1

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")