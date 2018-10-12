import uteis.leitura as lt
import uteis.lista_adjacencia as ladj
#import factory.automato_factory as af


### Início ###
# leitura do automato
leitor_arq = lt.Leitura()
info_automato = leitor_arq.ler_arquivo('afd')

# criacao do grafo orientado
# armazenado em uma lista de adjacência
# formato: lista_adjacencia.celula[i].vizinho[j]
Q = info_automato.get_Q()
alfabeto = info_automato.get_alfabeto()
q_inicial = info_automato.get_q_inicial()
q_finais = info_automato.get_q_finais()
transicoes = info_automato.get_transicoes()
lista_adjacencia = ladj.ListaAdjacencia(Q, alfabeto, q_inicial, q_finais, transicoes)
estados = lista_adjacencia.celula

# criacao do automato