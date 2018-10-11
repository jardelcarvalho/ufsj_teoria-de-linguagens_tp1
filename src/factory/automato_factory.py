from . import afd as afd
from . import afn as afn
from . import afne as afne

class AFD:
     def __init__(self, grafo, funcao_transicao):
        self.grafo = grafo
        self.funcao_transicao = funcao_transicao
        pass

class AutomatoFactory:
    def novo_automato(grafo, funcao_transicao):
        if funcao_transicao == 'afd':
            return afd.AFD(grafo)
        elif funcao_transicao == 'afn':
            return afn.AFN(grafo)
        


