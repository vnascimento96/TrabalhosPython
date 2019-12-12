# Aula 22 - 10/12/2019

# Somar numeros função for com numeros dinamicos

numero_inicial = int(input('Digite o primeiro numero: '))
numero_final = int(input('Digiter o segundo numero: '))

total = 0
for numero in range(numero_inicial, numero_final + 1):
    total += numero

print(f'Total: {total}')

#------------------------------------------------------------------------------------------#


texto = 'Ta legal, nosso proprio split, 3 textos em uma lista'

def nosso_split(txt,sep):

    

    result = []
    count = 0
    last_sep_pos = 0 
    for char in txt:
        if char == sep:
            result.append(txt[last_sep_pos:count])
            last_sep_pos = count + 1
            count +=1
        if last_sep_pos<len(txt[last_sep_pos:]):
            result.append(txt[last_sep_pos:])
        return result

print(nosso_split(texto, ','))




