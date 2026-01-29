#Utilizando o input do Python

name = input('Digite o nome do filme: \n')
yearLaunch = int(input('Digite o ano de lancamento: \n')) #Conversao explicita de dados para inteiro
noteMovie = float(input('Digite a nota do filme: \n'))

print('O filme escolhido foi: ', name)
print('O ano de lancamento: ', yearLaunch, type(yearLaunch))
print('A note do filme: ', noteMovie, type(noteMovie))
