num1 = int(input('Digite o primeiro numero:\n'))
num2 = int(input('Digite o segundo numero:\n'))

# Aritimeticos
sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2
exp = num1 ** num2

print(f'Soma: {sum}\n'
      f'Subtracao: {sub}\n'
      f'Multiplicacao: {mult}\n'
      f'Divisao: {div}\n'
      f'Modulo: {mod}\n'
      f'Expoente: {exp}\n'
      )

print('=====================================')

print(f'A soma de {num1} e {num2} da o resultado de {sum}, a subtracao: {sub}, a multiplicacao: {mult}, dividindo da o valor de: {div}, o restante do modulo da divisao: {mod} e seu respectivo expoente é: {exp}')

print('=====================================')

# Comparacao

bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2

print(f'\n{bigger},\n {smaller},\n {equal},\n {different}.')

# Atribuicao

num1 += 1 #num1 = num1 + 1
num1 -= 1 #num1 = num1 - 1
num1 *= 1 #num1 = num1 * 1
num1 /= 1 #num1 = num1 / 1