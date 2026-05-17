i = 0

while True:

    try:
      
        numero = int(input("Digite um número inteiro: "))
      
        if numero > 0:
            i = i + 1
            
        elif numero <= 0:
            print("Você digitou um número neutro ou negativo!")

        parar = input("Caso deseje finalizar o programa e mostrar o resultado digite stop, caso não deseje digite continuar: ")
        if parar == "stop":
            print(f"Voçê digitou {i} números positivos!")
            break


    except ValueError:
       print("Você digitou uma letra, tente novamente")
