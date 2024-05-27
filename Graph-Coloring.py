def is_safe(graph, color, v, c, n):
  for i in range(n):
      if graph[v][i] and color[i] == c:
          return False
  return True
def graph_coloring(graph, m, color, v, n):
  if v == n:
      return True
  for c in range(1, m + 1):
      if is_safe(graph, color, v, c, n):
          color[v] = c
          if graph_coloring(graph, m, color, v + 1, n):
              return True
          color[v] = 0
  return False
graph = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]
n = len(graph)
m = 3
color = [0] * n 
if graph_coloring(graph, m, color, 0, n):
  print("Solution exists: ", color)
else:
  print("Solution does not exist")
