from calculo2 import*


investimento = float(input('Digite o quanto você investiu: '))
taxa = float(input('Digite a taxa de rentabilidade mensal do seu investimento: '))
taxa = taxa / 100
numeses = int(input('Digite o numero de meses aplicados: '))

jurosFinal = jurosCompostos(investimento, taxa, numeses)
porc_final = (porc(jurosFinal, investimento))

print(f'Sua rentabilidade é de : R$ {jurosFinal} Seu lucro foi de : % {porc_final}')