# #1

# numero = int(input("Digite um número inteiro: "))

# if numero % 2 == 0:
#     print("Par")
# else:
#     print("Ímpar")

# #2

# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite outro número: "))

# if n1 < n2:
#     print(n1)
#     print(n2)
#     print(n2)
#     print(n1)
# else:
#     print(n2)
#     print(n1)
#     print(n1)
#     print(n2)


# #3

# x1 = int(input("Digite um número: "))
# x2 = int(input("Digite outro número: "))

# if x1 > x2:
#     print(x1, "é maior e" , x2 , "é menor")
# else:
#     print(x2, "é maior e" , x1 , "é menor")

# #4

# y1 = int(input("Digite o primeiro número: "))
# y2 = int(input("Digite o segundo número: "))
# y3 = int(input("Digite o terceiro número: "))

# if y1 < y2 < y3:
#     print(y1)
# elif y3 < y2 < y1:
#     print(y3)
# else:
#     print(y2)

# #5

# atacado = 10.90
# varejo = 12.90
# uni = int(input("Digite o tanto de unidades: "))

# if uni >= 20:
#     print(uni * atacado)
# else:
#     print(uni * varejo)

# #6

# a = int(input("Digite o primeiro número inteiro: "))
# b = int(input("Digite o segundo número inteiro: "))

# if a % b == 0:
#     print("É multiplo")
# else:
#     print("Não é multiplo")'''

# #7
 
# '''vogais = "a" or "A" and "e" or "E" and "i" or "I" and "o" or "O" and "u" or "U"
# letra = input("Digite uma letra: ")

# if letra == vogais:
#     print("Vogal")
# else:
#     print("Consoante")

# #8

# dia = int(input("Digite um dia de número: "))

# match dia:
#     case 1:
#         print("Domingo")
#     case 2:
#         print("Segunda")
#     case 3:
#         print("Terça")
#     case 4:
#         print("Quarta")
#     case 5:
#         print("Quinta")
#     case 6:
#         print("Sexta")
#     case 7:
#         print("Sábado")
#     case _:
#         print("Inválido")      


# #9

# #10

# morango = float(input("Digite a quantidade de morangos em kg: "))
# maca = float(input("Digite a quantidade de maçã em kg:  "))
# precoMaca1 = 8.80
# precoMorango1 = 19.50
# precoMaca2 = 7.50
# precoMorango2 = 15.20

# if morango <= 5 and maca > 5:
#     compra = (morango * precoMorango1) + (maca * precoMaca2)
#     if compra > 25:
#         print(compra - (compra * 0.10))
# elif maca <= 5 and morango > 5:
#     compra = (morango * precoMorango2) + (maca * precoMaca1)
#     if compra > 25:
#         print(compra - (compra * 0.10))
# elif maca and morango <= 5:
#     compra = (morango * precoMorango1) + (maca * precoMaca1)
#     if compra > 25:
#         print(compra - (compra * 0.10))
#     else:
#         print(compra)
# elif maca and morango > 5:
#     compra = (morango * precoMorango2) + (maca * precoMaca2)
#     if compra > 25:
#         print(compra - (compra * 0.10))
#     else:
#         print(compra)


# #11

# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))
# media = (n1 + n2) / 2

# if media >= 9:
#     conceito = "A"
#     if conceito == "A":
#         print("Nota 1:" , n1 , "Nota 2:" , n2 , "Média:" , media , "Conceito:" , conceito , "Resultado:" , "APROVADO")
# elif media >= 7.5:
#     conceito = "B"
#     if conceito == "B":
#         print("Nota 1:" , n1 , "Nota 2:" , n2 , "Média:" , media , "Conceito:" , conceito , "Resultado:" , "APROVADO")
# elif media >= 6:
#     conceito = "C"
#     if conceito == "C":
#         print("Nota 1:" , n1 , "Nota 2:" , n2 , "Média:" , media , "Conceito:" , conceito , "Resultado:" , "APROVADO")
# elif media >= 4:
#     conceito = "D"
#     if conceito == "D":
#         print("Nota 1:" , n1 , "Nota 2:" , n2 , "Média:" , media , "Conceito:" , conceito , "Resultado:" , "REPROVADO")
# elif media < 4:
#     conceito = "E"
#     if conceito == "E":
#         print("Nota 1:" , n1 , "Nota 2:" , n2 , "Média:" , media , "Conceito:" , conceito , "Resultado:" , "REPROVADO")
    

# #12

# numero = int(input("Digite um número inteiro e de três dígitos: "))
# n3 = numero % 10
# numero = numero // 10
# n2 = numero % 10
# numero = numero // 10
# n1 = numero

# if n1 < n2 < n3:
#     print("Crescente!")
# else:
#     print("Decrescente!")

