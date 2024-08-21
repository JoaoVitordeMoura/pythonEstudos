#1

print("Olá mundo")

#2

n1 = int(input("Digite o 1° número:"))
n2 = int(input("Digite o 2° número:"))
n3 = int(input("Digite o 3° número:"))
resultado = n1 + n2 + n3
print(resultado)

#3

fruta = input("Digite o nome de uma fruta: ")
print("A fruta digitada foi:", fruta)

#4

km = float(input("Digite a distância da cidade: "))
print (km * 1000)

#5

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(media)

#6

lado = float(input("Digite um lado do quadrado: "))
area = lado ** 2
print(area)

#7

raio = float(input("Digite um valor para o raio: "))
areaCirculo = raio * (3.14 ** 2)
print(areaCirculo)

#8

fahrenheit = float(input("Digite uma temperatura: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print(celsius)

idade = int(input("Digite uma idade: "))
if idade < 12:
    print("Criança")
else:
    if 12 <= idade < 18:
        print("Adolescente")
    else:
        print ("Adulto")

status = 400
match status:
    case 400:
        print("bad request")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _:
        print("Erro desconhecido")

nota = 7
frequencia = 88
if nota >= 5 and frequencia >= 75:
    print("Aprovado")
else:
    print("Reprovado")        

dia = 'Sábado'
if dia == 'Sábado' or dia == 'Domingo':
    print("Fim de semana")
else:
    print("Dia de semana")



        