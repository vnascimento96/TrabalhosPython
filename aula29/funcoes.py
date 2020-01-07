def primeira_viagem (aviao, terminal):
    print('-'*150)
    print(f"""\nTERMINAL: {str(terminal).strip('[]').replace("'","")}\n""")
    print(f"O Oficial 1 entrou no Smart Fortwo dirigido pelo Piloto.")
    input(f'Tecle ENTER para que o Smart Fortwo leve-os até o avião -----> ')
    input('O Smart Fortwo chegou ao seu destino! Tecle ENTER para que ele volte e possa levar mais pessoas ao avião -----> ')
    aviao.append(terminal.pop(0))
    print(f"""\nAVIÃO: {str(aviao).strip('[]').replace("'", "")}\n""")


def segunda_viagem (aviao, terminal):
    print('-'*150)   
    print(f"""\nTERMINAL: {str(terminal).strip('[]').replace("'","")}\n""")
    print(f"O Oficial 2 entrou no Smart Fortwo dirigido pelo Piloto.")
    input(f'Tecle ENTER para que o Smart Fortwo leve-os até o avião -----> ')
    input('O Smart Fortwo chegou ao seu destino! Tecle ENTER para que ele volte e possa levar mais pessoas ao avião -----> ')
    aviao.append(terminal.pop(0))
    print(f"""\nAVIÃO: {str(aviao).strip('[]').replace("'", "")}\n""")


def terceira_viagem (aviao, terminal):
    print('-'*150)
    print(f"\nO Piloto volta e deixa o Smart Fortwo no terminal!\n") 
    print(f"""\nTERMINAL: {str(terminal).strip('[]').replace("'","")}\n""")
    print(f"A Comissaria 1 entrou no Smart Fortwo dirigido pelo Chefe de Bordo.")
    input(f'Tecle ENTER para que o Smart Fortwo leve-os até o avião -----> ')
    input('O Smart Fortwo chegou ao seu destino! Tecle ENTER para que ele volte e possa levar mais pessoas ao avião -----> ')
    aviao.append(terminal.pop(0))
    print(f"""\nAVIÃO: {str(aviao).strip('[]').replace("'", "")}\n""")


def quarta_viagem (aviao, terminal):
    print('-'*150)
    print(f"""\nTERMINAL: {str(terminal).strip('[]').replace("'","")}\n""")
    print(f"A Comissaria 2 entrou no Smart Fortwo dirigido pelo Chefe de Bordo.")
    input(f'Tecle ENTER para que o Smart Fortwo leve-os até o avião -----> ')
    input('O Smart Fortwo chegou ao seu destino! Tecle ENTER para que ele volte e possa levar mais pessoas ao avião -----> ')
    aviao.append(terminal.pop(0))
    print(f"""\nAVIÃO: {str(aviao).strip('[]').replace("'", "")}\n""")


def quinta_viagem (aviao, terminal):
    print('-'*150)
    print(f"""\nTERMINAL: {str(terminal).strip('[]').replace("'","")}\n""")
    print(f"O Chefe de Bordo entrou no Smart Fortwo dirigido pelo Piloto.")
    input(f'Tecle ENTER para que o Smart Fortwo leve-os até o avião -----> ')
    input('O Smart Fortwo chegou ao seu destino! Tecle ENTER para que ele volte e possa levar mais pessoas ao avião -----> ')
    aviao.append(terminal.pop(0))
    print(f"""\nAVIÃO: {str(aviao).strip('[]').replace("'", "")}\n""")


def sexta_viagem (aviao, terminal):
    print('-'*150)
    print(f"\nO Piloto volta e deixa o Smart Fortwo no terminal!\n")
    print(f"""\nTERMINAL: {str(terminal).strip('[]').replace("'","")}\n""")
    print(f"O Presidiário entrou no Smart Fortwo dirigido pelo Policial.")
    input(f'Tecle ENTER para que o Smart Fortwo leve-os até o avião -----> ')
    input('O Smart Fortwo chegou ao seu destino! Tecle ENTER para que o CHEFE volte e possa levar mais pessoas ao avião -----> ')
    aviao.append(terminal.pop(0))
    aviao.append(terminal.pop(0))
    print(f"""\nAVIÃO: {str(aviao).strip('[]').replace("'", "")}\n""")


def setima_viagem (aviao, terminal):
    print('-'*150)
    print(f"\nO Chefe de Bordo volta e deixa o Smart Fortwo no terminal")
    terminal.append(aviao.pop(4))
    print(f"""\nTERMINAL: {str(terminal).strip('[]').replace("'","")}\n""")
    print(f"O Piloto entrou no Smart Fortwo dirigido pelo Chefe de Bordo.")
    input(f'Tecle ENTER para que o Smart Fortwo leve-os até o avião -----> ')
    print('O Smart Fortwo chegou ao seu destino com todos os passageiros embarcados no avião!')
    aviao.append(terminal.pop(0))
    aviao.append(terminal.pop(0))
    print(f'\nTERMINAL: Ninguém')
    print(f"""AVIÃO: {str(aviao).strip('[]').replace("'", "")}\n""")
    print('-'*150)