# #laço de repetição

# for i in range(0 , 10):
#     print(i)

# s = "python"

# for s in str(s):
#     print(s)

# s = "python"

# for i, c in enumerate(s, 1):
#     print(i, c)

# x = int(input("Digite um número positivo: "))

# while x < 0:
#     x = int(input("Invalido, digite novamente: "))

# contador = 0

# while contador < 100:
#     print("Curso de python")
#     contador +=1
# print(contador)

# i = 0
# contador = 0

# while i < 10:
#     x = int(input("Digite um número: "))
#     if x >= 0:
#         contador += 1
#     i += 1    
# print(contador)

# s = "joao"

# for c in s:
#     if c == 'o':
#         continue
#     print(c)

# for i in range(10):
#     print(i)
# else:
#     print("Fim do laço")

# #ex laço de repetição

# #a
# for i in range(1 , 101):
#     print(i)

# #b
# for i in range(20 , 41):
#     print(i)

# #c

# soma = 0
# numero = 20

# while numero <= 40:
#     soma += numero
#     numero += 1
#     print(soma)

# #D

# soma1 = 0
# numero1 = -20

# while numero1 <= 10:
#     soma1 += numero1
#     numero1 += 1
#     print(soma1)

# #2A

# for i in range(1 , 51):
#     if i % 2 == 0:
    
#         print(i)
#     else:
#         continue

# #2B

# for i in range(50 , 100):
#     if i % 2 == 0:
#         continue
#     print(i)

# #2C

# for i in range(1 , 100):
#     if i % 3 == 0:
#         print(i)
#     else:
#         continue

# #2D

# for i in range(50 , 200):
#     if i % 7 == 0:
#         print(i)
#     else:
#         continue


# #3A

# soma = 0
# numero = 50

# while numero <= 150:
#     soma += numero
#     numero += 2
#     print(soma)

# #3B

# for i in range(1 , 101):
#     if i % 3 == 0:
#         print(i)
#     elif i % 5 == 0:
#         print(i)
#     else:
#         continue

# #3C

# x = 1

# for i , c in enumerate(1 , 500):
#     if i % 5 == 0:
#         print(i)

# 4A

# for i in range(0 , 11):
#     i = i * 2
#     print(i)

# 4B

# for i in range(0 , 11):
#     i = i * 5
#     print(i)

# 4C

# for i in range(0 , 11):
#     i = i * 7
#     print(i)

# 5

# s = "Paralelepipedo"

# for i, c in enumerate(s, 1):
#      print(i, c)

# 6

# a = "Curso"
# b = "Python"

# for i in range(1 , 11):
#     print(a)
#     print(b)

# 7

# nota = float(input("Digite uma nota: "))

# while nota < 0 or nota > 10:
#     nota = float(input("Digite novamente: "))

# print(nota)

# 8

# idadeNova = 200
# idadeVelha = 0
# idade = int(input("Idade (idade negativa termina a leitura)"))
# while idade > 0:
#     idade = int(input("Idade (idade negativa termina a leitura)"))
#     if idade < idadeNova:
#         idadeNova = idade
#     if idade > idadeVelha:
#         idadeVelha = idade
# print("Nova: " , idadeNova)
# print("Velha: ", idadeVelha)

# 9

# vogal = 0
# consoante = 0

# palavra = input("Digite uma palavra: ")
# for i in enumerate(palavra , 1):
#     if i == "a" or "e" or "i" or "o" or "u":
#         vogal += 1
#     else:
#         consoante += 1

# print(vogal , consoante)





# 10

# n = int(input("Digite um número inteiro: "))

# while n < 0:
#     n = int(input("Número inválido, digite novamente: "))

# fatorial = 1
# for i in range(1 , n + 1):
#     fatorial *= i
# print("O fatorial de" , n , "é" , fatorial)


#11

# n = int(input("Digite o tanto de interações para o cálculo: "))
# soma = 0

# while n < 0:
#     n = int(input("Digite novamente, o número tem que ser positivo: "))

# for i in range(1 , n + 1):
#     soma += 1/(i*(i + 1)/2)
# print(soma)

#12tent

# lucrototal = 0
# preco = 5.0

# for i in range(121):
#     lucro = (i * preco) - 200
#     if preco >= 1:
#         preco -= 0.5
        
# print(preco)
# print(lucro)

#12res

# preco = 5
# qtd = 120
# i = 1

# while preco >= 1:

#     lucro = qtd * preco - 200
#     print("Preço do ingresso:" , preco)
#     print("Quantidade de ingressos:" , qtd)
#     print("Lucro máximo:" , lucro)
#     preco = preco - 0.5
#     qtd = qtd + i*26

#13

# aprovado = 0
# reprovado = 0
# qtdaluno = 0
# mediaaprovado = 0
# mediarep = 0
# notageral = 0


