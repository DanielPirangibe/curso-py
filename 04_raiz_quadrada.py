# Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.

numero = input("Digite um número para obter sua raiz quadrada:")
numero = int(numero)

raizquadrada = numero ** (1/2) # numero ** 0.5

print("A raiz quadrada de:", numero, "é:", raizquadrada)