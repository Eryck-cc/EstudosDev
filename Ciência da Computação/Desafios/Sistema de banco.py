'''🚀 Desafio Python #007 — Sistema de Banco

Você vai criar um pequeno caixa eletrônico.

Objetivo

O saldo inicial da conta é:

saldo = 1000

O programa deve mostrar um menu:

===== BANCO =====

1 - Ver saldo
2 - Depositar
3 - Sacar
4 - Extrato
5 - Sair

O menu deve aparecer várias vezes usando while True.

Opção 1

Mostra:

Seu saldo é R$ 1000.00
Opção 2

Pergunta:

Quanto deseja depositar?

Se o valor for maior que zero:

adiciona ao saldo
salva essa operação no extrato

Exemplo:

+ R$200
Opção 3

Pergunta:

Quanto deseja sacar?

Regras:

não pode sacar valor negativo
não pode sacar mais do que possui
caso contrário, diminui do saldo

Salve no extrato:

- R$150
Opção 4

Mostra todas as operações feitas.

Exemplo:

Extrato

+ R$300
- R$100
+ R$50

Saldo atual: R$1250

Se não houver movimentações:

Nenhuma movimentação encontrada.
Opção 5

Encerra o programa.

Requisitos
while
if
try/except
listas
funções (crie pelo menos 3)
menu
⭐ Bônus 1

Não permita depósitos ou saques iguais a zero.

⭐⭐ Bônus 2

Mostre o total de depósitos e o total de saques.

Exemplo:

Total depositado: R$800

Total sacado: R$350
⭐⭐⭐ Bônus 3

Adicione um sistema de login antes de entrar no banco.

Exemplo:

Usuário:
Senha:

O usuário terá apenas 3 tentativas.

Se errar as três:

Conta bloqueada.
🔥 Bônus Mestre

Implemente uma opção extra:

6 - Transferência

Pergunte o nome do destinatário e o valor da transferência. Verifique se há saldo suficiente, atualize o saldo e registre a operação no extrato.'''

saldo = 1000.00
extrato = {"Deposito": [],
           "Saque": [],
           "Transferência": []
}
totalsacado = 0
totaldepositado = 0
acessos = {"Usuários": [],
           "Senhas": []
}


def validar_login(usuario,senha):
    if usuario in acessos["Usuários"] and senha in acessos["Senhas"]:
        print("Login validado com sucesso, bem-vindo")
        return 200
    else:
        print("Login incorreto, tente novamente!")
        return 401


def depositar(deposito, saldo, totaldepositado):
    if deposito <= 0:
        return "Quantidade zero ou negativo para depositar, tente novamente"
    else:
        saldo = deposito + saldo
        extrato["Deposito"].append(deposito)
        totaldepositado = totaldepositado + deposito
        return saldo
        
    
def sacado(sacar, saldo, totalsacado):
    if sacar <= 0:
        return "Não é possível sacar um valor negativo ou zero, tente novamente!"
    elif sacar > saldo:
        return "Não é possível sacar um valor maior que o seu saldo, tente novamente!"
    else:
        saldo = saldo - sacar
        extrato["Saque"].append(sacar)
        print(f"R${sacar} sacado com sucesso!")
        totalsacado = totalsacado + sacar
        return saldo, totalsacado
    
def transferido(transferir,saldo):
    if transferir <= 0:
        return "Não é possivel transferir um valor negativo ou zerado, tente novamente!"
    elif transferir > saldo:
        return "Não é possivel transferir um valor maior que seu saldo, tente novamente!"
    else:
        saldo = saldo - transferir
        print(f"R${transferir} transferido com sucesso!")
        extrato["Transferência"].append(transferir)
        return transferir, saldo
    
#DASHBOARD
while True:
    try:
        print("Bem-vindo\n1 - Cadastro\n2 - Login")
        opcaoescolhida = int(input("Digite a opção que deseja: "))

    except ValueError:
        print(f"Digite apenas opção válida, tente novamente!")
        continue

    if opcaoescolhida == 1: 
    #CADASTRO
        while True:
            try:
                print("===== CADASTRO DE USUARIO=====")
                usuario = input("Digite um nome de usuario para cadastro: ")
                senha = int(input("Digite uma senha parada cadastro (Apenas números inteiros): "))
                acessos["Senhas"].append(senha)
                acessos["Usuários"].append(usuario)
                break
            except ValueError:
                print("A senha deve conter apenas números inteiros, tente novamente!")
                continue

    if opcaoescolhida == 2:
        #LOGIN
        while True:
            try:
                print("=====LOGIN=====")
                usuario = input("Digite seu nome de usuario: ")
                senha = int(input("Digite sua senha: "))
                validacao = validar_login(usuario, senha)
                if validacao == 200:
                    while True:
                        try:
                            print("===== BANCO =====\n1 - Ver saldo\n2 - Depositar\n3 - Sacar\n4 - Extrato\n5 - Ver total depositado\n6 - Ver total sacado\n7 - Transferir\n8 - Sair")
                            opcao = int(input("Selecione sua opção: "))
                            if opcao == 1:
                                print(f"Seu saldo é: R${saldo}")
                            elif opcao == 2:
                                deposito = float(input("Digite quanto você deseja depositar: R$"))
                                saldo = depositar(deposito, saldo, totaldepositado)
                                print(f"R${deposito} depositado com sucesso")
                            elif opcao == 3:
                                sacar = float(input("Digite quanto você deseja sacar: "))
                                print(sacado(sacar, saldo, totalsacado))
                            elif opcao == 4:
                                print(extrato["Deposito","Saque","Transferência"])
                            elif opcao == 5:
                                print(f"O total depositado foi R${totaldepositado}")
                            elif opcao == 6:
                                print(f"O total sacado foi R${totalsacado}")
                            elif opcao == 7:
                                destinatario = input("Digite nome do destinatario da trasnferência: ")
                                transferir = float(input("Digite valor da transferência: "))
                                print(transferido(transferir, saldo))
                            elif opcao == 8:
                                print("...Finalizando o programa")
                                break

                        except ValueError:
                            print("Onde for solicitado número, digite apenas números!")
                            continue
                else:
                    print("Usuário ou senha incorreto, tente novamente!")
            except ValueError:
                print("Em senha digite apenas números, tente novamente!")