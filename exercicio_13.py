# Operadores Aritméticos
# Reajuste de Salario

salario = float(input('Digite o salário do funcionário: '))

print("""
      O salário do funcianário é: {:.2f} kz,
      e com o aumento de 15% passara a receber: {:.2f} kz
      """.format(salario, salario + (salario*(15/100)))
)