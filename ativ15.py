# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

num1 = float(input("digite o primeiro numero"))
num2 = float(input("digite o segundo numero"))

operaçao = imput("digite a operaçao que deseja ultilizar; soma, multiplicar, subtrair ,dividir")

if operaçao == "soma":
    print(num1 + num2)
elif operaçao == "multiplicaçao":
    print(num1 * num2)
elif operaçao == "subtraçao":
    print(num1 -num2)
    if operaçao == "divisao":
        print(num1 / num2)
