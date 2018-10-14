from . import automato as a

class AFN(a.Automato):
    class Empilhavel:
        def __init__(self, atual_i, i_palavra, visitado):
            self.atual_i = atual_i
            self.i_palavra = i_palavra
            self.visitado = visitado
            pass


    def __init__(self, estados_lista):
        # Chamando construtor da superclasse
        super(AFN, self).__init__('Automato finito não determinístico', estados_lista)
        pass

    def __funcao_transicao(self, palavra):
        atual_i = self.estados_lista.i_q0
        if len(palavra) == 0:
            return self._verifica_final(atual_i)
        else:
            i_palavra = 0
            tam_palavra = len(palavra)
            pilha = [atual_i]
            aceitou = False
            visitado = [False for i in range(len(self.estados_lista.celula))]
            i_palavra_pilha = [0 for i in range(len(self.estados_lista.celula))]
            while pilha != [] and not aceitou:
                atual_i = pilha.pop()
                i_palavra = i_palavra_pilha[atual_i]
                if i_palavra == tam_palavra:
                    if self._verifica_final(atual_i):
                        aceitou = True
                        pilha.append(atual_i)
                        print('pilha = ', pilha)
                else:
                    if not visitado[atual_i]:
                        candidatos, travou = self._proximo(atual_i, palavra[i_palavra])
                        if not travou:
                            #empilhavel = self.Empilhavel(atual_i, i_palavra, True)
                            pilha.append(atual_i)
                            visitado[atual_i] = True
                            i_palavra += 1
                            for c in candidatos:
                                pilha.append(c)
                                i_palavra_pilha[c] = i_palavra
                            print(i_palavra)
    
    def processa_palavra(self, palavra):
        # Este método é abstrato na superclasse Automato,
        # está sendo sobrescrito de acordo com a função programa 
        # deste afd.
        # Recebe uma palavra e a processa com o uso da função
        # programa. Retorna valor booleano indicando se a palavra
        # foi aceita.
        aceita = self.__funcao_transicao(palavra)
        return aceita