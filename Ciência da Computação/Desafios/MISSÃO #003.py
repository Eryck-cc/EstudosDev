'''# Missão diária 003 Noite
## Fácil 
⚔️ Missão RPG: A Ponte do Guardião
Um guardião antigo protege a ponte que leva ao castelo da guilda 🏰
Somente aventureiros fortes o suficiente podem passar!
🎯 Objetivo
Criar um programa que:
✅ Pergunte o nome do aventureiro
✅ Pergunte o nível dele
✅ Se o nível for maior ou igual a 10:
O guardião deixa passar 🛡️
✅ Se for menor que 10:
O guardião bloqueia a passagem 🚫
🧩 Exemplo
Digite o nome do aventureiro:
Treloso
Digite seu nível:
12
🛡️ O guardião permitiu sua passagem, Treloso!
📜 Regras da Missão
⚔️ O programa deve utilizar:
✅ input()
✅ if e else
✅ Variáveis
✅ print()
✅ int()
✅ Comparação numérica (>=, <)
❌ Não vale copiar código pronto da internet
❌ Não vale deixar o programa sem mensagens RPG
👹 Mini Boss (Opcional)
O guardião ficou mais exigente…
🟢 Criar uma mensagem especial caso o nível seja exatamente 10
🟢 Mostrar o nível digitado usando f-string
🟡 Criar um “modo lendário” para níveis acima de 20'''

def permissao(a):
    if a < 10:
        return "O guardião bloqueou a passagem!"
    elif a == 10:
        return "O guardião permitiu sua passagem por muito pouco!"
    elif a > 10 and a < 20:
        return "O guardião permitiu sua passagem!"
    else:
        return "O guardião se ajoelhou para você!"

    
try:
    aventureiro = input("Digite seu nome: ")
    nivel = int(input("Me diga seu nível: "))
    print(f"Seu nível é [{nivel}]!\n{permissao(nivel)} {aventureiro}!")
except ValueError:
    print("Em nivel deve ser digitado apenas um número inteiro!")
