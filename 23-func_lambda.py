'''Funções Lambda em Python são funções anônimas e curtas (sem nome), 
definidas com a palavra-chave lambda, ideais para tarefas simples de linha única e para uso como argumentos de funções de ordem superior como map(), filter() e sorted(), pois executam uma única expressão e retornam seu resultado automaticamente, sem return explícito'''

# Função de potência de um número
power = lambda num: num ** 2

# Função que verifica se o número é par
is_even = lambda x: x % 2 == 0  # Verifica se pe par, informa em boolean se é true ou false

# Função que divide um número por outro
div_num = lambda x, y: x / y 

# Função que reverte um string (slice)
reverse_string = lambda s: s[::-1]

print(power(5))
print(power(9))
print(is_even(30))
print(is_even(33))
print(div_num(10,5))
print(div_num(20,4))
print(reverse_string("Pythom"))
print(reverse_string("Security"))

# Funcionalidades relacionada aos filmes
movies_list = ["Avangers", "The Matrix", "Star Wars", "Interstellar", "Lord Of The Rings"]
ratings = {
    "Avangers": [8.5, 9.0, 7.9],
    "The Matrix": [8.0, 9.6, 8.9],
    "Star Wars": [6.5, 7.0, 8.9],
    "Interstellar": [7.5, 8.0, 9.9],
    "Lord Of The Rings": [7.5, 6.0, 7.9]
}

# Função para calcular a média de avaliações do filme
filme = ("Avangers")   #input("Digite o filme para saber a avaliação:\n")

average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

# Função que verifica se tem o filme na lista
check_movie = lambda movie_name: movie_name in movies_list

print(f"A média do filme {filme} é: {average_rating(filme):.2f}")
print(f"O filme {filme} está na lista? {check_movie(filme)}")