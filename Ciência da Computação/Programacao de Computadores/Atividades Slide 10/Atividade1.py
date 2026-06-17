print("Cadastre a sua senha.")
print("A sua senha deve ter 6 caracteres exato.")
print("Deve ter letras e numeros")
print("Não deve contar as palavras 'FLA', 'MENGO' ou 'MENGAO'")
print("Não deve começar com a letra 'A' nem terminar com a letra 'F'")

senha = input("Digite a sua senha: ").upper()



def validarsenha(senha):
    if len(senha) != 6:
        print("Senha com menos ou mais de 6 caracteres")
    elif senha.isdigit():
        print("Senha com apenas numeros.")
        return False
    elif senha.isalpha():
        print("Senha com apenas letras.")
        return False
    elif "FLA" or "MENGO" or "MENGAO" in senha:
        print("Senha com palavras proibidas")
        return False
    elif senha.startswith("A"):
        print("Senha começou com A.")
        return False
    elif senha.endswith("F"):
        print("Senha terminou com F")
        return False
    return True

if validarsenha(senha):
    print("Senha invalida")

else:
    print("Senha valida")




        