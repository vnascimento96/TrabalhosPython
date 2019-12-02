def criar_faixa(musica, artista, album):
    faixa = {'musica': musica, 'artista': artista, 'album': album}
    return faixa

def salvar_faixa(faixa):
    arquivo = open('aula16/faixas.txt', 'a')
    arquivo.write(f'{faixa["musica"]};{faixa["artista"]};{faixa["album"]}\n')
    arquivo.close()

def ler_faixa():
    arquivo = open('aula16/faixas.txt', 'r')
    lista_faixas = []
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        faixa = criar_faixa(lista_linha[0], lista_linha[1], lista_linha[2])
        lista_faixas.append(faixa)
    arquivo.close()
    return lista_faixas




