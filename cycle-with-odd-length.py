import queue

with open("testes\col-teste3.txt", "r") as arquivo:
        lista_dados = [linha.strip() for linha in arquivo]
        # print(lista_dados, type(lista_dados[0]))

lista_convertida = [list(map(int, lista_dados.split(','))) for lista_dados in lista_dados]

#Função principal que determinará se o grafo G é bipartido.
#Indetificando se este contém ciclo ímpar
def containsOdd(G, src):
	global V
	
	# Cria um array de cores para armazenar
	# Cria um array de cores para armazenar e atribuir a cada vértice.
	# O número do vértice é usado como índice nesta matriz.
	#O valor '-1' de colorArr[i] é usado para indicar que nenhuma cor é atribuída ao vértice 'i'.
	# O valor '1' é usado para indicar a primeira cor atribuída e o valor '0' indica que a segunda cor está atribuída.
	colorArr = [-1] * V
	
	# Atribui a primeira cor à fonte
	colorArr[src] = 1

	# Cria uma fila (FIFO) de números de vértices e enfileira o vértice de origem para entrar em um BFS traversal
	q = queue.Queue()
	q.put(src)
	
	#Executa enquanto houver vértices na fila (semelhante ao BFS)
	while (not q.empty()):

		#Retira um vértice da fila
		u = q.get()
		
		# Retorna verdadeiro se houver um auto-loop
		if (G[u][u] == 1):
			return True

		# Encontra todos os vértices adjacentes não coloridos
		for v in range(V):
			
			# Se existir uma aresta de u a v e o destino v não é colorido
			if (G[u][v] and colorArr[v] == -1):
				
				# Atribui uma cor alternativa ao v adjacente de i
				colorArr[v] = 1 - colorArr[u]
				q.put(v)

			# Se existir uma aresta de u a v que o destino v é colorido com a mesma cor de u
			elif (G[u][v] and
				colorArr[v] == colorArr[u]):
				return True
			
	# Todos vértices adjacentes podem ser colorido com cores alternativa		
	return False

#Númer o de vértices	
V = 4

#Matriz do grafo teste
G = (lista_convertida)
# print(lista_convertida)

#Se G conter ciclos ímpares retorna Sim, do contrário Não 
if containsOdd(G, 0):
	print("Sim")
else:
	print("Não")