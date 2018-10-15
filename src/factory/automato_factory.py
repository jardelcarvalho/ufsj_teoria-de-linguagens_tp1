from .automato.automato_fd import AFD
from .automato.automato_fn import AFN
from .automato.automato_fne import AFNE

class AutomatoFactory:
    @staticmethod
    def novo_automato(funcao_transicao, estados_lista):
        if funcao_transicao == 'afd':
            return AFD(estados_lista)
        elif funcao_transicao == 'afn':
            return AFN(estados_lista)
        elif funcao_transicao == 'afne':
            return AFNE(estados_lista)
        


