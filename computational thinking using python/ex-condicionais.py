#EXERCÍCIO

'''
utilizando apenas if e else, faça um programa que peça a idade sua e de um colega e
seus respectivos nomes, e diga, colocando os nomes nas respostas:
1) se seus nomes possuem a mesma quantidade de letras
2) quantos porcento a idade do mais velho representa da idade do mais novo,
limitando a resposta a 1 casa decimal E
a) se a pessoa mais velha é maior de idade
b) se a pessoa mais nova é uma criança (possui menos de 12 anos)
3) para cada pessoa, diga:
a) se ela for maior de idade, se ela já se aposentou OU quanto tempo falta para se aposentar
(assumindo que a idade de aposentadoria é 75 anos);
b) se ela for menor de idade, qual sua idade em meses

OBS: criem casos de teste para todas as possibilidades que vocês identificarem
'''

nome_usuario = input ("Digite seu nome:")
nome_colega = input ("Digite o nome do seu colega:")
idade_usuario = float(input("Diga sua idade {}:" .format(nome_usuario)))
idade_colega = float(input("Diga a idade de {}" .format(nome_colega)))

#Exercício 1


diff = len(nome_usuario) - len(nome_colega)
print(diff)


# if len(nome_usuario) == len(nome_colega):
#     print("A diferenca de letras é nula")
# else:
#     print("Os nomes não possuem o mesmo número de caracteres")

    #Exercício 2






