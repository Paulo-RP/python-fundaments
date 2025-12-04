#Concatenacao de valores

name = input('Digite o nome do filme: \n')
yearLaunch = int(input('Digite o ano de lancamento: \n'))
noteMovie = float(input('Digite a nota do filme: \n'))

# print('O filme',name, 'é uma ótima producao, lancado em',yearLaunch, 'tem uma nota de avaliacao pela imdb de',noteMovie)

print(f'Nome do filme: {name}\n'
      f'Ano de lancamento: {yearLaunch}\n'
      f'Nota do filme: {noteMovie}\n'
      )