#A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
#Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
#técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
#A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
#O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
#é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
#serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
#pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
#sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
#junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
#A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
#Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
#tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
#processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

#Requisitos:
#1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
#2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
#3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
#4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
#5 - Deve ser feito em Python

# Tripulação tecnica:
# 1 piloto
# 2 oficiais

# Tripulação de cabine:
# 1 Chefe de serviço 
# 2 2 comissárias 

# Tripulantes extras:
# 1 policial
# 1 presidiário

# 1 - Apresentar quanto tempo ele vai levar para chegar do terminal até o avião
# 2 - Após efetuar o embarque apresentar quem se encontra no avião
# 3 - Após entrar no carrinho para ir ao avião apresentar quem esta no terminal para a proxiima viagem
# 4 - Após chegar no avião apresentar quem está no avião



# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. 
# 
# A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

from funcoes import *

aviao = []
terminal = ['Oficial 1','Oficial 2', 'Comissaria 1', 'Comissaria 2', 'Chefe', 'Policial', 'Presidiário', 'Piloto']

# Oficial 1 e Piloto
primeira_viagem (aviao, terminal)

# Oficial 2 e Piloto
segunda_viagem (aviao, terminal)

# Comissaria 1 e Chefe
terceira_viagem (aviao, terminal)

# Comissaria 2 e Chefe
quarta_viagem (aviao, terminal)

# Chefe e piloto
quinta_viagem (aviao, terminal)

# Policial e Presidiário
sexta_viagem (aviao, terminal)

# Piloto e Chefe
setima_viagem (aviao, terminal)