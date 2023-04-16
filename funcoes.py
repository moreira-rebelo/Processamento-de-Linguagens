def slurp(filename):
    with open(filename, "r") as fh:
        contents = fh.read()
    return contents

"""
def troco(aux, qttE2, qttE1, qttC50, qttC20, qttC10, qttC5, qttC2, qttC1, tE2, tE1, tC50, tC20, tC10, tC5, tC2, tC1):

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

    if 0 < aux < 0.01:
        aux = -1

    return qttE2, qttE1, qttC50, qttC20, qttC10, qttC5, qttC2, qttC1, tE2, tE1, tC50, tC20, tC10, tC5, tC2, tC1, aux


def imprimirTroco(troco, tE2, tE1, tC50, tC20, tC10, tC5, tC2, tC1):
    if 0 < troco < 0.01:
        print(f"Sem troco!")
    else:
        print(f"Troco: €{troco:0.2f}")
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
            tC1 = 0
    return tE2, tE1, tC50, tC20, tC10, tC5, tC2, tC1
    """