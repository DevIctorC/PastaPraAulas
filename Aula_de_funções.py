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