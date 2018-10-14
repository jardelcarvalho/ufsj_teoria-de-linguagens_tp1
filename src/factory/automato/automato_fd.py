from . import automato as a

class AFD(a.Automato):
    def __init__(self, estados_lista):
        # Chamando construtor da superclasse
        super(AFD, self).__init__('Automato finito determinístico', estados_lista)
        pass

    def __funcao_transicao(self, palavra):
        # Função de transição que descreve o comportamento
        # de um AFD.
        # Retorna um valor booleano indicando se a palavra foi aceita.
        # Usa função da superclasse __proximo() na execução.
        travou = None
        atual_i = self.estados_lista.i_q0
        for i in range(len(palavra)):
            simbolo = palavra[i]
            candidatos, travou = self._proximo(atual_i, simbolo)
            if candidatos != []:
                atual_i = candidatos.pop()
            if travou:
                break
        if travou:
            return False
        else:
            return self._verifica_final(atual_i)

    def processa_palavra(self, palavra):
        # Este método é abstrato na superclasse Automato,
        # está sendo sobrescrito de acordo com a função programa 
        # deste afd.
        # Recebe uma palavra e a processa com o uso da função
        # programa. Retorna valor booleano indicando se a palavra
        # foi aceita.
        aceita = self.__funcao_transicao(palavra)
        return aceita
        