

nome = input('Digite seu nome: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))


mediaFinal = (nota1 + nota2 + nota3 + nota4) / 4

print(f'Aluno: {nome} Média Final: {mediaFinal} \t')

maior = 0
if nota1 >= nota2 and nota1 >= nota3 and nota1 >= nota4:
    maior = nota1

elif nota2 >= nota1 and nota2 >= nota3 and nota2 >= nota4:
    maior = nota2

elif nota3 >= nota1 and nota3 >= nota2 and nota3 >= nota4:
    maior = nota3

elif nota4 >= nota1 and nota4 >= nota2 and nota4 >= nota3:
    maior = nota4 

print(f'Maior nota {maior}')

menor = 0
if nota1 <nota2 and nota1 < nota3 and nota1 < nota4:
    menor = nota1

elif nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    menor = nota2
elif nota3 < nota1 and nota3 < nota2 and nota3 < nota4:
    menor = nota3

elif nota4 < nota1 and nota4 < nota2 and nota4 < nota3:
    menor = nota4     

print(f'Menor nota: {menor}')  


if mediaFinal >= 7.0 and mediaFinal <=10:
    print('Parabens, você foi aprovado')
elif mediaFinal < 7:
    print('Reprovado, estude mais.')

else:
    print('Média invalida, escreva suas notas corretamente')    


 
     