import ply.lex as lex  #biblioteca lex
import re  #suporte para expressões regulares
from funcoes import slurp

#Tokens
tokens = ("c1", "c2", "c5", "c10", "c20", "c50", "e1", "e2",
          "QUANTIA", "PRODUTO", "CANCELAR", "LISTAR_STOCK", "LISTAR_MEALHEIRO")

#Dicionário de moedas
valoresMoedas = {'c1': 0.01, 'c2': 0.02, 'c5': 0.05, 'c10': 0.10, 'c20': 0.20, 'c50': 0.50, 'e1': 1.00, 'e2': 2.00}

#Dicionário de produtos
produtos = {"twix": 2.30, "lanche": 2.50, "croissant": 2.50}

#-------------VARIÁVEIS-------------
total = 0
aux = 0
manterTroco = 0
auxStrings = 'a'

#Moedas:
qttC1 = 50; qttC2 = 50; qttC5 = 50; qttC10 = 50; qttC20 = 50; qttC50 = 25; qttE1 = 20; qttE2 = 10

tC1 = 0; tC2 = 0; tC5 = 0; tC10 = 0; tC20 = 0; tC50 = 0; tE1 = 0; tE2 = 0

#Produtos:
qttCroissant = 7; qttLanche = 7; qttTwix = 10

#Funções para validação de expressões regulares
def t_QUANTIA(t):
    r'QUANTIA\s+(c[0-9]?[0-9]?|e[1-9])(\s*,\s*(c[0-9]?[0-9]?|e[1-9]))*\s*\.' #QUANTIA + espaços + moeda +  mais moedas ou nada + espaços + teminação com '.'
    listaDeMoedas = re.findall(r'(c[0-9]?[0-9]?|e[1-9])', t.value) #proura em t.value por todas as ocurrências de moedas

    global total

    for moeda in listaDeMoedas:
        if moeda not in valoresMoedas:
            print(f"{moeda} - Moeda não aceite!")
        elif moeda == 'c1' and moeda in listaDeMoedas:
            global qttC1
            qttC1 += 1
            parcial = valoresMoedas[moeda]
            total += parcial
        elif moeda == 'c2' and moeda in listaDeMoedas:
            global qttC2
            qttC2 += 1
            parcial = valoresMoedas[moeda]
            total += parcial
        elif moeda == 'c5' and moeda in listaDeMoedas:
            global qttC5
            qttC5 += 1
            parcial = valoresMoedas[moeda]
            total += parcial
        elif moeda == 'c10' and moeda in listaDeMoedas:
            global qttC10
            qttC10 += 1
            parcial = valoresMoedas[moeda]
            total += parcial
        elif moeda == 'c20' and moeda in listaDeMoedas:
            global qttC20
            qttC20 += 1
            parcial = valoresMoedas[moeda]
            total += parcial
        elif moeda == 'c50' and moeda in listaDeMoedas:
            global qttC50
            qttC50 += 1
            parcial = valoresMoedas[moeda]
            total += parcial
        elif moeda == 'e1' and moeda in listaDeMoedas:
            global qttE1
            qttE1 += 1
            parcial = valoresMoedas[moeda]
            total += parcial
        elif moeda == 'e2' and moeda in listaDeMoedas:
            global qttE2
            qttE2 += 1
            parcial = valoresMoedas[moeda]
            total += parcial

    return t

def t_PRODUTO(t):
    r'PRODUTO=(twix|lanche|croissant)'
    listaDeProdutos = re.findall(r'(twix|lanche|croissant)', t.value)

    global aux
    aux = produtos[listaDeProdutos[0]]
    global auxStrings
    auxStrings = listaDeProdutos[0]
    return t

def t_CANCELAR(t):
    r'CANCELAR'
    return t

def t_LISTAR_STOCK(t):
    r'LISTAR\s+STOCK'
    return t

def t_LISTAR_MEALHEIRO(t):
    r'LISTAR\s+MEALHEIRO'
    return t

def t_ESPACO(t):
    r"[ ]+"
    pass

def t_VIRGULA(t):
    r","
    pass

def t_PONTO(t):
    r"."
    pass
