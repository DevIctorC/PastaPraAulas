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

"""Coleta de informações! e teste com fatiamento e fstrings"""

user_name = input("Digite seu nome: ")
user_idade = input("Digite sua idade: ")

if user_idade and user_idade:
    print(f'Ola {user_name} seu nome invertido fica:',user_name[::-1],)

    if ' ' in user_name:
        print("Seu nome contem espaços! ")
    else:
        print("Seu nome nao tem espaços! ")

    print(f"seu nome contem {len(user_name)} letras contando com espaços!")

    print(f"a primeira letra do seu nome é:", user_name[0], "/e a ultima letra é:", user_name[-1] )

else:
    print("Nada foi digitado no prompt! ")