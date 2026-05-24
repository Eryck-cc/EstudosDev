while True: 
    print("-------Sistema de Algoritmos-------")
    print("Bem-vindo, escreva de 1 até 8 o algoritmo o qual deseja selecionar")
    print("Caso deseje finalizar escreva Sair")
    print("Sistema1: Análise de Maior e Menor Valor em Lista\nSistema2: Separando Números Pares e Ímpares\nSistema3: Verificação de Número em Lista\nSistema4: Remoção de Elementos em uma Lista\nSistema5: Contagem de Positivos, Negativos e Zeros\nSistema6: Comparação entre Duas Listas\nSistema7: Sistema de Cadastro e Controle de Produtos\nSistema8: Ordenação e Classificação de Números Inteiros")
 
         

    algoritmo = (input("Digite o numero do sistema que deseja selecionar: "))

    if algoritmo == "1":

        lista1 = []

        for i in range(10):
            numerosinte = int(input("Digite 10 números inteiros, o sistema irá mostrar o maior e o menor: "))
            lista1.append(numerosinte)
        
        maximo = max(lista1)
        minimo = min(lista1)
        print(f"Os números digitados foram {lista1}")
        print(f"O maior número digitado foi {maximo}")
        print(f"O menor número digitado foi {minimo}")
    
    elif algoritmo == "2":

        lista2 = []
        
        for i in range(15):
            numerosinteiro = int(input("Digite 15 números inteiros o qual deseja armazenar na lista: "))
            lista2.append(numerosinteiro)
        
        listapar = []
        listaimpar = []

        for j in lista2:

            if j % 2 == 0:
                listapar.append(j)
            else:
                listaimpar.append(j)
        
        print(f"A lista com apenas números pares fica {listapar}")
        print(f"A lista com apenas números impares fica {listaimpar}")
    
    elif algoritmo == "3":
         
        lista3 = []

        for i in range(8):
            numerodigitado = int(input("Digite 8 números para serem adicionados a lista: "))
            lista3.append(numerodigitado)
        
        numerosolicitado = int(input("Digite um número inteiro: "))

        if numerosolicitado in lista3:
            print("Este número está presente na lista!")
        
        else: 
            print("Esse número não está presente na lista!")
    
    elif algoritmo == "4":

        lista4 = []

        for i in range(10):
            n = int(input("Digite 10 números inteiros para serem adicionados na lista: "))
            lista4.append(n)

        remocao = int(input("Digite um número para remover da lista: "))

        if remocao in lista4:
            
            quantidaderemo = lista4.count(remocao)

            for i in range(quantidaderemo):

                lista4.remove(remocao)
         
            print(f"A lista após a remoção é {lista4}")
        
        else: 
            print(f"Esse número não está na lista, sua lista ficou {lista4}")

    elif algoritmo == "5":
        lista5 = []
        positivo = 0
        negativo = 0
        zeros = 0

        for a in range(20):
            numerosintei = int(input("Digite 20 números inteiros tanto negativos ou positivos: "))
            
            if numerosintei > 0:
                positivo = positivo + 1
            elif numerosintei < 0:
                negativo = negativo + 1
            else:
                zeros = zeros + 1
        
        print(f"Fora digitados {positivo} números positivos; {negativo} números negativos e {zeros} números igual a zero!")
            
    elif algoritmo == "6":
        lista6 = [7, 11, 23, 36, 42]
        lista6_1 = [11, 5, 23, 36, 33]
        valorigual = []
        valordiferente = []
        valores = []

        print(f"Os valores que aparecem na primeira lista são {lista6} e na segunda {lista6_1}")

        for c in lista6:
            if c in lista6_1:
                valorigual.append(c)
            else:
                valordiferente.append(c)
        for d in lista6_1:
            if d in lista6:
                valorigual.append(d)
            else:
                valordiferente.append(d)

        print(f"Os valores iguais nas duas listas são: {valorigual}")
        print(f"Os valores diferentes nas duas listas são: {valordiferente}")

    elif algoritmo == "7":
        produto = ["Nome", "Preço", "Estoque"]


    elif algoritmo == "8":
        lista8 = []
        pares = 0
        impares = 0


        for e in range(12):
            valoress = int(input("Digite 12 valores para serem adicionados na lista: "))
            if valoress % 2 == 0: 
                pares = pares + 1
            else: 
                impares = impares + 1
        
        ordemcres = lista8.sort()
        ordemdecres = lista8.reverse()

        print(f"A lista em ordem crescente fica {ordemcres}")
        print(f"Em ordem descrescente fica {ordemdecres}")
        print(f"A lista possui {pares} números pares.")
        print(f"Possui {impares} numeros impar.")
        
    elif algoritmo == "Sair" or "sair":
        break
