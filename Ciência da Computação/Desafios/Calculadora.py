def soma(a,b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não é possivel divisão por zero"
    else:
        return a / b

historico = []

while True:
        
    try:

        print("----CALCULADORA DO ERYCK----\nDigite qual opção você quer")

        print("[0]Sair\n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\n[5]Histórico")

        selecionado =  int(input("Digite a opção desejada (Apenas o número da opção!): "))

        if selecionado == 1:
            print("Você selecionou soma, digite agora os números que você deseja somar.")
            numero1 = float(input("Primeiro número: "))
            numero2 = float(input("Segundo número: "))

            resultado = soma(numero1, numero2)

            print(f"[{numero1}]+[{numero2}]=[{resultado}]")
            historico.append(f"[{numero1}]+[{numero2}]=[{resultado}]")

        elif selecionado == 2:
            print("Você selecionou subtração, digite agora os números que você deseja subtrair.")
            numero1 = float(input("Primeiro número: "))
            numero2 = float(input("Segundo número: "))

            resultado = sub(numero1, numero2)

            print(f"[{numero1}]-[{numero2}]=[{resultado}]")
            historico.append(f"[{numero1}]-[{numero2}]=[{resultado}]")

        elif selecionado == 3:
            print("Você selecionou multiplicação, digite agora os numeros que você deseja multiplicar.")
            numero1 = float(input("Primeiro número: "))
            numero2 = float(input("Segundo número: "))

            resultado = multi(numero1, numero2)

            print(f"[{numero1}]x[{numero2}]=[{resultado}]")
            historico.append(f"[{numero1}]x[{numero2}]=[{resultado}]")

        elif selecionado == 4:
            print("Você selecionou divisão, digite agora os número que você deseja dividir.")
            numero1 = float(input("Primeiro número: "))
            numero2 = float(input("Segundo número: "))

            resultado = divisao(numero1, numero2)
            
            print(f"[{numero1}]/[{numero2}]=[{resultado}]")
            historico.append(f"[{numero1}]/[{numero2}]=[{resultado}]")

        elif selecionado == 5:
            print("Aqui está o seu histórico")

            for i in historico:
                print(i)

        elif selecionado == 0:
            print("Encerrando...")
            break

        else:
            print("Número digitado incorreto, tente novamente.")

        

    except ValueError:
        print("Você não digitou um numero, tente novamente.")
