dias_mes = {
    1: 31
    2: 28
    3: 31
    4: 30
    5: 31
    6: 30
    7: 31
    8: 31
    9: 30
    10: 31
    11: 30
    12: 31
}

print(sum(list(dias_mes.values())[qual_mes-1:]))

total = 0
for mes in range(qual_mes, 12+1):
    total += dias_mes[mes]

print('total de dias para o finall do ano ', total)