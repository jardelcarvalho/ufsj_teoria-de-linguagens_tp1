from . import automato as a

class AFNE(a.Automato):

    class EstadoAceso:
        def __init__(self, i_celula, usado):
            self.i_celula = i_celula
            self.usado = usado
            pass
    
    class Processamento:
        # Esta classe é uma abstração de um estado candidato
        # no processamento de um símbolo de uma palavra.
        def __init__(self, i_celula, i_palavra, acendeu, estados_acesos):
            # Recebe o índice da célula que especifica um estado do automato,
            # o índice que indica o síbolo da palavra a ser processado e 
            # uma variável booleana indicando se este elemento da pilha
            # já foi usado(aceso). Estados_acesos é uma lista de estados acesos
            # a partir do estado atual.
            self.i_celula = i_celula
            self.i_palavra = i_palavra
            self.acendeu = acendeu
            self.estados_acesos = estados_acesos
            pass
        

    def __init__(self, estados_lista):
        # Chamando construtor da superclasse
        super(AFNE, self).__init__('Automato finito não determinístico com movimentos vazios', estados_lista)
        pass
    
    def __uniao_conjuntos(self, pilha):
        estados_presentes_conjunto = [False for i in range(len(self.estados_lista.celula))]
        uniao = []
        for e in pilha:
            for a in e.estados_acesos:
                estados_presentes_conjunto[a.i_celula] = True
        for i in range(len(estados_presentes_conjunto)):
            if estados_presentes_conjunto[i]:
                uniao.append(i)
        return uniao
    
    def __funcao_transicao(self, palavra):
        # Função de transição que descreve o comportamento
        # de um AFNE.
        # Retorna um valor booleano indicando se a palavra foi aceita e
        # o caminho percorrido para processar a palavra incluindo os
        # elementos acessos.
        # Usa função da superclasse __proximo() na execução.
        # Varre o estado da iteração procurando processamentos vazios e 
        # adicionando na lista de estados acesos.
        # A união dos conjuntos de estados acesos de todos os processamentos empilhados
        # corresponde ao número de estados acesos no processamento total da palavra.
        estado_inicial = self.estados_lista.i_q0
        aceitou = False
        caminho = None
        pilha = None
        if len(palavra) == 0:
            aceitou = self._verifica_final(estado_inicial)
            if aceitou:
                caminho = [estado_inicial]
            return aceitou, []
        else:
            i_palavra = 0
            proc_atual = self.Processamento(estado_inicial, i_palavra, False, [])
            pilha = [proc_atual]
            tam_palavra = len(palavra)
            while pilha != [] and not aceitou:
                proc_atual = pilha.pop()
                i_palavra = proc_atual.i_palavra
                if i_palavra == tam_palavra:
                    if self._verifica_final(proc_atual.i_celula):
                        estado_final_acesso = self.EstadoAceso(proc_atual.i_celula, False)
                        final = self.Processamento(proc_atual.i_celula, proc_atual.i_palavra, True, [estado_final_acesso])
                        pilha.append(final)
                        aceitou = True
                else:
                    if not proc_atual.acendeu:
                        cand_vazio, travou = self._proximo(proc_atual.i_celula, 'vazio')
                        proc_atual.acendeu = True
                        acesos = []
                        acesos.append(self.EstadoAceso(proc_atual.i_celula, False))
                        if not travou:
                            for cand in cand_vazio:
                                acesos.append(self.EstadoAceso(cand, False))
                        proc_atual.estados_acesos = acesos
                    proc_final_da_pilha = []
                    for i in range(len(proc_atual.estados_acesos)):
                        if not proc_atual.estados_acesos[i].usado:
                            cand_simbolo, travou = self._proximo(proc_atual.estados_acesos[i].i_celula, palavra[i_palavra])
                            if not travou:
                                proc_atual.estados_acesos[i].usado = True
                                for cand in cand_simbolo:
                                    proc = self.Processamento(cand, i_palavra + 1, False, [])
                                    proc_final_da_pilha.append(proc)
                    if proc_final_da_pilha != []:
                        pilha.append(proc_atual)
                        for i in range(len(proc_final_da_pilha)):
                            pilha.append(proc_final_da_pilha[i])
        uniao = self.__uniao_conjuntos(pilha)
        return aceitou, uniao

    def processa_palavra(self, palavra):
        # Este método é abstrato na superclasse Automato,
        # está sendo sobrescrito de acordo com a função programa 
        # deste afd.
        # Recebe uma palavra e a processa com o uso da função
        # programa. Retorna valor booleano indicando se a palavra
        # foi aceita e os estados acesos no processamento.
        aceita, estados_acesos = self.__funcao_transicao(palavra)
        return aceita, estados_acesos