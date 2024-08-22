'''#1

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")

#2

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 < n2:
    print(n1)
    print(n2)
    print(n2)
    print(n1)
else:
    print(n2)
    print(n1)
    print(n1)
    print(n2)


#3

x1 = int(input("Digite um número: "))
x2 = int(input("Digite outro número: "))

if x1 > x2:
    print(x1, "é maior e" , x2 , "é menor")
else:
    print(x2, "é maior e" , x1 , "é menor")

#4

y1 = int(input("Digite o primeiro número: "))
y2 = int(input("Digite o segundo número: "))
y3 = int(input("Digite o terceiro número: "))

if y1 < y2 < y3:
    print(y1)
elif y3 < y2 < y1:
    print(y3)
else:
    print(y2)

#5

atacado = 10.90
varejo = 12.90
uni = int(input("Digite o tanto de unidades: "))

if uni >= 20:
    print(uni * atacado)
else:
    print(uni * varejo)

#6

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))

if a % b == 0:
    print("É multiplo")
else:
    print("Não é multiplo")'''

#7

str 
vogais = "a" and "A" or "e" and "E" or "i" and "I" or "o" and "O" or "u" and "U"
letra = str(input("Digite uma letra: "))

if letra == vogais:
    print("Vogal")
else:
    print("Consoante")

#8

dia = int(input("Digite um dia de número: "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Inválido")                 
   

