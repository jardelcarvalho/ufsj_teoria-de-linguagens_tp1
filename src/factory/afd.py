class AFD:
    def __init__(self, grafo):
        self.grafo = grafo
        self.label = 'Automato finito determinístico'

    def funcao_transicao(self, q, simbolo):
        prox_q = None
        for i in range(len(q)):
            if q[i][0] == simbolo:
                prox_q = q[i][1]
                break
        return prox_q

    def processa_palavra(self, palavra):
        aceitou = False
        q0 = None
        for i in range(len(self.grafo.Q)):
            if self.grafo.Q[i].tipo == 'inicial':
                q0 = i
                break
        Q = self.grafo.Q
        atual = q0
        caminho = [atual]
        for i in range(len(palavra)):
            atual = self.funcao_transicao(Q[atual].tr, palavra[i])
            if atual == None:
                aceitou = False
                break
            atual = int(atual)
            caminho.append(atual)
        if Q[atual].tipo == 'final':
            aceitou = True
        return aceitou, caminho

    def aceita(self, palavra):
        return self.processa_palavra(palavra)