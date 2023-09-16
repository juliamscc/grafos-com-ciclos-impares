# Função para criar a lista de arestas
def createListOfEdges(graph):
	listofedges = graph[1:]
	edges = []
	for i in listofedges:
		e = list(map(int, i.split( )))
		edges.append(e)
	return edges

# Função verifica se uma subparte da floresta pode ser colorida com duas cores
def twoColorUtil(G, src, colorArr):
	colorArr[src] = 1 # Colore o nó com a primeira cor
	q = [src] # Cria uma fila com os nós a serem percorridos
	
	while q:
		u = q.pop(0) # pega o primeiro nó da fila

		for v in G[u]: # percorre os nós adjacentes a u
			if colorArr[v] == -1:
				colorArr[v] = 1 - colorArr[u] # colore com a cor direrente de u
				q.append(v) # adiciona o nó adjacente à fila
			elif colorArr[v] == colorArr[u]:		
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
			if not twoColorUtil(G, i, colorArr):
				return False
			return True

# Função que verifica a existência de ciclos ímpares
def isOddSum(edges, numNodes):
	G = [[] for i in range(numNodes)]

	for edge in edges: # Percorre as arestas
		u = edge[0] # Recebe o primeiro nó da aresta
		v = edge[1] # Recebe o segundo nó da aresta
		weight = edge[2] # Recebe o peso da aresta

		if weight % 2 == 1:
			G[u-1].append(v-1)
			G[v-1].append(u-1)

	return not twoColor(G, numNodes)

if __name__ == "__main__":
# Leitura dos arquivos de texto
	with open("testes\cows-test1.txt", "r") as file:
		text = file.read()

	graph = text.split('\n')

	numNodes = int(graph[0])
	edges = createListOfEdges(graph) 

	if isOddSum(edges, numNodes):
		print("Existem ciclos com peso ímpar no grafo.")
	else:
		print("Não existem ciclos com peso ímpar no grafo.")