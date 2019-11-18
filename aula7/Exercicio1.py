#Exercicio 1 - Dicionario
#Escreva programa que lia os dados de cerveja 
#Cerveja: Marca, Tipo, IBU, ABV, EBC, Volume
#Imprima os dados do dicionario (não dicionario completo)




marca = input('Digite o nome da cerveja: ')
tipo = input('Digite o tipo dela: ')
ibu = int(input('Digite o IBU: '))
abv = float(input('Digite o ABV: '))
ebc = float(input('Digite o EBC: '))
volume = int(input('Digite o volume: '))

dicionario_cerveja = {'Marca': marca, 'Tipo': tipo, 'IBU': ibu, 'ABV': abv, 'EBC': ebc, 'Volume': volume}

print(f'{dicionario_cerveja["Marca"]} - {dicionario_cerveja["Tipo"]} - {dicionario_cerveja["IBU"]} - {dicionario_cerveja["ABV"]} - {dicionario_cerveja["EBC"]} - {dicionario_cerveja["Volume"]}')

