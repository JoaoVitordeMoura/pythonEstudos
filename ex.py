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
 
vogais = "a" and "A" or "e" and "E" or "i" and "I" or "o" and "O" or "u" and "U"
letra = input("Digite uma letra: ")

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


#9

#10

morango = float(input("Digite a quantidade de morangos em kg: "))
maca = float(input("Digite a quantidade de maçã em kg:  "))
precoMaca1 = 8.80
precoMorango1 = 19.50
precoMaca2 = 7.50
precoMorango2 = 15.20

if maca and morango <= 5:
    compra = (morango * precoMorango1) + (maca * precoMaca1)
    if compra > 25:
        print(compra - (compra * 0.10))
    else:
        print(compra)
elif maca and morango > 5:
    compra = (morango * precoMorango2) + (maca * precoMaca2)
    if compra > 25:
        print(compra - (compra * 0.10))
    else:
        print(compra)
elif morango <= 5:
    compra = (morango * precoMorango1) + (maca * precoMaca2)
    if compra > 25:
        print(compra - (compra * 0.10))
elif maca <= 5:
    compra = (morango * precoMorango2) + (maca * precoMaca1)
    if compra > 25:
        print(compra - (compra * 0.10))


#11

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2

if media >= 9:
    conceito = "A"
    if conceito == "A":
        print("Nota 1:" , n1 , "Nota 2:" , n2 , "Média:" , media , "Conceito:" , conceito , "Resultado:" , "APROVADO")
elif media >= 7.5:
    conceito = "B"
    if conceito == "B":
        print("Nota 1:" , n1 , "Nota 2:" , n2 , "Média:" , media , "Conceito:" , conceito , "Resultado:" , "APROVADO")
elif media >= 6:
    conceito = "C"
    if conceito == "C":
        print("Nota 1:" , n1 , "Nota 2:" , n2 , "Média:" , media , "Conceito:" , conceito , "Resultado:" , "APROVADO")
elif media >= 4:
    conceito = "D"
    if conceito == "D":
        print("Nota 1:" , n1 , "Nota 2:" , n2 , "Média:" , media , "Conceito:" , conceito , "Resultado:" , "REPROVADO")
elif media < 4:
    conceito = "E"
    if conceito == "E":
        print("Nota 1:" , n1 , "Nota 2:" , n2 , "Média:" , media , "Conceito:" , conceito , "Resultado:" , "REPROVADO")
    




