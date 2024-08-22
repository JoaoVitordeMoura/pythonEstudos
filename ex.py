#1

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
   

