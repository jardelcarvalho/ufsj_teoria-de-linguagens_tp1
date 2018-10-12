import uteis.leitura as lt
import uteis.lista_adjacencia as ladj

#teste leitura
print('#(1) Teste leitura')
leitor_arq = lt.Leitura()
info_automato = leitor_arq.ler_arquivo('afn')
print(info_automato.get_Q())
print(info_automato.get_alfabeto())
print(info_automato.get_funcao_transicao())
print(info_automato.get_q_inicial())
print(info_automato.get_q_finais())
print(info_automato.get_transicoes())

#teste lista de adjacência
print('\n#(2) Teste lista de adjacência')
Q = info_automato.get_Q()
alfabeto = info_automato.get_alfabeto()
q_inicial = info_automato.get_q_inicial()
q_finais = info_automato.get_q_finais()
transicoes = info_automato.get_transicoes()
lista_adjacencia = ladj.ListaAdjacencia(Q, alfabeto, q_inicial, q_finais, transicoes)
for i in range(len(lista_adjacencia.celula)):
    str_print = ''
    str_print = lista_adjacencia.celula[i].label + ','
    for j in range(len(lista_adjacencia.celula[i].vizinho)):
        str_print += ' ' + lista_adjacencia.celula[lista_adjacencia.celula[i].vizinho[j].indice_celula].label
        str_print += '-' + lista_adjacencia.celula[i].vizinho[j].simbolo_acesso
    str_print += ', ' + lista_adjacencia.celula[i].tipo
    print(str_print)