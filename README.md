# tp1TL

## Dependências:
  ### Python 3.6.5 (default)
  
  ### GCC 7.3.0
  
  ### GNU Make 4.1


# Para executar:

  (1) Através do terminal, acessar diretório onde se encontra o arquivo make.
  
  (2) Digitar "make" sem as aspas
  
  
# Diretório "data/" (Local de especificação de automatos):

  No diretório data encontram-se as especificações dos automatos utilizados pelo programa,
  sendo eles "afd.txt", "afn.txt" e "afne.txt".
  
  Caso seja necessário especificar outro automato é necessário que se siga as seguintes diretivas:
  
  (1) O novo automato deve ser descrito no arquivo que corresponde ao seu tipo, ou seja
      se for necessário especificar um AFN, deve-se faze-lo dentro do arquivo "afn.txt".
      
  (2) O arquivo deve ter a seguinte formatação:
  
      linha 1(Cabeçalho): Todos_estados Alfabeto Função_transição Estado_inicial Estados_finais
      linha 2: estado_1 transicao_1 transição_2 ... transição_n 
      linha 3: estado_2 transicao_1 transição_2 ... transição_n
      .
      .
      .
      linha k: estado_m transicao_1 transição_2 ... transição_n
      Com exceção a primeira linha do arquivo (cabeçalho) temos as demais que são as respectivas transições.
      Considere a seguinte explicação das transições descritas no arquivo:
      linha 2: estado_1 transicao_1 transição_2 ... transição_n
      Lê-se da seguinte maneira:
        A partir do estado_1 vamos para o estado da transição_1 processando o 1° símbolo do alfabeto descrito no cabeçalho.
        A partir do estado_1 vamos para o estado da transição_2 processando o 2° símbolo do alfabeto descrito no cabeçalho.
        A partir do estado_1 vamos para o estado da transição_n processando o n-ésimo símbolo do alfabeto descrito no cabeçalho.
        
      Exemplo real:
      q0,q1,q2,qf a,b afd q0 qf,q0
      q0 q1 q2
      q1 qf q2
      q2 q1 qf
      qf qf qf
      
      Considere a seguinte explicação das transições descritas no exemplo real acima:
      q0 q1 q2
      Lê-se da seguinte maneira:
        A partir do q0 vamos para o estado da q1 processando o símbolo 'a' do alfabeto descrito no cabeçalho.
        A partir do q0 vamos para o estado da q2 processando o símbolo 'b' do alfabeto descrito no cabeçalho.
        
   (4) A inserção das palavras a serem testadas se dá em tempo de execução como entrada do
       usuário após selecionar o automato desejado de acordo com as opções do menu.