def t_EOL(t):
    r"\n"
    pass

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def troco(aux):
    global qttE2, qttE1, qttC50, qttC20, qttC10, qttC5, qttC2, qttC1
    global tE2, tE1, tC50, tC20, tC10, tC5, tC2, tC1

    while total > 0:
        while aux >= 2 and qttE2 > 0:
            tE2 += 1
            aux -= 2
            qttE2 -= 1
        while aux >= 1 and qttE1 > 0:
            tE1 += 1
            aux -= 1
            qttE1 -= 1
        while aux >= 0.5 and qttC50 > 0:
            tC50 += 1
            aux -= 0.5
            qttC50 -= 1
        while aux >= 0.2 and qttC20 > 0:
            tC20 += 1
            aux -= 0.2
            qttC20 -= 1
        while aux >= 0.1 and qttC10 > 0:
            tC10 += 1
            aux -= 0.1
            qttC10 -= 1
        while aux >= 0.05 and qttC5 > 0:
            tC5 += 1
            aux -= 0.05
            qttC5 -= 1
        while aux >= 0.02 and qttC2 > 0:
            tC2 += 1
            aux -= 0.02
            qttC2 -= 1
        while aux >= 0.01 and qttC1 > 0:
            tC1 += 1
            aux -= 0.01
            qttC1 -= 1
        if aux > 0 and aux < 0.01:
            aux = -1


lexer = lex.lex()
lexer.input(slurp("tokens.txt"))

for tok in lexer:
    if tok.type == 'QUANTIA':
        print(f"Crédito: €{total:0.2f}\n")

    elif tok.type == 'CANCELAR':
        troco(total)
        print(f"Valor devolvido: €{total:0.2f}\n")

    elif tok.type == 'PRODUTO':
        print(f"Preço de {auxStrings}: €{aux:0.2f}\n")
        if total < aux:
            aux = aux - total
            print(f"Quantia insficiente! Faltam: €{aux:0.2f}")
            print(f"Crédito: €{total:0.2f}\n")

        elif total >= aux:
            aux = total - aux
            total = 0
            manterTroco = aux

            if aux > 0:

                troco(aux)

                print(f"Vendido!")

                if manterTroco == 0:
                    print(f"Sem troco!")
                else:
                    print(f"Troco: €{manterTroco:0.2f}")
                    print(f"Devolvido sob a forma de:")
                    if tE2 > 0:
                        print(f"{tE2} moedas de 2€")
                        tE2 = 0
                    if tE1 > 0:
                        print(f"{tE1} moedas de 1€")
                        tE1 = 0
                    if tC50 > 0:
                        print(f"{tC50} moedas de 50c")
                        tC50 = 0
                    if tC20 > 0:
                        print(f"{tC20} moedas de 20c")
                        tC20 = 0
                    if tC10 > 0:
                        print(f"{tC10} moedas de 10c")
                        tC10 = 0
                    if tC5 > 0:
                        print(f"{tC5} moedas de 5c")
                        tC5 = 0
                    if tC2 > 0:
                        print(f"{tC2} moedas de 2c")
                        tC2 = 0
                    if tC1 > 0:
                        print(f"{tC1} moedas de 1c")
                        tE2 = 0

            if auxStrings == 'twix':
                qttTwix -= 1
            if auxStrings == 'lanche':
                qttLanche -= 1
            if auxStrings == 'croissant':
                qttCroissant -= 1

    elif tok.type == 'LISTAR_STOCK':
        print(f"Twix: {qttTwix:d}")
        print(f"Lanche: {qttLanche:d}")
        print(f"Croissant: {qttCroissant:d}\n")

    elif tok.type == 'LISTAR_MEALHEIRO':
        print(f"C1: {qttC1:d}")
        print(f"C2: {qttC2:d}")
        print(f"C5: {qttC5:d}")
        print(f"C10: {qttC10:d}")
        print(f"C20: {qttC20:d}")
        print(f"C50: {qttC50:d}")
        print(f"E1: {qttE1:d}")
        print(f"E2: {qttE2:d}")


    else:
        print("Token inesperado:", tok.value)
        exit(1)
