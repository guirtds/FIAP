#solicite dois números ao usuário, sendo que o segundo deverá ser obrigatoriamente maior que o primeiro

numero1 = float(input("Digite um número:"))
numero2 = float(input("Digite outro número:"))

while numero2 <= numero1:
     print("O segundo número é menor que o primeiro.")
     numero2 = float(input(f"Digite um número maior que o {numero1}:"))

#solicite um número obrigatoriamente inteiro positivo, e calcular seu fatorial

numero_aleatorio = int(input("Digite um número inteiro positivo:"))
print(float(numero_aleatorio)//1==float(numero_aleatorio))



