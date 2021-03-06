# BFS traversal algorithm
import Queue
print "no. of vertices: "
n = int(raw_input()) 
adj_matrix = [[int(j) for j in raw_input().split(" ")] for i in range(n)]

print adj_matrix

def BFS_traversal(matrix, v, start): 
	visited = [0]*v
	q = Queue.Queue() 
	q.put(start)
	visited[start] = 1
	while(q.empty() == False):
		s = q.get()
		print s
		for i in range(v):
			if matrix[s][i] == 1 and visited[i] == 0:
				q.put(i)
				visited[i] = 1

BFS_traversal(adj_matrix, n,0)