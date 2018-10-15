from . import automato as a

class AFN(a.Automato):

    class Empilhavel:
        # Esta classe é uma abstração de um estado candidato
        # no processamento de um símbolo de uma palavra.
        def __init__(self, i_celula, i_palavra, visitado):
            # Recebe o índice da célula que especifica um estado do automato,
            # o índice que indica o síbolo da palavra que foi processado e 
            # uma variável booleana indicando se este elemento da pilha
            # já foi utilizado para se testar uma transição.
            self.i_celula = i_celula
            self.i_palavra = i_palavra
            self.visitado = visitado
            pass


    def __init__(self, estados_lista):
        # Chamando construtor da superclasse
        super(AFN, self).__init__('Automato finito não determinístico', estados_lista)
        pass

    def __remove_nao_visitados(self, pilha):
        # Descarta objetos do tipo empilhavel de uma pilha
        # dos quais não foram marcados como visitados ainda.
        nova_pilha = [e for e in pilha if e.visitado]
        return nova_pilha

    def __funcao_transicao(self, palavra):
        # Função de transição que descreve o comportamento
        # de um AFN.
        # Retorna um valor booleano indicando se a palavra foi aceita e
        # o caminho percorrido para processar a palavra.
        # Usa função da superclasse __proximo() na execução.
        # Usa o método de busca em profundidade iterativa com pilha 
        # para processar a palavra.
        atual = self.Empilhavel(self.estados_lista.i_q0, 0, False)
        caminho = []
        aceitou = False
        if len(palavra) == 0:
            aceitou = self._verifica_final(atual.i_celula)
            if aceitou:
                caminho = [atual.i_celula]
            return aceitou, caminho
        else:
            pilha = [atual]
            i_palavra = 0
            tam_palavra = len(palavra)
            while pilha != [] and not aceitou:
                atual = pilha.pop()
                i_palavra = atual.i_palavra
                if i_palavra == tam_palavra:
                    if self._verifica_final(atual.i_celula):
                        aceitou = True
                        pilha = self.__remove_nao_visitados(pilha)
                        pilha.append(atual)
                        caminho = [e.i_celula for e in pilha]
                else:
                    if not atual.visitado:
                        candidatos, travou = self._proximo(atual.i_celula, palavra[i_palavra])
                        if not travou:
                            atual.visitado = True
                            pilha.append(atual)
                            i_palavra += 1
                            candidato_empilhavel = None
                            for c in candidatos:
                                candidato_empilhavel = self.Empilhavel(c, i_palavra, False)
                                pilha.append(candidato_empilhavel)
            return aceitou, caminho
    
    def processa_palavra(self, palavra):
        # Este método é abstrato na superclasse Automato,
        # está sendo sobrescrito de acordo com a função programa 
        # deste afd.
        # Recebe uma palavra e a processa com o uso da função
        # programa. Retorna valor booleano indicando se a palavra
        # foi aceita e o caminho pelos estados do automato.
        aceita, caminho = self.__funcao_transicao(palavra)
        return aceita, caminho