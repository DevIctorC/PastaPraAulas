"""Calculo do IMC"""
nome = 'Jcolobri'
altura = 1.69
peso = 54
calc_IMC = peso / (altura*altura)
print(f'nome:{nome}, altura:{altura}', end=' ')
print(f'peso:{peso} e seu calculo do IMC é: {calc_IMC:.2f} ')
print(f'{peso:.2f}')

"""COMPARANDO VALORES! """
valor1 = input("Digite um valor: ")
valor2 = input("Digite um valor: ")
if valor1 > valor2:
    print(f"O primeiro valor digitado: {valor1} é maior que o segundo: {valor2}")
else:
    print(f'O segundo valor digitado: {valor2} é maior que o primeiro: {valor1}')