'''OBJETIVO
Perguntar o nome do arqueiro X
Perguntar a pontuação de 3 disparos X
Calcular a pontuação total X
Exibir o resultado final X
Informar se o arqueiro foi aprovado no treinamento X'''
'''MINI BOSS
Mostrar a média dos disparos X
Informar qual foi o melhor disparo X
Criar diferentes classificações (Bronze, Prata e Ouro)
Validar pontuações inválidas'''
'''ULTRA BOSS
Permitir vários arqueiros na mesma competição
Criar um ranking final
Exibir o campeão do torneio
Salvar os resultados em uma lista'''
print("A competição terá 5 arqueiros!")

nome = input("Digite o seu nome arqueiro: ")
print("Me diga a pontuação de seus 3 disparos!")
disparo_um = int(input("Primeiro: "))
disparo_dois = int(input("Segundo: "))
disparo_tres = int(input("Terceiro: "))

def calculo_pontuacao():
    return disparo_um + disparo_dois + disparo_tres

def validar_aprovacao():
    if calculo_pontuacao() >= 21:
        return "Aprovado"
    else:
        return "Reprovado"
    
def media_disparos():
    return calculo_pontuacao() / 3

def melhor_disparo():
    if disparo_um > disparo_dois and disparo_um > disparo_tres:
        return f"Melhor disparo foi {disparo_um}"
    elif disparo_dois > disparo_um and disparo_dois > disparo_tres:
        return f"Melhor disparo foi {disparo_dois}"
    else:
        return f"Melhor disparo foi {disparo_tres}"


# Perguntar o nome do arqueiro
print(f"Arqueiro: {nome}")

# Perguntar a pontuação de 3 disparos
print(f"Disparo 1: {disparo_um}") 
print(f"Disparo 2: {disparo_dois}")
print(f"Disparo 3: {disparo_tres}")

# Calcular a pontuação total
print(f"Pontuação total: {calculo_pontuacao()}")

# Informar se o arqueiro foi aprovado no treinamento
print(f"Você foi {validar_aprovacao()}")

# Mostrar a média dos disparos
print(f"A média dos seus disparos foi: {media_disparos()}")

# Informar qual foi o melhor disparo
print(f"{melhor_disparo()}")

