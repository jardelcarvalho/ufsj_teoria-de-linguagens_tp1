import uteis.leitura as lt
import uteis.estados_lista as el
from factory.automato_factory import AutomatoFactory

#teste leitura
print('#(1) Teste leitura')
leitor_arq = lt.Leitura()
info_automato = leitor_arq.ler_arquivo('afne')
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
lista_estados = el.ListaEstados(Q, alfabeto, q_inicial, q_finais, transicoes)
for i in range(len(lista_estados.celula)):
    str_print = ''
    str_print = lista_estados.celula[i].label + ','
    for j in range(len(lista_estados.celula[i].vizinho)):
        str_print += ' ' + lista_estados.celula[lista_estados.celula[i].vizinho[j].indice_celula].label
        str_print += '-' + lista_estados.celula[i].vizinho[j].simbolo_acesso
    str_print += ', ' + lista_estados.celula[i].tipo
    print(str_print)


#teste afd
print('\n#(3) Teste AFD')
leitor_arq = lt.Leitura()
info_automato = leitor_arq.ler_arquivo('afd')
Q = info_automato.get_Q()
alfabeto = info_automato.get_alfabeto()
q_inicial = info_automato.get_q_inicial()
q_finais = info_automato.get_q_finais()
transicoes = info_automato.get_transicoes()
estados_lista = el.ListaEstados(Q, alfabeto, q_inicial, q_finais, transicoes)
automato = AutomatoFactory.novo_automato('afd', estados_lista)
print('aac: ', automato.processa_palavra('aac'))
print('caa: ', automato.processa_palavra('caa'))
print('aaa: ', automato.processa_palavra('aaa'))
print('aaaaaabbbbbb: ', automato.processa_palavra('aaaaaabbbbbb'))
print('aa: ', automato.processa_palavra('aa'))
print('a: ', automato.processa_palavra('a'))
print('vazia: ', automato.processa_palavra(''))

#teste afn
print('\n#(4) Teste AFN')
leitor_arq = lt.Leitura()
info_automato = leitor_arq.ler_arquivo('afn')
Q = info_automato.get_Q()
alfabeto = info_automato.get_alfabeto()
q_inicial = info_automato.get_q_inicial()
q_finais = info_automato.get_q_finais()
transicoes = info_automato.get_transicoes()
estados_lista = el.ListaEstados(Q, alfabeto, q_inicial, q_finais, transicoes)
automato = AutomatoFactory.novo_automato('afn', estados_lista)
print('aac: ', automato.processa_palavra('aac'))
print('caa: ', automato.processa_palavra('caa'))
print('aaa: ', automato.processa_palavra('aaa'))
print('aaaaaabbbbbb: ', automato.processa_palavra('aaaaaabbbbbb'))
print('aa: ', automato.processa_palavra('aa'))
print('a: ', automato.processa_palavra('a'))
print('abaa: ', automato.processa_palavra('abaa'))
print('babb: ', automato.processa_palavra('babb'))
print('vazia: ', automato.processa_palavra(''))

#teste afne
print('\n#(5) Teste AFNE')
leitor_arq = lt.Leitura()
info_automato = leitor_arq.ler_arquivo('afne')
Q = info_automato.get_Q()
alfabeto = info_automato.get_alfabeto()
q_inicial = info_automato.get_q_inicial()
q_finais = info_automato.get_q_finais()
transicoes = info_automato.get_transicoes()
estados_lista = el.ListaEstados(Q, alfabeto, q_inicial, q_finais, transicoes)
automato = AutomatoFactory.novo_automato('afne', estados_lista)
print('ababbaba: ', automato.processa_palavra('ababbaba'))
print('abababb: ', automato.processa_palavra('abababb'))
print('aaaccc: ', automato.processa_palavra('aaaccc'))
print('aaaaaabbbbbb: ', automato.processa_palavra('aaaaaabbbbbb'))
print('aa: ', automato.processa_palavra('aa'))
print('a: ', automato.processa_palavra('a'))
print('accabaz: ', automato.processa_palavra('accabaz'))
print('zbabb: ', automato.processa_palavra('zbabb'))
print('b: ', automato.processa_palavra('b'))
print('cc: ', automato.processa_palavra('cc'))
print('vazia: ', automato.processa_palavra(''))