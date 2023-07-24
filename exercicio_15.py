layer = "ALUGUEL DE CARRO"
print('{:=^60}'.format(layer))

km = float(input('Digite a quantidade de km percorrido: '))
dia = int(input('Digite o numero de dias: '))
valorPago = (dia*60) + (km*0.15)
print('O valor a ser pago é: {:.2f} kz'.format(valorPago)) 