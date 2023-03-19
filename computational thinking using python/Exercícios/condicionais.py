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
idade_usuario = float(input("Diga sua idade {}:" .format(nome_usuario)))
nome_colega = input ("Digite o nome do seu colega:")
idade_colega = float(input("Diga a idade de {}:" .format(nome_colega)))

#Exercício 1
#diferenca_de_letras = len(nome_usuario) - len(nome_colega)
#print("A diferença de letras entre os nomes é de {} caracteres." .format(diferenca_de_letras))


if len(nome_usuario) == len(nome_colega):
     print("A diferenca de letras é nula.")
else:
     print("Os nomes não possuem o mesmo número de caracteres.")

#Exercício 2 quantos porcento a idade do mais velho representa da idade do mais novo,
#limitando a resposta a 1 casa decimal

pessoa_mais_velha = idade_usuario - idade_colega

if pessoa_mais_velha > 0:
    print(f"{nome_usuario} é mais velho.")

else:
    print(f"{nome_colega} é mais velho>")

porcentagem_entre_idade = ( / ) * 100

print(f"A idade do usuário representa {porcentagem_entre_idade:.1f} % em relação a idade do colega.")

#a) se a pessoa mais velha é maior de idade
#b) se a pessoa mais nova é uma criança (possui menos de 12 anos)











    






