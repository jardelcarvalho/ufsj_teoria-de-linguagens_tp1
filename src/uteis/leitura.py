import os

class InfoAutomato:
	# Armazena informações do arquivo 
	# que dizem respeito ao automato.
	def __init__(self, Q, alfabeto, funcao_transicao, q_inicial, q_finais, transicoes):
		self.Q = Q
		self.alfabeto = alfabeto
		self.funcao_transicao = funcao_transicao
		self.q_inicial = q_inicial
		self.q_finais = q_finais
		self.transicoes = transicoes
		pass
	
	def get_Q(self):
		return self.Q

	def get_alfabeto(self):
		return self.alfabeto

	def get_funcao_transicao(self):
		return self.funcao_transicao

	def get_q_inicial(self):
		return self.q_inicial

	def get_q_finais(self):
		return self.q_finais

	def get_transicoes(self):
		return self.transicoes



class Leitura:
	# Realiza a leitura de informações contidas 
	# em um arquivo que descreve um automato.
	def __init__(self):
		self.arq_dir = None
		pass

	def __ler_cabecalho(self, arq):
		# Cabeçalho do arquivo: 
		# q1,q2,...,qn a,b funcao_transicao q0 qf1,qf2,...,qfn
		linha = arq.readline().split('\n')[0]
		linha = linha.split(' ')
		Q = linha[0]
		Q = Q.split(',')
		alfabeto = linha[1].split(',')
		funcao_transicao = linha[2]
		q_inicial = linha[3]
		q_finais = linha[4].split(',')
		return Q, alfabeto, funcao_transicao, q_inicial, q_finais

	def __ler_transicoes(self, arq):
		# Transições: qi qj qk ... qn
		#	alfabeto:    Si Sj ... Sn
		def quebra_linha(linha):
			linha = linha.split('\n')[0]
			dividido = linha.split(' ')
			q_atual = dividido[0]
			q_prox = dividido[1 : ]
			return q_atual, q_prox
		linhas = arq.readlines()
		transicoes = []
		for i in range(len(linhas)):
			q_atual, q_prox = quebra_linha(linhas[i])
			transicoes.append([q_atual, q_prox])
		return transicoes

	def ler_arquivo(self, nome_arquivo):
		# Retorna um objeto de InfoAutomato
		# Por padrão a leitura é feita a partir dos 
		# arquivos do diretório data/ do projeto.
		self.arq_dir = os.path.abspath('data/' + nome_arquivo + '.txt')
		arq = open(self.arq_dir, 'r')
		Q, alfabeto, funcao_transicao, q_inicial, q_finais = self.__ler_cabecalho(arq)
		transicoes = self.__ler_transicoes(arq)
		arq.close()
		info_automato = InfoAutomato(Q, alfabeto, funcao_transicao, q_inicial, q_finais, transicoes)
		return info_automato