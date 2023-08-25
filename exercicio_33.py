# Estruturas Condicionais
# Mostrando o 'Maior' e 'Menor' de 3 números digitados

panel = ' Analizando \'Maior e Menor\' de 3 numeros '
print(f'{panel:=^55}')

maior = int()
menor = int()
number = [0, 1, 2]
count = int(1)

while count <= 3:
    number[count-1] = int(input(f'Digite o {count}º numero: '))
    count += 1

count = 1
while count <= 3:

    if number[count-1] >= maior:
        maior = number[count-1]
    else:
        menor = number[count-1]
    count += 1

print(f"""
      O maior número digitado é: {maior}
      O menor número digitado é: {menor}
""")