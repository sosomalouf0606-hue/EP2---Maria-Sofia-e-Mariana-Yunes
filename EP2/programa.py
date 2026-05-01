import funcoes as fun
cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
print(fun.imprime_cartela(cartela))
i = 0 
n = 0
dados = fun.rolar_dados(6)
dados_guardados = []
while i < 12:
    print (f'dados rolados: {dados}')
    print(f'dados guardados: {dados_guardados}')
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
    acao = int(input(' '))
    if acao == 1:
        print("Digite o índice do dado a ser guardado (0 a 4):")
        guardar = int(input(' '))
        novos_dados = fun.guardar_dado(dados, dados_guardados, guardar)
        dados = novos_dados[0]
        dados_guardados = novos_dados[1]
    elif acao == 2:
        print("Digite o índice do dado a ser removido (0 a 4):")
        remover = int(input(' '))
        novos_dados = fun.remover_dado(dados, dados_guardados, remover)
        dados = novos_dados[0]
        dados_guardados = novos_dados[1]
    elif acao == 3:
        if n < 2:
            novos_dados = fun.rolar_dados(len(dados))
            dados = novos_dados
            n += 1
        else:
            print('"Você já usou todas as rerrolagens."')
    elif acao == 4:
        print ('Cartela de pontos:')
        print (fun.imprime_cartela(cartela))
    elif acao == 0:
        dados_finais = dados + dados_guardados
        print('Digite a combinação desejada:')
        comb = input ('')
        if comb in cartela['regra_simples'] or comb in cartela['regra_avancada']:
            if cartela['regra_simples'][comb] != -1 or cartela['regra_avancada'][comb] != -1:
               cartela = fun.faz_jogada(dados_finais, comb, cartela)
               i += 1
               n = 0
               dados = fun.rolar_dados(6)
               dados_guardados = []
            else:
                print('Essa combinação já foi utilizada.')
        else:
            "Combinação inválida. Tente novamente."
    else:
        print("Opção inválida. Tente novamente.")
    s = 0


for p in cartela['regra_simples'].values():
    s += p
if s >= 63:
    s += 35
for p in cartela['regra_avancada'].values():
    s += p
print('Cartela de pontos:')
print(cartela)
print (f'Pontuação total: {259}')



    