# resp = int(input("Deseja ver a nota de um aluno?(1-Sim/2-Não): "))

# if resp != 1:
#     print("Obrigado até a próxima!")
# else:
#     while resp == 1:
#         if resp == 2:
#             break
#         qtdaluno += 1
#         n1 = float(input("Digite a nota da prova: "))
#         n2 = float(input("Digite a nota da atividade: "))

#         while n1 < 0 or n1 > 10:
#             n1 = float(input("Digite a nota da prova: "))
#         while n2 < 0 or n2 > 10:
#             n2 = float(input("Digite a nota da atividade: "))

#         media = (n1 + n2) / 2
#         print(media)

#         if media >= 7:
#             print("Aluno aprovado")
#             aprovado += 1
#             mediaaprovado += media
#             notageral += media
#         else:
#             print("Aluno reprovado")
#             reprovado += 1
#             mediarep += media
#             notageral += media

#         resp = int(input("Deseja ver a nota de mais um aluno?(1-Sim/2-Não): "))

#     print("Alunos aprovados:" , aprovado)
#     print("Alunos reprovados:" , reprovado)
#     perA = (aprovado * 100) / qtdaluno
#     perR = (reprovado * 100) / qtdaluno
#     print("Porcentagem de alunos aprovados: " , perA , "%")
#     print("Porcentagem de alunos reprovados: " , perR , "%")

#     if aprovado == 0:
#         mediaR = mediarep / reprovado
#         print("Média das notas dos reprovados:" , mediaR)
#     elif reprovado == 0:
#         mediaA = mediaaprovado / aprovado
#         print("Média das notas dos aprovados:" , mediaA)
#     else:
#         mediaA = mediaaprovado / aprovado
#         mediaR = mediarep / reprovado
#         print("Média das notas dos aprovados:" , mediaA)
#         print("Média das notas dos reprovados:" , mediaR)




#     mediaGeral = notageral / qtdaluno
#     print("Media geral dos alunos:" , mediaGeral)

#14

# n = int(input("Digite um número inteiro: "))
# m = n
# inverso = 0

# while n > 0:
#     inverso = inverso * 10 + n % 10
#     n = n // 10

# if inverso == m:
#     print("Palíndromo")
# else:
#     print("Não é palíndromo")

# def soma(n1 , n2):
#     s = n1 + n2
#     return s

# r = soma(2 , 3)
# print(r)

# def soma():
#     n1 = int(input("N1: "))
#     n2 = int(input("N2: "))
#     s = n1 + n2
#     return s
# print(soma())

# def calcSalario(salBase , valorH , qtdHoras):
#     salBase = int(input("Digite o salário base: "))
#     valorH = int(input("Digite o valor por hora extra: "))
#     qtdHoras = int(input("Digite a quantidade de horas extras: "))
#     salario = salBase + (valorH * qtdHoras)
#     return salario
# print(calcSalario(0 , 0 , 0))

#print(round(1/3 , 2))


import random
import math

# print(math.pi)
# print(round(math.sqrt(87) , 2))


# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))

# print(random.randint(n1 , n2))

# print(random.randint(1 , 20))

#exercicios função

#1

# def soma(*numeros):
#     soma = 0
#     for i in numeros:
#         soma += 1
#         return soma
# print(soma(1 , 2 , 3 , 4 , 5))

#2

# def media(numeros):
#     return sum(numeros) / len(numeros)
# l = [8 , 10 , 9]
# print(media(l))

#3

# def palindromo(s):
#     s = s.lower()
#     i = 0
#     j = len(s) - 1
#     while i < j:
#         if s[i] != s[j]:
#             return False
#         i = i + 1
#         j = j - 1
#     return True

# print(palindromo("Arara"))

#1

# def tam():
#     palavra = input("Digite uma palavra: ")
#     cont = 0
#     for i in palavra:
#         cont += 1
#     print("O tamanho da palavra é de:" , cont , "letras")
# tam()

# #2

# def mult():
#     a = input("Digite uma palavra: ")
#     n = int(input("Digite um número: "))
#     m = a * n
#     print(m)
# mult()

# def nome():
#     a = input("Digite seu nome completo: ").upper()
#     b = a.split()
#     iniciais = []
#     for i in b:
#         iniciais.append(i[0])    
#     c = "".join(iniciais)
#     print(c)
# nome()

def senha():
    s = input("Digite sua senha (ela precisa de 8 caracteres, pelo menos uma letra maiúscula e uma minúscula e conter pelo menos um número): ")
    tam = len(s)
    while tam < 8:
        s = input("Digite sua senha (ela precisa de 8 caracteres, pelo menos uma letra maiúscula e uma minúscula e conter pelo menos um número): ")
senha()


