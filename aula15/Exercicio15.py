# Pedir os dados da cerveja

marca = input('Digite a marca da cerveja: ')
teor = float(input('Teor alcoólico: '))
tipo = input('Digite o tipo da cerveja: ')

# Salvar os dados em um metodo

def salvar_dados(cerveja_dicionario):
    arquivo = open('exercicio15.txt', 'a')
    arquivo.write(f"{cerveja_dicionario['marca']};{cerveja_dicionario['teor']};{cerveja_dicionario['tipo']}\n")
    arquivo.close()

# Ler os dados e apresentar na tela.
def ler_dados():
    lista = []
    arquivo = open('exercicio15.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja = {'marca': lista_linha[0], 'teor': lista_linha[1], 'tipo': lista_linha[2]}
        lista.append(cerveja)
    arquivo.close()
    return lista

# criação da variável para apresentação do dado e chamando o metodo onde salva.
cerveja = {'marca': marca, 'teor': teor, 'tipo': tipo}
salvar_dados(cerveja)

# Apresentando o dado na tela linha por linha.
for p in ler_dados():
    print(f"Marca: {p['marca']} Teor Alcoólico: {p['teor']} Tipo da cerveja: {p['tipo']}")

