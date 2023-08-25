# Estruturas Condiçionais
# Ano Bissesto

# Formatando um header
panel = ' Calculo de Ano Bissexto '
print(f'{panel:=^35}')

# Calculo de Ano de Bissesto |&| import date time for call the actualy date
from datetime import date

years = int(input('Type to verify the year > U < type 0-Show actualy year: '))
if years == 0:
    years = date.today().year
if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
    print(f'O ano de {years} é Bissexto!')
else:
    print(f'O ano de {years}, não é Bissexto!')