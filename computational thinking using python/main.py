#primeiro input
media_km_por_dia = float(input("Diga sua média de km rodados por dia útil: "))

#dados vindos do programa anterior
autonomia_em_km_por_L = 15

#calculando dados intermediários
media_km_mensal = media_km_por_dia * 20
media_litros_por_mes = media_km_mensal/autonomia_em_km_por_L

#segundo input
preco_por_litro = float(input("Diga quanto você pagou em reais por litro de gasolina:"))

valor_gasto_mensal = media_litros_por_mes * preco_por_litro

print("Você gasta, em média, por mês {:.2f} R$ com combustível".format(valor_gasto_mensal))



# calcular o menor número de notas necessárias para pagar este custo mensal
#ainda falta descobrir o quanto o troco importa
#completar o problema utilizando moedas para chegar no valor

print("Qual o menor número de notas para pagar o valor de R${}?" .format((valor_gasto_mensal15)))


#Estruturas Condicionais - Simples (if/else)

idade_julio = 30
idade_julia = 40

if idade_julio > idade_julia:
    print("Você é um bbzao!")
else:
    print("Você é um idoso!")

#Receber 4 notas escolares, calcular a média do estudante, se a média for maior que 7,5 msg "aprovado!", entre 5 e 7,4 recuperação e abaixo de 5 reprovado

n1 = float(input("Digite a nota de sua prova:"))
n2 = float(input("Digite a nota de sua prova:"))
n3 = float(input("Digite a nota de sua prova:"))
n4 = float(input("Digite a nota de sua prova:"))
media = (n1 + n2 + n3 + n4)/4

if media >= 7.5:
    print("Aprovado!")

if media >=5 and media <= 7.4:
    print("Você está de recuperação!")

if media <=4.9:
    print("Reprovado!")



