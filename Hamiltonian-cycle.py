def is_hamiltonian_cycle(graph,pos,path,visited):
  if pos==len(graph):
    if graph[path[pos-1]][0]==1:
      return True
    return False
  for v in range(1,len(graph)):
    if not visited[v] and graph[path[pos-1]][v]==1:
      visited[v]=True
      path[pos]=v
      if is_hamiltonian_cycle(graph,pos+1,path,visited):
        return True
      visited[v]=False
      path[pos]=-1
  return False
def find_hamiltonian_cycle(graph):
  n=len(graph)
  path=[-1]*n
  visited=[False]*n
  path[0]=0
  visited[0]=True
  if is_hamiltonian_cycle(graph,1,path,visited):
    return path
  else:
    return None
graph = [[0, 1, 1, 1, 0, 0],
         [1, 0, 1, 0, 1, 0],
         [1, 1, 0, 1, 1, 0],
         [1, 0, 1, 0, 1, 1],
         [0, 1, 1, 1, 0, 1],
         [0, 0, 0, 1, 1, 0]]
result=find_hamiltonian_cycle(graph)
if result:
  print("Hamiltonian cycle exists: ",result)
else:
  print("Hamiltonian cycle does not exist")
