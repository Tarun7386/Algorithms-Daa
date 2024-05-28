#dijskra
def dijskra(g):
  n=len(g)
  p=[99999]*n
  selected=[False]*n
  selected[0]=True
  p[0]=0
  count=0
  for i in range(n):
    if g[0][i]!=0:
      p1=p[0]+g[0][i]
      if p1<p[i]:
        p[i]=p1
  while count<n:
    minindex=-1
    minvalue=99999
    for i in range(len(p)):
      if selected[i]==False and minvalue>p[i]:
        minindex=i
        minvalue=p[i]
    selected[minindex]=True
    count=count+1
    for j in range(n):
      if g[minindex][j]!=0 and selected[j]==False:
        p2=p[minindex]+g[minindex][j]
        if p2<p[j]:
          p[j]=p2
  print("shortest dist from 0:")
  for i in range(len(p)):
    print(i,"--",p[i])
g= [
    [0, 2, 6, 0, 0, 0, 0],
    [2, 0, 0, 5, 0, 0, 0],
    [6, 0, 0, 8, 0, 0, 0],
    [0,5,8,0,10,15,0],
    [0, 0, 0, 10, 0, 0, 2],
    [0, 0, 0, 15,0, 0, 2],
    [0 ,0 ,0 ,0 ,2 ,6 ,0]
]
dijskra(g)

