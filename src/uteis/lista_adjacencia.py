class Vizinho:
	def __init__(self, indice_celula, simbolo_acesso):
		self.indice_celula = indice_celula
		self.simbolo_acesso = simbolo_acesso
		pass

class Celula:
	def __init__(self, label, tipo):
		self.label = label
		self.tipo = tipo
		self.vizinho = []
		pass

class ListaAdjacencia:
	def __agrupa_transicoes(self, celulas_sem_adjacentes, alfabeto, transicoes):
		celulas = celulas_sem_adjacentes
		def agrupa_vizinhos(adjacentes, k):
			for i in range(len(adjacentes)):
				for j in range(len(celulas)):
					if adjacentes[i] == celulas[j].label:
						v = Vizinho(j, alfabeto[i])
						celulas[k].vizinho.append(v)
					pass
				pass
			pass

		for i in range(len(transicoes)):
			for j in range(len(celulas)):
				if transicoes[i][0] == celulas[j].label:
					agrupa_vizinhos(transicoes[i][1], j)
		return celulas

	def __cria_vetor_celulas(self, Q, q_inicial, q_finais):
		celulas = []
		for i in range(len(Q)):
			final = False
			inicial = False
			tipo = None
			c = None
			label = Q[i]
			for j in range(len(q_finais)):
				if Q[i] == q_finais[j]:
					final = True
			if Q[i] == q_inicial:
				inicial = True
			if final and inicial:
				tipo = 'IF'
			elif final and not inicial:
				tipo = 'F'
			elif not final and inicial:
				tipo = 'I'
			else:
				tipo = 'N'
			c = Celula(label, tipo)
			celulas.append(c)
		return celulas
			

	def __init__(self, Q, alfabeto, q_inicial, q_finais, transicoes):
		celulas_sem_adjacentes = self.__cria_vetor_celulas(Q, q_inicial, q_finais)
		self.celula = self.__agrupa_transicoes(celulas_sem_adjacentes, alfabeto, transicoes)



