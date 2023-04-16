V = {"+", "-", "range (10)", "."} 
Q = {"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"}
delta = {"q0": {"+": "q1", "-": "q1", "range (10)": "q2"}, 
         "q1": {"range (10)": "q2"},
         "q2": {"range (10)": "q2", ".": "q3"},
         "q3": {"range (10)": "q4"},
         "q4": {"range (10)": "q4", "E": "q5"},
         "q5": {"+": "q6", "-": "q6", "range (10)": "q7"},
         "q6": {"range (10)": "q7"},
         "q7": {"range (10)": "q7", "E": "q5"},
        }
q0 = "q0"
F = {"q7"}

def reconhece(palavra:str):
    def reconhecedigitos0_9(c):
        return c.isdigit() and c in "0123456789"
    
    estado_atual= "q0"
    tam = len(palavra)
    i = 0
    while (i<tam) and (estado_atual != "Erro"):
        simbolo_atual = palavra[i]
        if simbolo_atual in V: 
            estado_atual = delta[estado_atual][simbolo_atual]
        elif  reconhecedigitos0_9(simbolo_atual):
            estado_atual = delta[estado_atual]["range (10)"]
        elif simbolo_atual == "E":
            estado_atual = delta[estado_atual]["E"]
        else:
            estado_atual = "Erro"
        i+=1
    return (estado_atual in F) and (i==tam)

for exemplo in ["12.5", "-12.5", "12.55E-10", "-12.45E-10", "125", "12.55E10"]:
	print(f"'{exemplo}'\t{reconhece(exemplo)}")
 
 
 