# Pedir salario, nome completo, cpf, rg, cargo
# Deve ser calculado o valor do IRRF



from calculoImposto import calculo_inss, calculo_irrf


print('='*50, '\n')



salario = float(input('Digite o salario: '))


inss = calculo_inss(salario)
irrf = calculo_irrf(salario, inss)

salario_liquido = salario - inss - irrf

print(f'INSS: {inss}')
print(f'IRRF: {irrf}')
print(f'Seu salário liquido é {salario_liquido}')

print ('\n' * 2, '='*50)