animeInception = {
    "title": "Inception",
    "yearRelease": 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-fi", "Action", "Thriller"]
}
print(animeInception)
print(len(animeInception))
print(type(animeInception))

# 1 - Como recuperar um elemento do dicionario

print(animeInception["genre"])
print(animeInception.get("imdbRating"))

# 2 - Buscar apenas as chaves do dicionario
print(animeInception.keys())

# 3 - Busca apenas valores do dicionário
print(animeInception.values())

# 4 - Buscar itens do dicionário com chave e valor
print(animeInception.items())

# 5 - Adicionar itens no dicionário
animeInception["director"] = "Christopher Nolan"
print(animeInception)

# 6 - Atualizar itens no dicionário
animeInception.update({"imdbRating": 8.7})
print(animeInception)

# 7 - Remover item do dicionário
animeInception.pop("director")
print(animeInception)