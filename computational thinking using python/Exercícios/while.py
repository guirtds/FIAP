#solicite dois números ao usuário, sendo que o segundo deverá ser obrigatoriamente maior que o primeiro

# numero1 = float(input("Digite um número:"))
# numero2 = float(input("Digite outro número:"))

# while numero2 <= numero1:
#      print("O segundo número é menor que o primeiro.")
#      numero2 = float(input(f"Digite um número maior que o {numero1}:"))

#faça um programa que imprima a soma dos números inteiros positivos de 1 a 100,
#e realize este exercício utilizando primeiramente "for", e depois "while"

soma = 0

for i in range (1,101):
     soma += i

print("A soma dos números inteiros positivos de 1 a 100 é {}." .format(soma))

#utilizando "while"

contador = 1
soma_while = 0

while contador <= 100:
      soma_while += contador
      
print("A soma dos números inteiros positivos de 1 a {} é {}." .format(contador, soma_while))

# imprima a tabuada do número 5, de 0 a 10, inclusive
# depois, adapte o programa para receber dois números do usuário: o de início e o de fim, utilize o "for" e "while"

n1 = float(input("Diga um número inteiro para o início da tabuada:"))
n2 = float(input("Diga um número inteiro para o final da tabuada:"))

while n1!=int(n1):
    n1 = float(input("Diga um número inteiro para o início da tabuada:"))

while True:
      n1 = float(input("Diga um número inteiro para o início da tabuada:"))





