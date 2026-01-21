# 1 - Função para imprimir uma mensagem
def welcome():
    print("Bem-Vindos ao desespero Movies")

'''for i in range(50):
    welcome()'''

'''# 2 - Função calcular média de notas
def calculate_average():
    num_ratings = int(input("Digite a quantidade de avaliações que deseja fazer:\n"))
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a note do filme:\n"))
        total += note

    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0
    
    return average

print (f"A média de avaliações é: {calculate_average():.2f}")'''

# 3 - Cadastrando filmes:
def create_movie():
    name = input("Digite o nome do filmes:\n")
    yearLaunch = int(input("Digite o ano de lançamento do filmes:\n"))
    moviePrice = float(input("Digite o preço do filme:\n"))
    rating = float(input("Digite a nota do filme:\n"))
    print(f"{name}, ({yearLaunch}) - R$ {moviePrice:.2f}, com a nota {rating:.2f}")

create_movie()
create_movie()