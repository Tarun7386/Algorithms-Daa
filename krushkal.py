def krushkal(graph):
  n=len(graph)
  edges=[]
  for i in range(n):
    for j in range(i+1,n):
      if graph[i][j]!=0:
        edges.append((i,j,graph[i][j]))
  edges.sort(key=lambda x:x[2])
  mst=[]
  total_cost=0
  parent=[i for i in range(n)]
  def find(u):
    if parent[u]==u:
      return u
    return find(parent[u])
  def union(u,v):
    parent_u=find(u)
    parent_v=find(v)
    parent[parent_u]=parent_v
  for edge in edges:
    u,v,weight=edge
    if find(u)!=find(v):
      mst.append((u,v,weight))
      total_cost+=weight
      union(u,v)
  return mst,total_cost
t = [
    [0, 2, 0, 4, 0, 5, 0],
    [2, 0, 7, 1, 3, 8, 4],
    [0, 7, 0, 0, 10, 0, 6],
    [4, 1, 0, 0, 2, 0, 0],
    [0, 3, 10, 2, 0, 0, 0],
    [5, 8, 0, 0, 0, 0, 1],
    [0, 4, 6, 0, 0, 1, 0]
]
mst,t_cost=krushkal(t)
print("minimum spanning tree:")
for edge in mst:
  print(f"{edge[0]}--{edge[1]} : {edge[2]}")
print("total cost is ",t_cost)
