from . import arquivo as arq

class Estado:
	def __init__(self):
		self.tr = []
		self.label = None
		self.tipo = None
		pass

class Grafo:
	def cria_grafo(self):
		qs, ft, q0, qfs = arq.Arquivo.ler_cabecalho(self)
		print(qfs)
		Q = []
		for i in range(len(qs)):
			q = Estado()
			for j in range(len(qfs)):
				if qfs[j] == qs[i]:
					q.tipo = 'final'
				elif q0 == qs[i]:
					q.tipo = 'inicial'
				else:
					q.tipo = 'comum'
			q.label = qs[i]
			Q.append(q)
		Q = arq.Arquivo.ler_transicoes(self, Q)
		#arq.Arquivo.ft = ft
		return Q, ft
	
	def __init__(self, nome_arquivo):
		arq.Arquivo.define_arq(self, nome_arquivo)
		self.Q, self.ft = self.cria_grafo()
		pass




