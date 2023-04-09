import ply.lex as lex

tokens = ("1c", "2c", "5c", "10c", "20c", "50c", "1e", "2e")
total = 0

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

lexer = lex.lex()
lexer.input("1c")
lexer.token()
lexer.input("2c")
lexer.token()

print(f"Total: {total}")

