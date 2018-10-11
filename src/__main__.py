import factory.automato_factory as af
import uteis.grafo as gra

def imprime_grafo(grafo):
    Q = grafo.Q
    for i in range(len(Q)):
        ls = []
        for j in range(len(Q[i].tr)):
            ls.append([Q[i].tr[j][0], Q[int(Q[i].tr[j][1])].label])
        print(Q[i].label, ls, Q[i].tipo)

def imprime_processamento(grafo, palavra, aceitou, caminho):
    Q = grafo.Q
    s = '('
    tam = len(caminho)
    sa = None
    for i in range(tam):
        s += Q[caminho[i]].label
        if i < tam - 1:
            s += ' -> '
    s += ')'
    sa = ''
    if aceitou:
        if Q[caminho[len(caminho) - 1]].tipo == 'final':
            sa = ', a palavra FOI ACEITA!'
    else:
        sa = ', a palavra NÃO FOI ACEITA!'
    print('     ', s, sa)

#Aqui começa
while True:
    tipo = input('Menu\n(1) AFD\n(2) AFN\n(3) AFN vazio\n(@) Sair\nEscolha: ')
    nome_arq = None
    if tipo == '1':
        nome_arq = 'afd'
    elif tipo == '2':
        nome_arq = 'afn'
    elif tipo == '3':
        nome_arq = 'afn_vazio'
    elif tipo == '@':
        break

    grafo = gra.Grafo(nome_arq)
    ft = grafo.ft

    automato = af.AutomatoFactory.novo_automato(grafo, ft)
    print('##', automato.label, '##')
    imprime_grafo(grafo)
    while True:
        palavra = input('Digite a palavra ou @ para sair: ')
        if palavra == '@':
            break    
        aceitou, caminhos = automato.aceita(palavra)
        if ft == 'afd':
            imprime_processamento(grafo, palavra, aceitou, caminhos)
        else:
            for i in range(len(caminhos)):
                imprime_processamento(grafo, palavra, aceitou, caminhos[i])
