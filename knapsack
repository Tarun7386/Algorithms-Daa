def knapsack(p,w,m):
  s=[[[0,0]]]
  for i in range(len(p)):
    s1=[]
    for t in range(len(s[i])):
      s1.append(s[i][t])

    for j in range(len(s[i])):
      p1=s[i][j][0]+p[i]
      w1=s[i][j][1]+w[i]
      if w1<=m:
        s1.append([p1,w1])
    r=[]
    for l in range(len(s1)-1):
      if s1[l][0]<s1[l+1][0] and s1[l][1]>s1[l+1][1]:
        r.append(s1[l])
    for n in range(len(r)):
      if r[n] in s1:
        s1.remove(r[n])
    s.append(s1)
  x=[0 for i in range(len(p))]
  c=len(p)
  st=s[-1][-1]
  while c>0:
    if st in s[c] and st in s[c-1]:
      c=c-1
      x[c]=0
    else:
      c=c-1
      x[c]=1
      st[0]=st[0]-p[c]
      st[1]=st[1]-w[c]
  px=0
  for i in range(len(p)):
    px=px+p[i]*x[i]
  print("maximum possible profit is:",px)
  print(x)
p=[1,2,5,6]
w=[2,3,4,5]
m=8
knapsack(p,w,m)
