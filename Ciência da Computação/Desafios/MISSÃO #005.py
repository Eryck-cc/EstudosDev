'''# Missão Diária 005 Tarde

## Médio/Difícil 

💰 Missão RPG: O Mercador Viajante

Um mercador da guilda retornou de suas viagens trazendo moedas de terras distantes. 🌎

Agora ele precisa da ajuda dos alquimistas-programadores para converter suas riquezas para reais!

---

🎯 Objetivo

Criar um programa que:

✅ Mostre uma lista de moedas disponíveis

✅ Pergunte qual moeda o usuário deseja converter

✅ Pergunte a quantidade da moeda

✅ Converta o valor para reais

✅ Exiba o resultado da conversão

---

🧩 Moedas Disponíveis

💵 Dólar → R$ 5.50

💶 Euro → R$ 6.20

💷 Libra → R$ 7.30


---

📜 Regras da Missão

⚔️ O programa deve utilizar:

✅ Lista

✅ "input()"

✅ "float()"

✅ Variáveis

✅ "if", "elif" e "else"

✅ Operações matemáticas

✅ f-string

❌ Não vale mostrar resultados prontos

❌ O usuário deve poder escolher entre pelo menos 3 moedas

---

## 👹 Mini Boss (Opcional)

🟢 Mostrar uma pequena história sobre a moeda escolhida

🟢 Informar quando uma moeda inválida for digitada

🟡 Mostrar quantos reais o mercador possui ao final da conversão

🟡 Adicionar pelo menos 2 moedas extras ao sistema

---

## ☠️Ultra Boss PC do MZ:
⚫ Faça a conversão de kwanzas para reais

---

Boa sorte mercadores! 💰

---
## Dica:
 pesquisem no Google conversão de moeda. 🫪👍'''

moedas = ("Dólar", "Euro", "Libra", "Kwanzas", "Bitcoin")

historias = {
    "Dólar": "A moeda mais usada no comércio internacional e referência da economia mundial.",
    "Euro": "Moeda oficial de diversos países da Europa, criada para facilitar o comércio.",
    "Libra": "Moeda oficial do Reino Unido e uma das mais antigas ainda em circulação.",
    "Kwanzas": "Moeda oficial de Angola, utilizada em todas as transações do país.",
    "Bitcoin": "Criptomoeda descentralizada criada em 2009, sem controle de bancos centrais."
}


conversao = input("Digite o nome da moeda ao qual você deseja converter: ")
quantidade = float(input("Digite a quantida de reais que você quer converter: "))
if conversao not in moedas:
    print("Moeda inválida digitada!")
    exit()
conversao = conversao.strip().upper()



def converter_moeda(a, b):
    if b == "DOLAR" or b == "DÓLAR":
        return f"[R${a}] = [${a * 5.18}], Pequena história sobre o Dólar: {historias["Dólar"]}"
    elif b == "EURO":
        return f"[R${a}] = [€{a * 5.91}], Pequena história sobre o Euro: {historias['Euro']}"
    elif b == "LIBRA":
        return f"[R${a}] = [£{a * 6.83}], Pequena história sobre a Libra: {historias['Libra']}"
    elif b == "KWANZAS":
        return f"[R${a}] = [Kz{a * 0.0056}], Pequena história sobre o Kwanza: {historias['Kwanzas']}"
    elif b == "BITCOIN":
        return f"[R${a}] = [₿{a * 311577.54}], Pequena história sobre o Bitcoin: {historias['Bitcoin']}"
    
print(converter_moeda(quantidade,conversao))