class AFN:
    def __init__(self, grafo):
        self.label = 'Automato finito não determinístico'
        self.Q = grafo.Q
        self.caminho = None
        self.palavra = None
        self.atual = None
        self.todos_caminhos = None
    
    def funcao_transicao(self):
        if self.palavra == '':
            self.todos_caminhos.append(self.caminho)
            if self.Q[self.atual].tipo == 'final':
                return True
            return False
        else:
            for i in range(len(self.Q[self.atual].tr)):
                if self.Q[self.atual].tr[i][0] == self.palavra[0]:
                    p_temp = self.palavra
                    self.palavra = p_temp[1 : ]
                    a_temp = self.atual
                    self.atual = int(self.Q[self.atual].tr[i][1])
                    self.caminho.append(self.atual)
                    aceitou = self.funcao_transicao()
                    if aceitou == True:
                        return aceitou
                    self.palavra = p_temp
                    self.caminho = self.caminho[ : -1]
                    self.atual = a_temp
            return False

    def processa_palavra(self, palavra):
        aceitou = None
        q0 = None
        for i in range(len(self.Q)):
            if self.Q[i].tipo == 'inicial':
                q0 = i
                break
        self.atual = q0
        self.caminho = [self.atual]
        self.todos_caminhos = []
        self.palavra = palavra
        aceitou = self.funcao_transicao()
        return aceitou

    def aceita(self, palavra):
        aceitou = self.processa_palavra(palavra)
        return aceitou, self.todos_caminhos