import uteis.leitura as lt
import uteis.estados_lista as el
from factory.automato_factory import AutomatoFactory


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
estados_lista = el.ListaEstados(Q, alfabeto, q_inicial, q_finais, transicoes)

# criacao do automato
automato = AutomatoFactory.novo_automato('afd', estados_lista)
print(automato.processa_palavra(''))


leitor_arq = lt.Leitura()
info_automato = leitor_arq.ler_arquivo('afn')

# criacao do grafo orientado
# armazenado em uma lista de adjacência
# formato: lista_adjacencia.celula[i].vizinho[j]
Q = info_automato.get_Q()
alfabeto = info_automato.get_alfabeto()
q_inicial = info_automato.get_q_inicial()
q_finais = info_automato.get_q_finais()
transicoes = info_automato.get_transicoes()
estados_lista = el.ListaEstados(Q, alfabeto, q_inicial, q_finais, transicoes)

automato = AutomatoFactory.novo_automato('afn', estados_lista)
print(automato.processa_palavra('abbb'))
# aa, aaa, abbb