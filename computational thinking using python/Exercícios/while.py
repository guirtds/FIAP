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






