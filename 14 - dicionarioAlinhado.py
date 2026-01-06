import pprint # Ajuda na visualização na hora de print
animeDict = {
    "inception":{
        "yearRelease": 2010,
        "imdbRating": 8.6,
        "genre": ["Sci-Fi", "Action", "Thriller"]
    },
    "interstellar":{
        "yearRelease": 2014,
        "imdbRating": 8.9,
        "genre": ["Sci-Fi", "Drama"]
    },
    "The Dark Knight":{
        "yearRelease": 2008,
        "imdbRating": 9.0,
        "genre": ["Action", "Drama", "Crime"]
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(animeDict)

# 1 - Buscar informação dentro de um dicionário alinhado
print(animeDict["interstellar"]["imdbRating"])

# 2 - Adicionar novo item
animeDict["interstellar"]["director"] = "Paulo R. P. Silva"
pp.pprint(animeDict)

# 3 - Excluir um dicionário
del animeDict["The Dark Knight"]
pp.pprint(animeDict)