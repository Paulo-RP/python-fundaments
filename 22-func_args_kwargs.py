'''
*args - Utilizamos quando não temos certeza de quantos argumentos queremos em um função
- Os argumentos são passados como uma tupla

**kwargs - Além dos valores podemos passar também, passar as respectivas chaves para cada argumento.
- Os argumentos são passado como um dicionário

'''

def sum(*num):   #Utilizando o args
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")

'''n1 = int(input("Digite o primeiro número para soma:\n"))
n2 = int(input("Digite o segundo número para soma:\n"))'''

sum(5,18,10)

def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("Lista de Cursos:")
line = "*"
presentation(name="Python", category="Backend", level="iniciante")
print(line*50)
presentation(name="Dashboards com dash", category="Data Science", level="intermediário")
print(line*50)
presentation(name="Visão computacional com Python", category="IA", level="avançado")
