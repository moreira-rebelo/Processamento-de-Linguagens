import ply.lex as lex
from funcoes import slurp

tokens = ("1c", "2c", "5c", "10c", "20c", "50c", "1e", "2e", "ESPACO")
total = 0
twix = 1.50
aux = 0


def t_1c(t):
    r"1c"
    global total
    total += 0.01;
    pass

def t_2c(t):
    r"2c"
    global total
    total += 0.02
    pass

def t_5c(t):
    r"5c"
    global total
    total += 0.05
    pass

def t_10c(t):
    r"10c"
    global total
    total += 0.10
    pass

def t_20c(t):
    r"20c"
    global total
    total += 0.20
    pass

def t_50c(t):
    r"50c"
    global total
    total += 0.50
    pass

def t_1e(t):
    r"1e"
    global total
    total += 1.00
    pass

def t_2e(t):
    r"2e"
    global total
    total += 2.00
    pass

def t_other(t):
    r"[.\n]"
    pass

def t_error(t):
    print("Token inesperado")
    exit(1)

def t_ESPACO(t):
    r"[ ]+"
    pass

lexer = lex.lex()
lexer.input(slurp("tokens.txt"))

for tok in lexer:
    pass

print(f"Total inserido: {total:0.2f}€\n")

if total < twix:
    aux = twix - total
    print(f"Saldo insuficiente! Faltam: {aux:0.2f}€\n")
elif total >= twix:
    aux = total - twix
    print(f"Vendido! Troco: {aux:0.2f}€\n")
