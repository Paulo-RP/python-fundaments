line = ("*")
'''# 1 - Função para imprimir um nome completo
def full_name(first_name, last_name):
    print(f"Nome é: {first_name} {last_name}")

full_name("Paulo", "Silva")
print(line*50)

# 2 - Função para somar dois números
def sum_numbers(a, b, c):
    return a + b + c

primeiro = float(input("Primeiro número da soma\n"))
segundo = float(input("Segundo número da soma\n"))
terceiro = float(input("Terceiro número da soma\n"))

print(f"Soma é: {sum_numbers(primeiro, segundo, terceiro)}")'''

'''# 3 - Função com parâmetro default
def address(country="Brasil"):
    print(f"O país que resíduo é: {country}")

address()'''

# 4 - Função para avaliar filmes
def rate_movie(num_ratings, movie_name):
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme:\n"))
        total += note

    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0
    
    print(f"Média de avaliação do filme: {movie_name} é: {average:.2f}")

rate_movie(2, "Sonic")