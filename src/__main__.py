import uteis.leitura as lt
import uteis.estados_lista as el
from factory.automato_factory import AutomatoFactory
import os

class Aplicacao:
    __menu_principal = '\--- Menu principal\n ------ Selecione o automato\n ------ (1) AFD\n ------ (2) AFN\n ------ (3) AFNE\n ------ (4) Sair'
    __input_escolha_msg = ' ------ Escolha: '
    __input_palavra_msg = ' ------ Digite a Palavra ou Fim para sair: '

    @staticmethod
    def __imprime_saida(palavra, aceita, conjunto_caminho, estados_lista):
        string_resultado = ' ------ {' + palavra + '}, '
        if aceita:
            string_resultado += 'Aceita, {'
        else:
            string_resultado += 'Não aceita, {'
        for c in conjunto_caminho:
            string_resultado += estados_lista.celula[c].label + ', '
        if conjunto_caminho != []:
            string_resultado = string_resultado[ : -2]
        else:
            string_resultado += ' '
        string_resultado += '}'
        print(string_resultado)

    @staticmethod
    def __menu_automato(tipo_automato):
        leitor_arq = lt.Leitura()
        info_automato = leitor_arq.ler_arquivo(tipo_automato)
        Q = info_automato.get_Q()
        alfabeto = info_automato.get_alfabeto()
        q_inicial = info_automato.get_q_inicial()
        q_finais = info_automato.get_q_finais()
        transicoes = info_automato.get_transicoes()
        estados_lista = el.ListaEstados(Q, alfabeto, q_inicial, q_finais, transicoes)
        automato = AutomatoFactory.novo_automato(tipo_automato, estados_lista)
        sair = False
        while not sair:
            os.system('clear')
            print('\--- ', automato.label)
            entrada = input(Aplicacao.__input_palavra_msg)
            if entrada == 'Fim' or entrada == 'fim':
                sair = True
            else:
                aceita, conjunto_caminho = automato.processa_palavra(entrada)
                Aplicacao.__imprime_saida(entrada, aceita, conjunto_caminho, estados_lista)
                input(' ------ Pressione Enter para continuar ... ')
            
    @staticmethod
    def menu_principal():
        sair = False
        while not sair:
            os.system('clear')
            print(Aplicacao.__menu_principal)
            escolha = input(Aplicacao.__input_escolha_msg)
            escolha = int(escolha)
            if escolha is 1:
                Aplicacao.__menu_automato('afd')
            elif escolha is 2:
                Aplicacao.__menu_automato('afn')
            elif escolha is 3:
                Aplicacao.__menu_automato('afne')
            elif escolha is 4:
                sair = True

### Início ###
# Chamando menu
Aplicacao.menu_principal()