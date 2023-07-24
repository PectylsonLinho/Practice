from math import(sin, cos, tan, radians)
display = '- Sin, Cos, Tan -'
print('')
print('{:|^20}'.format(display))

print('')

angle = float(input('Digite o ângulo: '))
convert = radians(angle)

print('')

print('O seno do ângulo é: {:.2f}'.format(sin(radians(angle))))
print('')
print('O cosseno do ângulo é: {:.2f}'.format(cos(radians(angle))))
print('')
print('A tangente do ângulo é: {:.2f}'.format(sin(convert)/cos(convert)))
'''OU'''
print('A tangente do ângulo é: {:.2f}'.format(tan(convert)))