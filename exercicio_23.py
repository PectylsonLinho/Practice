# Separando Dígitos de um número!

header = 'read a number, range(0- 9999)'
print('{:=^40}'.format(header))

number = int(input('Digite um numero: '))
num = number // 1 % 10
num1 = number // 10 % 10
num2 = number // 100 % 10
num3 = number // 1000 % 10
print('Analisando o valor!')
print('''
       Unidade: {}
       Dezena:  {}
       Centena: {}
       Milhar:  {}
'''.format(num, num1, num2, num3))
