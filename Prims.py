def prims(g):
  inf=99999
  n=len(g)
  print("graph len", n)
  selected=[0]*n
  selected[0]=True
  count=1
  cost=0
  while count<n:
    minimum=inf
    a=0
    b=0
    for i in range(n):
      if selected[i]:
        for j in range(n):
          if (not selected[j]) and (g[i][j]):
            if minimum>g[i][j]:
              minimum=g[i][j]
              a=i
              b=j
    cost=cost+g[a][b]
    count=count+1
    selected[b]=True
    print(a,"-",b,"weight-", g[a][b])
  print("cost:",cost)

G = [
    [0, 2, 0, 4, 0, 5, 0],
    [2, 0, 7, 1, 3, 8, 4],
    [0, 7, 0, 0, 10, 0, 6],
    [4, 1, 0, 0, 2, 0, 0],
    [0, 3, 10, 2, 0, 0, 0],
    [5, 8, 0, 0, 0, 0, 1],
    [0, 4, 6, 0, 0, 1, 0]
]
prims(G)
