# Função para criar a lista de arestas
def createListOfEdges(graph):
	listofedges = graph[1:]
	edges = []
	for i in listofedges:
		e = list(map(int, i.split(' ')))
		edges.append(e)
	return edges

# Função verifica se uma subparte da floresta pode ser colorida com duas cores
def twoColorUtil(G, src, colorArr):
	colorArr[src] = 1 # Colore o nó com a primeira cor
	q = [src] # Cria uma fila com os nós a serem percorridos
	
	while len(q) > 0:
		u = q.pop(0) # pega o primeiro nó da fila

		for v in range(0, len(G[u])): # percorre os nós adjacentes a u
			if colorArr[G[u][v]] == -1:
				colorArr[G[u][v]] = 1 - colorArr[u] # colore com a cor direrente de u
				q.append(G[u][v]) # adiciona o nó adjacente à fila
			elif colorArr[G[u][v]] == colorArr[u]:		
				return False
	return True
	
# Função que verifica se o grafo pode ser colorido com duas cores
def twoColor(G, numNodes):
	# Cria uma lista para guardar as cores marcadas no grafo
	# -1 indica que o vétice não foi colorido
	# 1 e 0 representam a primeira e a segunda cor marcada respectivamente
	colorArr = [-1] * numNodes

	for i in range(numNodes):
		if colorArr[i] == -1:
			if twoColorUtil(G, i, colorArr) == False:
				return False
			return True

# Função que verifica a existência de ciclos ímpares
def isOddSum(edges, numNodes):
	G = [[] for i in range(2*numNodes)] # Acrescenta um pseudo nó para cada aresta (no caso de todas serem pares)
	
	pseudo = numNodes + 1
	pseudo_count = 0

	for i in range(1, len(edges)): # Percorre as arestas
		u = edges[i][0] # Recebe o primeiro nó da aresta
		v = edges[i][1] # Recebe o segundo nó da aresta

		if edges[i][2] % 2 == 1: # Se o peso for ímpar, apenas adiciona a aresta no grafo
			G[u].append(v)
			G[v].append(u)
		else: 
			# Adiciona um pseudo nó entre os nós da aresta
			G[u].append(pseudo)
			G[pseudo].append(u)
			G[v].append(pseudo)
			G[pseudo].append(v)
			pseudo_count += 1
			pseudo += 1
		
		if twoColor(G, numNodes + pseudo_count):
			return False
	return True

if __name__ == "__main__":
# Leitura dos arquivos de texto
	with open("testes\cows-test2.txt", "r") as file:
		text = file.read()

	# graph = text.split('\n')

	# numNodes = int(graph[0])
	# edges = createListOfEdges(graph) 
	# print(edges)
	numNodes = 3
	edges = [[1, 2, 1], [2, 3, 1], [1, 3, 1]]

	if isOddSum(edges, numNodes) == True:
		print("Existem ciclos com peso ímpar no grafo.")
	else:
		print("Não existem ciclos com peso ímpar no grafo.")