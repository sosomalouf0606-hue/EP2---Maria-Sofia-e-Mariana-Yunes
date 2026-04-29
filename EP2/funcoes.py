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
        i+=1
    dados_rolados.append(dado_removido)
    lista_dados.append(dados_rolados)
    lista_dados.append(novo_estoque)
    return lista_dados
#exercício 4
def calcula_pontos_regra_simples(lista_dados):
    dic_pontos={}
    for dado in range(1,7):
        dic_pontos[dado]=0
        for i in lista_dados:
            if i==dado:
                dic_pontos[dado]+=i
    return dic_pontos
#exercício 5
def calcula_pontos_soma(dados_rolados):
    soma=0
    i=0
    while i<len(dados_rolados):
        soma+=dados_rolados[i]
        i+=1
    return soma
#exercício 6
def calcula_pontos_sequencia_baixa(dados_rolados):
    for inicio_sequencia in range(1,4):
        contador=0
        for valor in range(inicio_sequencia,inicio_sequencia+4):
            if valor in dados_rolados:
                contador+=1
    if contador==4:
        return 15
    return 0


        

