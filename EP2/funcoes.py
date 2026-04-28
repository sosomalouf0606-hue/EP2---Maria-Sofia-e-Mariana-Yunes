# Exercício 1
from random import randint
def rolar_dados (n):
    l = []
    for k in range (0, n, 1):
        a = randint(1, 6)
        l.append(a)
    return l
# Exercício 2
def guardar_dado (dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    del dados_rolados [dado_para_guardar]
    return [dados_rolados, dados_no_estoque]
#exercício 3
def remover_dado(dados_rolados, dados_no_estoque, n): #n= índice do dado a ser removido do estoque
    lista_dados=[]
    dado_removido=dados_no_estoque[n]
    novo_estoque=[]
    i=0
    while i<len(dados_no_estoque):
        if i!=n:
            novo_estoque.append(dados_no_estoque[i])
    dados_rolados.append(dado_removido)
    dados_no_estoque=dados_no_estoque-dado_removido
    lista_dados.append(dados_rolados)
    lista_dados.append(novo_estoque)
    return lista_dados

