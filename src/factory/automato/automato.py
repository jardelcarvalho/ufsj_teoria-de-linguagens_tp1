from abc import ABC, abstractmethod

class Automato(ABC):
    def __init__(self, label, estados_lista):
        # Guarda o nome da função programa utilizada 
        # e o grafo direcionado que representa os 
        # estados do automato e suas transições.
        self.label = label
        self.estados_lista = estados_lista
        pass

    @abstractmethod
    def processa_palavra(self, palavra):
        # Sobrescrito e usado para passagem
        # da palavra a ser processada.
        # Deve retornar a um valor booleano
        # indicando se a palavra foi aceita.
        pass

    def _verifica_final(self, i):
        tipo = self.estados_lista.celula[i].tipo
        if tipo == 'IF' or tipo == 'F':
            return True
        else:
            return False
    
    def _proximo(self, atual_i, simbolo):
        # Recebe um símbolo e o índice do estado atual
        # e retorna o próximo estado juntamente com
        # um valor booleano indicando se aconteceu o process-
        # amento, ou seja, se a função programa foi total neste
        # estado.
        vizinho = self.estados_lista.celula[atual_i].vizinho
        travou = True
        candidatos = []
        for i in range(len(vizinho)):
            if vizinho[i].simbolo_acesso == simbolo:
                candidatos.append(vizinho[i].indice_celula)
                travou = False
            pass
        #print(candidatos)
        #input()
        return candidatos, travou
