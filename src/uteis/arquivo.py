import os

class Arquivo():
	arq_dir = None
	funcao_transicao = None

	def define_arq(self, nome_arquivo):
		Arquivo.arq_dir = os.path.abspath('data/' + nome_arquivo + '.txt')
		pass
	def ler_cabecalho(self):
		# q1,q2,...,qn.funcao_transicao.q0.qf1,qf2,...,qfn
		arq = open(Arquivo.arq_dir, 'r')
		c = arq.readline().split('\n')[0]
		c = c.split(' ')
		qs = c[0]
		qs = qs.split(',')
		ft = c[1]
		q0 = c[2]
		qfs = c[3].split(',')
		arq.close()
		return qs, ft, q0, qfs #estados, funcao_transicao, q0, estados finais -->Ex: q1 q2 q3 qf1 qf2, afd, q0, qf1 qf2 
        
	def ler_transicoes(self, Q):
		arq = open(Arquivo.arq_dir, 'r')
		arq.readline()
		alfabeto = arq.readline().split('\n')[0]
		alfabeto = alfabeto.split(' ')
		tr = arq.readlines()
		for i in range(len(tr)):
			l = tr[i].split('\n')[0]
			tr[i] = l.split(' ')
			l = tr[i]
			for j in range(len(Q)):
				if l[0] == Q[j].label:
					for k in range(len(l) - 1):
						for m in range(len(Q)):
							if l[k] == '-1':
								pass
							if Q[m].label == l[k + 1]:
								Q[j].tr.append([alfabeto[k], m]) #['símbolo', indice_estado] -->Ex: ['a', 1]
								break
		return Q