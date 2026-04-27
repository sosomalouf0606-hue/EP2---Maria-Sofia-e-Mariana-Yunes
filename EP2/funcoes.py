from random import randint
def rolar_dados (n):
    l = []
    for k in range (0, n, 1):
        a = randint(1, 6)
        l.append(a)
    return l

def guardar_dado (dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    del dados_rolados [dado_para_guardar]
    return [dados_rolados, dados_no_estoque]

