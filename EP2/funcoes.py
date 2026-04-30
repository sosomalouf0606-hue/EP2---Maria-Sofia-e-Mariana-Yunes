# Exercício 1
from random import randint
def rolar_dados (n):
    l = []
    for k in range (0, n, 1):
        a = randint(1, 6)
        l.append(a)
    return l

#------------------------------------------------------------------

# Exercício 2
def guardar_dado (dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    del dados_rolados [dado_para_guardar]
    return [dados_rolados, dados_no_estoque]


#---------------------------------------------------------------------------

#exercício 3 
 # Existe um jeito mais rápido de fazer esse exercício. 
 # Não muda nada, mas se vc quiser eu te ensino depois
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


#---------------------------------------------------------------------------------------

#exercício 4
def calcula_pontos_regra_simples(lista_dados):
    dic_pontos={}
    for dado in range(1,7):
        dic_pontos[dado]=0
        for i in lista_dados:
            if i==dado:
                dic_pontos[dado]+=i
    return dic_pontos

#--------------------------------------------------------------------------------------------

#exercício 5
def calcula_pontos_soma(dados_rolados):
    soma=0
    i=0
    while i<len(dados_rolados):
        soma+=dados_rolados[i]
        i+=1
    return soma

#--------------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------------

# Exercício 7
def calcula_pontos_sequencia_alta(dados_rolados):
    for inicio_sequencia in range (1,3):
        contador = 0
        for valor in range (inicio_sequencia, inicio_sequencia + 5):
            if valor in dados_rolados:
                contador += 1
            if contador == 5:
                return 30
    return 0

#-----------------------------------------------------------------------------------------------

# Exercício 8
def calcula_pontos_full_house (dados_rolados):
    resp = 0
    l = [0, 0, 0, 0, 0, 0]
    for x in dados_rolados:
        if x == 1:
            l[0] += 1
        if x == 2:
            l[1] += 1
        if x == 3:
            l[2] += 1
        if x == 4:
            l[3] += 1
        if x == 5:
            l[4] += 1
        if x == 6:
            l[5] += 1
    if 2 in l and 3 in l:
        i = 0
        while i < len (l):
            if l[i] == 2:
                resp += 2 * (i + 1)
            if l[i] == 3:
                resp += 3 * (i + 1)
            i += 1
    return resp
#----------------------------------------------------------------------------
#exerício 9
def calcula_pontos_quadra(dados_rolados):
    i = 0
    while i < len(dados_rolados):
        contador = 0
        dado = dados_rolados[i]
        k = 0
        while k < len(dados_rolados):
            if dados_rolados[k] == dado:
                contador += 1
            k += 1
        if contador >= 4:
            soma = 0
            j = 0
            while j < len(dados_rolados):
                soma += dados_rolados[j]
                j += 1
            return soma
        i += 1
    return 0
#--------------------------------------------------------------------------------------
#exercício 10
def calcula_pontos_quina(dados_rolados):
    i = 0
    while i < len(dados_rolados):
        contador = 0
        dado = dados_rolados[i] 
        k = 0
        while k < len(dados_rolados):
            if dados_rolados[k] == dado:
                contador += 1
            k += 1 
        if contador >= 5:
            return 50
        i += 1
    return 0
#-------------------------------------------------------------------------------------------
# Exercício 11

def calcula_pontos_regra_avancada (dados_rolados):
    dic = {}
    dic['cinco_iguais'] = calcula_pontos_quina(dados_rolados)
    dic['full_house'] = calcula_pontos_full_house(dados_rolados)
    dic['quadra'] = calcula_pontos_quadra(dados_rolados)
    dic['sem_combinacao'] = calcula_pontos_soma(dados_rolados)
    dic['sequencia_alta'] = calcula_pontos_sequencia_alta(dados_rolados)
    dic['sequencia_baixa'] = calcula_pontos_sequencia_baixa(dados_rolados)
    return dic

#--------------------------------------------------------------------------------------------

# Exercício 12

def faz_jogada (dados, categoria, dic):
    simples = calcula_pontos_regra_simples(dados)
    avancada = calcula_pontos_regra_avancada(dados)
    if categoria == '1' or categoria == '2' or categoria == '3' or categoria == '4' or categoria == '5' or categoria == '6':
        dic['regra_simples'][int(categoria)] = simples[int(categoria)]
    else:
        dic['regra_avancada'][categoria] = avancada[categoria]
    return dic