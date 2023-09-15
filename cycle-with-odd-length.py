import queue

def containsOdd(G, src):
	global V
	
	colorArr = [-1] * V
	
	colorArr[src] = 1
	
	q = queue.Queue()
	q.put(src)
	
	while (not q.empty()):
		u = q.get()
		
		if (G[u][u] == 1):
			return True

		for v in range(V):
			
			if (G[u][v] and colorArr[v] == -1):
				
				colorArr[v] = 1 - colorArr[u]
				q.put(v)
	
			elif (G[u][v] and
				colorArr[v] == colorArr[u]):
				return True
			
	return False
	
V = 4
G = [[0, 1, 0, 1],
	[1, 0, 1, 0],
	[0, 1, 0, 1],
	[1, 0, 1, 0]]

if containsOdd(G, 0):
	print("Yes")
else:
	print("No")