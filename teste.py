# Python3 program to check if there
# is a cycle of total odd weight

# This function returns true if the current subpart
# of the forest is two colorable, else false.
def twoColorUtil(G, src, N, colorArr):
	
	# Assign first color to source
	colorArr[src] = 1
	
	# Create a queue (FIFO) of vertex numbers and
	# enqueue source vertex for BFS traversal
	q = [src]
	
	# Run while there are vertices in queue
	# (Similar to BFS)
	while len(q) > 0:
		
		u = q.pop(0)
		
		# Find all non-colored adjacent vertices
		for v in range(0, len(G[u])):
	
			# An edge from u to v exists and
			# destination v is not colored
			if colorArr[G[u][v]] == -1:
			
				# Assign alternate color to this
				# adjacent v of u
				colorArr[G[u][v]] = 1 - colorArr[u]
				q.append(G[u][v])
			
			# An edge from u to v exists and destination
			# v is colored with same color as u
			elif colorArr[G[u][v]] == colorArr[u]:		
				return False
		
	return True

# This function returns true if graph
# G[V][V] is two colorable, else false	
def twoColor(G, N):
	
	# Create a color array to store colors assigned
	# to all vertices. Vertex number is used as index
	# in this array. The value '-1' of colorArr[i]
	# is used to indicate that no color is assigned
	# to vertex 'i'. The value 1 is used to indicate
	# first color is assigned and value 0 indicates
	# second color is assigned.
	colorArr = [-1] * N
	
	# As we are dealing with graph, the input might
	# come as a forest, thus start coloring from a
	# node and if true is returned we'll know that
	# we successfully colored the subpart of our
	# forest and we start coloring again from a new
	# uncolored node. This way we cover the entire forest.
	for i in range(N):
		if colorArr[i] == -1:
			if twoColorUtil(G, i, N, colorArr) == False:
				return False
			
			return True

# Returns false if an odd cycle is present else true
# int info[][] is the information about our graph
# int n is the number of nodes
# int m is the number of informations given to us
def isOddSum(info, n, m):
	
	# Declaring adjacency list of a graph
	# Here at max, we can encounter all the
	# edges with even weight thus there will
	# be 1 pseudo node for each edge
	G = [[] for i in range(2*n)]
	
	pseudo, pseudo_count = n+1, 0
	for i in range(0, m):
		
		# For odd weight edges, we
		# directly add it in our graph
		if info[i][2] % 2 == 1:
			
			u, v = info[i][0], info[i][1]
			G[u].append(v)
			G[v].append(u)
		
		# For even weight edges, we break it
		else:
			u, v = info[i][0], info[i][1]

			# Entering a pseudo node between u---v
			G[u].append(pseudo)
			G[pseudo].append(u)
			G[v].append(pseudo)
			G[pseudo].append(v)
			
			# Keeping a record of number
			# of pseudo nodes inserted
			pseudo_count += 1

			# Making a new pseudo node for next time
			pseudo += 1
	
	# We pass number graph G[][] and total number
	# of node = actual number of nodes + number of
	# pseudo nodes added.
	return twoColor(G, n+pseudo_count)

# Driver function
if __name__ == "__main__":
	
	# 'n' correspond to number of nodes in our
	# graph while 'm' correspond to the number
	# of information about this graph.
	n, m = 3, 2
	info = [[1, 2, 1],
			[3, 2, 1],
			[3, 1, 1]]
					
	# This function break the even weighted edges in
	# two parts. Makes the adjacency representation
	# of the graph and sends it for two coloring.
	if isOddSum(info, n, m) == True:
		print("No")
	else:
		print("Yes")
	
# This code is contributed by Rituraj Jain
